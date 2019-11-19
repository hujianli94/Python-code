import requests
import time
import datetime
import re
from urllib import parse

# 用户登录
def login(username, password):
    #坐标参考：40,40,114,35,192,39,257,36,42,115,119,107,185,124,272,117
    code_list = {
        '1': '40,40,',
        '2': '114,35,',
        '3': '192,39,',
        '4': '257,36,',
        '5': '42,115,',
        '6': '119,107,',
        '7': '185,124,',
        '8': '272,117'
    }
    #请求头
    headers = { 'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/63.0.3218.0 Safari/537.36',
                'Referer':
                'https://kyfw.12306.cn/otn/login/init'}

    url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
    #忽略证书验证
    r = session.get(url, headers=headers, verify=False)
    #下载验证码图片
    f = open('code.png','wb')
    f.write(r.content)
    f.close()
    #输入验证码图片位置,多个验证码用英文逗号分开
    code=input("请输入验证码：")
    get_code = ''
    for i in code.split(','):
        # 根据输入每组图片的组号，获取对应的坐标位置
        get_code += code_list[i]
    #验证码校验
    data={
        'answer':get_code,
        'login_site':'E',
        'rand':'sjrand'
    }
    url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
    r = session.post(url, data=data)
    print(r.text)
    if '验证码校验失败' not in str(r.text):
        # 用户登录
        url = 'https://kyfw.12306.cn/passport/web/login'
        data = {
            'username': username,
            'password': password,
            'appid': 'otn'
        }
        r = session.post(url, data=data)
        print(r.text)
        if '密码输入错误' not in str(r.text):
            #登录验证第一次请求
            url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
            data = {
                'appid': 'otn'
            }
            r = session.post(url, data=data)
            #登录验证第二次请求
            newapptk = r.json()['newapptk']
            url = 'https://kyfw.12306.cn/otn/uamauthclient'
            data = {
                'tk': newapptk
            }
            r=session.post(url, data=data)
            print(r.text)
            return True
        else:
            return False
    return False

# 获取城市编号
def city_name():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9031'
    city_code = session.get(url)
    city_code_list = city_code.text.split("|")
    city_dict = {}
    for k, i in enumerate(city_code_list):
        if '@' in i:
            # 城市名作为字典的键，城市英文编号作为字典的值
            city_dict[city_code_list[k + 1]] = city_code_list[k + 2]
    return (city_dict)



# 获取车次信息
def train_info(train_date, query_from_station_name, query_to_station_name):
    #调用函数city_name获取城市编号
    city_dict = city_name()
    from_station = city_dict[query_from_station_name]
    to_station = city_dict[query_to_station_name]
    # 获取车次信息
    while 1:
        # 第一次请求
        url = 'https://kyfw.12306.cn/otn/leftTicket/log?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (train_date, from_station, to_station)
        r = session.get(url)
        # 第二次请求
        # 请求地址的query可能变为queryA，可通过try……except控制
        try:
            url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (train_date, from_station, to_station)
            r = session.get(url)
            test = r.json()['data']['result']
        except:
            url = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (
            train_date, from_station, to_station)
            r = session.get(url)
        time.sleep(2)
        if '非法请求' not in str(r.text) and '"result":[]' not in str(r.text):
            train_info_info = r.json()
            train_info_dict = {}
            for i in train_info_info['data']['result']:
                train_info_status = i.split('|')
                if train_info_status[0] != '':
                    train_info_dict['secretStr'] = train_info_status[0]
                    train_info_dict['train_no'] = train_info_status[2]
                    train_info_dict['stationTrainCode'] = train_info_status[3]
                    train_info_dict['fromStationTelecode'] = train_info_status[4]
                    train_info_dict['toStationTelecode'] = train_info_status[7]
                    train_info_dict['leftTicket'] = train_info_status[12]
                    train_info_dict['train_location'] = train_info_status[15]
                    return train_info_dict

# 预订车票
def train_order(secretStr, train_date, query_from_station_name, query_to_station_name):
    # 获取当前日期
    back_train_date = datetime.datetime.now().strftime('%Y-%m-%d')
    # 用户登录检查
    url = 'https://kyfw.12306.cn/otn/login/checkUser'
    data = {
        '_json_att': ''
    }
    r = session.post(url, data=data)
    # 提交车票预订请求
    url = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
    data = {
        'secretStr': secretStr,
        'train_date': train_date,
        'back_train_date': back_train_date,
        'tour_flag': 'dc',
        'purpose_codes': 'ADULT',
        'query_from_station_name': query_from_station_name,
        'query_to_station_name': query_to_station_name,
        'undefined': ''
    }
    r = session.post(url, data=data)



