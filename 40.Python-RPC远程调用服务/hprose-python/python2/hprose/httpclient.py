############################################################
#                                                          #
#                          hprose                          #
#                                                          #
# Official WebSite: http://www.hprose.com/                 #
#                   http://www.hprose.org/                 #
#                                                          #
############################################################

############################################################
#                                                          #
# hprose/httpclient.py                                     #
#                                                          #
# hprose httpclient for python 2.3+                        #
#                                                          #
# LastModified: Dec 25, 2018                               #
# Author: Ma Bingyao <andot@hprose.com>                    #
#                                                          #
############################################################

import httplib, re, threading, urlparse
from calendar import timegm
from hprose.common import HproseException
import time
from hprose.client import HproseClient

# _http2time from cookielib.py in python 2.5
EPOCH_YEAR = 1970

MONTHS_LOWER = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]

def _timegm(tt):
    year, month, mday, hour, minute, sec = tt[:6]
    if ((year >= EPOCH_YEAR) and (1 <= month <= 12) and (1 <= mday <= 31) and
        (0 <= hour <= 24) and (0 <= minute <= 59) and (0 <= sec <= 61)):
        return timegm(tt)
    else:
        return None

UTC_ZONES = {"GMT": None, "UTC": None, "UT": None, "Z": None}

TIMEZONE_RE = re.compile(r"^([-+])?(\d\d?):?(\d\d)?$")

def offset_from_tz_string(tz):
    offset = None
    if tz in UTC_ZONES:
        offset = 0
    else:
        m = TIMEZONE_RE.search(tz)
        if m:
            offset = 3600 * int(m.group(2))
            if m.group(3):
                offset = offset + 60 * int(m.group(3))
            if m.group(1) == '-':
                offset = -offset
    return offset

def _str2time(day, mon, yr, hr, minute, sec, tz):
    # translate month name to number
    # month numbers start with 1 (January)
    try:
        mon = MONTHS_LOWER.index(mon.lower())+1
    except ValueError:
        # maybe it's already a number
        try:
            imon = int(mon)
        except ValueError:
            return None
        if 1 <= imon <= 12:
            mon = imon
        else:
            return None

    # make sure clock elements are defined
    if hr is None: hr = 0
    if minute is None: minute = 0
    if sec is None: sec = 0

    yr = int(yr)
    day = int(day)
    hr = int(hr)
    minute = int(minute)
    sec = int(sec)

    if yr < 1000:
        # find "obvious" year
        cur_yr = time.localtime(time.time())[0]
        m = cur_yr % 100
        tmp = yr
        yr = yr + cur_yr - m
        m = m - tmp
        if abs(m) > 50:
            if m > 0: yr = yr + 100
            else: yr = yr - 100

    # convert UTC time tuple to seconds since epoch (not timezone-adjusted)
    t = _timegm((yr, mon, day, hr, min, sec, tz))

    if t is not None:
        # adjust time using timezone string, to get absolute time since epoch
        if tz is None:
            tz = "UTC"
        tz = tz.upper()
        offset = offset_from_tz_string(tz)
        if offset is None:
            return None
        t = t - offset

    return t

STRICT_DATE_RE = re.compile(
    r"^[SMTWF][a-z][a-z], (\d\d) ([JFMASOND][a-z][a-z]) (\d\d\d\d) (\d\d):(\d\d):(\d\d) GMT$")
WEEKDAY_RE = re.compile(
    r"^(?:Sun|Mon|Tue|Wed|Thu|Fri|Sat)[a-z]*,?\s*", re.I)
LOOSE_HTTP_DATE_RE = re.compile(
    r"""^
    (\d\d?)            # day
       (?:\s+|[-\/])
    (\w+)              # month
        (?:\s+|[-\/])
    (\d+)              # year
    (?:
          (?:\s+|:)    # separator before clock
       (\d\d?):(\d\d)  # hour:min
       (?::(\d\d))?    # optional seconds
    )?                 # optional clock
       \s*
    ([-+]?\d{2,4}|(?![APap][Mm]\b)[A-Za-z]+)? # timezone
       \s*
    (?:\(\w+\))?       # ASCII representation of timezone in parens.
       \s*$""", re.X)
