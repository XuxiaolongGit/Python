'''
分支子进程，用os.wait观察其退出状态；分支在Unix和Cygwin下能够进行
但在Windows Python 3.1标准版本中不能；请注意：派生线程
共享全局变量，但每个分支进程拥有其自己的全局变量副本（分支共享文件描述符）
exitstat在这里将保持不变，而如果是线程的话将发生变化

'''
import os
exitstat = 0

def child():
    global exitstat
    exitstat +=1
    print('Hello from child',os.getpid(),exitstat)
    os._exit(exitstat)
    print('never reached')

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pid,status = os.wait()
            print('Parent got',pid,status,(status >> 8))
            if input() == 'q':break

if __name__ == '__main__':
    parent()