# 生成订单
def creat_order(name, identity_card, phone_number, train_date, train_info_dict):
    # 获取Doc标签的数据
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
    data = {
        '_json_att': ''
    }
    r = session.post(url, data=data)
    # 获取参数
    key_check_isChange = r.text.split('key_check_isChange')[1].split(',')[0].replace(':', '').replace("'", '').strip()
    get_token = r.text.split('globalRepeatSubmitToken')[1].split(';')[0].replace('=', '').replace("'", '').strip()
    seat_code_str = r.text.split('ticket_seat_codeMap=')[1].split(';')[0].strip()
    # 找出席别编号并去重
    temp_list = re.findall(r"'id':'(.+?)',", seat_code_str)
    temp_list = list(set(temp_list))
    seatType = temp_list[1]

    # 检查订单信息
    # 构建请求参数，name-乘客姓名，identity_card-身份证号，phone_number-电话号码，票种为成人票
    oldPassengerStr = name + ',1,' + identity_card + ',1_'
    passengerTicketStr = seatType + ',0,1,' + name + ',1,' + identity_card + ',' + phone_number + ',N'
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'
    data = {
        'cancel_flag': '2',
        'bed_level_order_num': '000000000000000000000000000000',
        'passengerTicketStr': passengerTicketStr,
        'oldPassengerStr': oldPassengerStr,
        'tour_flag': 'dc',
        'randCode': '',
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN': get_token
    }
    r = session.post(url, data=data)
    # 提交订单信息
    # train_date，train_no,stationTrainCode,fromStationTelecode,toStationTelecode,
    # leftTicket,train_location来自车次信息
    # seatType和REPEAT_SUBMIT_TOKEN来自Doc标签的数据
    # purpose_codes和_json_att固定不变
    while 1:
        url = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'
        # 日期格式化处理
        check_ticket_date = train_date + ' 00:00:00'
        timeArray = time.strptime(check_ticket_date, "%Y-%m-%d %H:%M:%S")
        date = time.strftime("%a %b %d %Y", timeArray)
        data = {
            'train_date': date + ' GMT+0800 (中国标准时间)',
            'train_no': train_info_dict['train_no'],
            'stationTrainCode': train_info_dict['stationTrainCode'],
            'seatType': seatType,
            'fromStationTelecode': train_info_dict['fromStationTelecode'],
            'toStationTelecode': train_info_dict['toStationTelecode'],
            #leftTicket进行数据格式化处理
            'leftTicket': parse.unquote(train_info_dict['leftTicket']),
            'purpose_codes': '00',
            'train_location': train_info_dict['train_location'],
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': get_token
        }
        r = session.post(url, data=data)
        print(r.text)
        # 判断请求是否成功
        if '系统繁忙，请稍后重试' not in str(r.text):
            break
    # 生成订单
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'
    data = {
        'passengerTicketStr': passengerTicketStr,
        'oldPassengerStr': oldPassengerStr,
        'randCode': '',
        'purpose_codes': '00',
        'key_check_isChange': key_check_isChange,
        'leftTicketStr': train_info_dict['leftTicket'],
        'train_location': train_info_dict['train_location'],
        'choose_seats': '',
        'seatDetailType': '000',
        'roomType': '00',
        'dwAll': 'N',
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN': get_token
    }
    r = session.post(url, data=data)
    print(r.text)


if __name__ == '__main__':
    session = requests.session()
    # 网站账号密码
    username = '13435423143'
    password = 'XXXXXXXX'
    login_info = login(username, password)
    if login_info:
        train_date = 'YYYY-MM-DD'
        query_from_station_name = '广州'
        query_to_station_name = '武汉'
        train_info_dict = train_info(train_date, query_from_station_name, query_to_station_name)
        secretStr = parse.unquote(train_info_dict['secretStr'])
        train_order(secretStr, train_date, query_from_station_name, query_to_station_name)
        # 乘客信息
        name = '黄永祥'
        identity_card = 'XXXXXXXXX'
        phone_number = '13435423143'
        creat_order(name, identity_card, phone_number, train_date, train_info_dict)