def _http2time(text):
    """Returns time in seconds since epoch of time represented by a string.

    Return value is an integer.

    None is returned if the format of str is unrecognized, the time is outside
    the representable range, or the timezone string is not recognized.  If the
    string contains no timezone, UTC is assumed.

    The timezone in the string may be numerical (like "-0800" or "+0100") or a
    string timezone (like "UTC", "GMT", "BST" or "EST").  Currently, only the
    timezone strings equivalent to UTC (zero offset) are known to the function.

    The function loosely parses the following formats:

    Wed, 09 Feb 1994 22:23:32 GMT       -- HTTP format
    Tuesday, 08-Feb-94 14:15:29 GMT     -- old rfc850 HTTP format
    Tuesday, 08-Feb-1994 14:15:29 GMT   -- broken rfc850 HTTP format
    09 Feb 1994 22:23:32 GMT            -- HTTP format (no weekday)
    08-Feb-94 14:15:29 GMT              -- rfc850 format (no weekday)
    08-Feb-1994 14:15:29 GMT            -- broken rfc850 format (no weekday)

    The parser ignores leading and trailing whitespace.  The time may be
    absent.

    If the year is given with only 2 digits, the function will select the
    century that makes the year closest to the current date.

    """
    # fast exit for strictly conforming string
    m = STRICT_DATE_RE.search(text)
    if m:
        g = m.groups()
        mon = MONTHS_LOWER.index(g[1].lower()) + 1
        tt = (int(g[2]), mon, int(g[0]),
              int(g[3]), int(g[4]), float(g[5]))
        return _timegm(tt)

    # No, we need some messy parsing...

    # clean up
    text = text.lstrip()
    text = WEEKDAY_RE.sub("", text, 1)  # Useless weekday

    # tz is time zone specifier string
    day, mon, yr, hr, minute, sec, tz = [None]*7

    # loose regexp parse
    m = LOOSE_HTTP_DATE_RE.search(text)
    if m is not None:
        day, mon, yr, hr, minute, sec, tz = m.groups()
    else:
        return None  # bad format

    return _str2time(day, mon, yr, hr, minute, sec, tz)

_cookieManager = {}
_cookieManagerLock = threading.RLock()

def _setCookie(cookieList, host):
    _cookieManagerLock.acquire()
    try:
        for cookies in cookieList:
            if cookies == '': continue
            cookies = cookies.strip().split(';')
            cookie = {}
            value = cookies[0].strip().split('=', 1)
            cookie['name'] = value[0]
            if len(value) == 2:
                cookie['value'] = value[1]
            else:
                cookie['value'] = ''
            for i in xrange(1, len(cookies)):
                value = cookies[i].strip().split('=', 1)
                if len(value) == 2:
                    cookie[value[0].upper()] = value[1]
                else:
                    cookie[value[0].upper()] = ''
            # Tomcat can return SetCookie2 with path wrapped in "
            if 'PATH' in cookie:
                if cookie['PATH'][0] == '"':
                    cookie['PATH'] = cookie['PATH'][1:]
                if cookie['PATH'][-1] == '"':
                    cookie['PATH'] = cookie['PATH'][:-1]
            else:
                cookie['PATH'] = '/'
            if 'EXPIRES' in cookie:
                cookie['EXPIRES'] = _http2time(cookie['EXPIRES'])
            if 'DOMAIN' in cookie:
                cookie['DOMAIN'] = cookie['DOMAIN'].lower()
            else:
                cookie['DOMAIN'] = host
            cookie['SECURE'] = 'SECURE' in cookie
            if (cookie['DOMAIN'] not in _cookieManager):
                _cookieManager[cookie['DOMAIN']] = {}
            _cookieManager[cookie['DOMAIN']][cookie['name']] = cookie
    finally:
        _cookieManagerLock.release()

def _getCookie(host, path, secure):
    cookies = []
    _cookieManagerLock.acquire()
    try:
        for domain in _cookieManager:
            cookieList = _cookieManager[domain]
            if host.endswith(domain):
                names = []
                for name in cookieList:
                    cookie = cookieList[name]
                    if 'EXPIRES' in cookie and time.time() > cookie['EXPIRES']:
                        names.append(name)
                    elif path.startswith(cookie['PATH']):
                        if (((secure and cookie['SECURE']) or
                             not cookie['SECURE']) and cookie['value'] != ''):
                            cookies.append(cookie['name'] + '=' + cookie['value'])
                for name in names:
                    del _cookieManager[domain][name]
    finally:
        _cookieManagerLock.release()
    if len(cookies) > 0:
        return '; '.join(cookies)
    return ''

