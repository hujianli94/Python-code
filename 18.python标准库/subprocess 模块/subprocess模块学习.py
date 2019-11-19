#!/usr/bin/env python
#-*- coding:utf8 -*-
'''
call(*popenargs, timeout=None, **kwargs):
    """Run command with arguments.  Wait for command to complete or
    timeout, then return the returncode attribute.

    The arguments are the same as for the Popen constructor.  Example:

    retcode = call(["ls", "-l"])  输入和输出绑定到父进程，返回新进程退出码
    """
check_call(*popenargs, **kwargs):
    """Run command with arguments.  Wait for command to complete.  If
    the exit code was zero then return, otherwise raise
    CalledProcessError.  The CalledProcessError object will have the
    return code in the returncode attribute.

    The arguments are the same as for the call function.  Example:

    check_call(["ls", "-l"]) 输入和输出绑定到父进程，返回新进程退出码，退出码为0正常，非0引发CalledProcessError

check_output(*popenargs, timeout=None, **kwargs):
    创建新进程运行程序，返回新进程的输出

getstatusoutput(cmd):
    """    Return (status, output) of executing cmd in a shell.

    Execute the string 'cmd' in a shell with 'check_output' and
    return a 2-tuple (status, output). Universal newlines mode is used,
    meaning that the result with be decoded to a string.

    A trailing newline is stripped from the output.
    The exit status for the command can be interpreted
    according to the rules for the function 'wait'. Example:

    import subprocess
    subprocess.getstatusoutput('ls /bin/ls')
    (0, '/bin/ls')
    subprocess.getstatusoutput('cat /bin/junk')
    (256, 'cat: /bin/junk: No such file or directory')
    subprocess.getstatusoutput('/bin/junk')
    (256, 'sh: /bin/junk: not found')
    """
getoutput(cmd):
    """Return output (stdout or stderr) of executing cmd in a shell.

    Like getstatusoutput(), except the exit status is ignored and the return
    value is a string containing the command's output.  Example:
    import subprocess
    subprocess.getoutput('ls /bin/ls')
    '/bin/ls'

check_output(*popenargs, timeout=None, **kwargs):
    r"""Run command with arguments and return its output.

    If the exit code was non-zero it raises a CalledProcessError.  The
    CalledProcessError object will have the return code in the returncode
    attribute and output in the output attribute.

    The arguments are the same as for the Popen constructor.  Example:

    check_output(["ls", "-l", "/dev/null"])
    b'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'

'''
"""
import subprocess
print("call() test :",subprocess.call(['python','hello_word.py']))
print('')
print("check_call() test",subprocess.check_call(['python','hello_word.py']))
print()
print("getstatusoutput(cmd) test",subprocess.getstatusoutput(['python','hello_word.py']))
print()
print("getoutput(cmd): test",subprocess.getoutput(["python","hello_word.py"]))
print()
print("check_output(): test",subprocess.check_call(["python","hello_word.py"]))
"""
import subprocess
p = subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE)
out = p.stdout.read()
print(out)

p = subprocess.Popen("wc",shell=True,stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = p.communicate(0)

p1 = subprocess.Popen("ls -l",shell=True,stdout=subprocess.PIPE)
p2 = subprocess.Popen("wc",shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)
out = p2.stdout.read()



"""
import subprocess
print("$ nslookup www.python.org")
r = subprocess.call(['nslookup','www.python.org'])
print("Exit code:", r)
"""

'''
# 子进程如果需要输入，可通过communicate()方法输入
import subprocess
print("$ nslookup")
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)
'''

'''
import subprocess
pingP=subprocess.Popen(args='ping -n 2 www.sina.com.cn', shell=True, stdout=subprocess.PIPE)
pingP.wait()        #等待进程完成
print(pingP.stdout.read().decode('gbk'))  #读取进程的输出信息
print("进程的PID信息为：{}".format(pingP.pid))
print("Process的return值为:{}".format(pingP.returncode))

'''

