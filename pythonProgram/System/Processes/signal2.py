'''
在python中设置和捕获定时暂停信号，time.sleep和定时
合用效果不好，所以在这里调用signal.pause来暂停操作，
直到接收到信号：
'''

import sys,signal,time

def now():
    return time.asctime()

def onSignal(signum,stackframe):
    print('Got alarm',signum,'at,',now())

while True:
    print('Setting gat',now())
    signal.signal(signal.SIGALRM,onSignal)
    signal.alarm(5)
    signal.pause()