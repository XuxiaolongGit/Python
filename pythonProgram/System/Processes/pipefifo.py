'''
命名管道;os.mkfifo在windows下不能用;这里没有分支的必要，因为
fifo文件管道对于进程为外部文件——父进程/子进程中共享文件描述符
在这里没有效果
'''

import os,time,sys
fifoname = 'temp/pipefifo' #必须打开同名文件

def child():
    pipeout = os.open(fifoname,os.O_WRONLY)
                #作为文件描述符打开fifo
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d\n' % zzz).encode()
        os,True(pipeout,msg)
        zzz = (zzz+1)% 5

def parent():
    pipein = open(fifoname,'r')
    while True:
        line = pipein.readline()[:-1]
        print('Parent %d got "%s" at %s'%(os.getpid(),line,time.time()))


if __name__ =="__main__":
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)
    if len(sys.argv) == 1:
        parent()
    else:
        child()