class HproseHttpClient(HproseClient):
    def __init__(self, uri = None):
        self.__header = {}
        self.__proxy = None
        self.timeout = 30
        self.keepAlive = True
        self.keepAliveTimeout = 300
        self.__scheme = None
        self.__port = None
        self.__host = None
        self.__ip = None
        self.__path = None
        self.__query = None
        self.__fragment = None
        self.__conn = None
        super(HproseHttpClient, self).__init__(uri)

    def setUri(self, uri):
        super(HproseHttpClient, self).setUri(uri)
        uri = urlparse.urlsplit(uri, 'http')
        self.__scheme = uri[0]
        if self.__scheme == 'https':
            self.__port = 443
        else:
            self.__port = 80
        netloc = uri[1]
        if "@" in netloc:
            netloc = netloc.split("@", 1)[1]
        if ":" in netloc:
            netloc = netloc.split(":", 1)
            self.__port = int(netloc[1])
            netloc = netloc[0]
        self.__host = netloc.lower()
        if self.__host == 'localhost':
            self.__ip = '127.0.0.1'
        else:
            self.__ip = self.__host
        self.__path = uri[2]
        self.__query = uri[-2]
        self.__fragment = uri[-1]

    def setProxy(self, host, port = None):
        if host == None:
            self.__proxy = None
        else:
            proxy = urlparse.urlsplit(host)
            scheme = proxy[0]
            if port == None:
                if self.__scheme == 'https':
                    port = 443
                else:
                    port = 80
            netloc = proxy[1]
            if "@" in netloc:
                netloc = netloc.split("@", 1)[1]
            if ":" in netloc:
                netloc = netloc.split(":", 1)
                port = int(netloc[1])
                netloc = netloc[0]
            host = netloc.lower()
            if host == 'localhost':
                ip = '127.0.0.1'
            else:
                ip = host
            self.__proxy = {'scheme': scheme, 'host': host, 'ip':ip, 'port': port}

    proxy = property(fset = setProxy)

    def setHeader(self, name, value):
        lname = name.lower()
        if (lname != 'content-type' and
            lname != 'content-length' and
            lname != 'host'):
            if value:
                self.__header[name] = value
            else:
                del self.__header[name]

    def __getconnect_old(self):
        if self.__proxy == None:
            if self.__scheme == 'https':
                httpclient = httplib.HTTPSConnection(self.__ip, self.__port)
            else:
                httpclient = httplib.HTTPConnection(self.__ip, self.__port)
        else:
            if self.__proxy['scheme'] == 'https':
                httpclient = httplib.HTTPSConnection(self.__proxy['ip'], self.__proxy['port'])
            else:
                httpclient = httplib.HTTPConnection(self.__proxy['ip'], self.__proxy['port'])
        return httpclient

    def __getconnect_new(self):
        if self.__proxy == None:
            if self.__scheme == 'https':
                httpclient = httplib.HTTPSConnection(self.__ip, self.__port, timeout = self.timeout)
            else:
                httpclient = httplib.HTTPConnection(self.__ip, self.__port, timeout = self.timeout)
        else:
            if self.__proxy['scheme'] == 'https':
                httpclient = httplib.HTTPSConnection(self.__proxy['ip'], self.__proxy['port'], timeout = self.timeout)
            else:
                httpclient = httplib.HTTPConnection(self.__proxy['ip'], self.__proxy['port'], timeout = self.timeout)
        return httpclient

    if httplib.HTTPConnection.__init__.func_code.co_argcount == 4:
        __getconnect = __getconnect_old
    else:
        __getconnect = __getconnect_new

    def __getconn(self):
        if not self.keepAlive:
            return self.__getconnect()
        if self.__conn == None:
            self.__conn = self.__getconnect()
        return self.__conn

    def _sendAndReceive(self, data):
        header = {'Content-Type': 'application/hprose'}
        header['Host'] = self.__host
        if (self.__port != 80):
            header['Host'] += ':' + str(self.__port)
        cookie = _getCookie(self.__host, self.__path, self.__scheme == 'https')
        if cookie != '':
            header['Cookie'] = cookie
        if self.keepAlive:
            header['Connection'] = 'keep-alive'
            header['Keep-Alive'] = str(self.keepAliveTimeout)
        else:
            header['Connection'] = 'close'
        for name in self.__header: header[name] = self.__header[name]
        httpclient = self.__getconn()
        if self.__proxy == None:
            path = urlparse.urlunsplit(('', '', self.__path, self.__query, self.__fragment))
        else:
            path = self._uri
        httpclient.request('POST', path, data, header)
        resp = httpclient.getresponse()
        if resp.status == 200:
            cookieList = resp.getheader('set-cookie', '').split(',')
            cookieList.extend(resp.getheader('set-cookie2', '').split(','))
            _setCookie(cookieList, self.__host)
            data = resp.read()
            if not self.keepAlive:
                httpclient.close()
            return data
        else:
            if not self.keepAlive:
                httpclient.close()
            raise HproseException, '%d:%s' % (resp.status, resp.reason)
