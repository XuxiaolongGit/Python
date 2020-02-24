'''
在python中捕获信号；将信号编号N作为命令行参数传入，利用shell命令
"kill -N pid"向这个进程发送信号；大多数信号处理器在捕获信号后转到
Python中处理（关于SIGCHLD的细节请参考“网络脚本”这一章），signal
模块在windows下可用，不过仅定义了少数几种信号类型，而且没有os.kll;
'''

import sys,signal,time

def now():
    return time.ctime(time.time())

def onSignal(signum,stackfram):  #python信号处理器
    print('Got signal',signum,'at',now())

signum = int(sys.argv[1])
signal.signal(signum,onSignal)
while True:
    signal.pause()