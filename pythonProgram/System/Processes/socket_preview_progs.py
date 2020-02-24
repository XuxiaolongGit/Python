'''
同样的套接字，除了在线程间通信，还在独立程序间通信；此处的服务器在进程
中运行，为线程和进程中的客户端提供服务；套接字是机器水平的全局对象，
类似fifo，无需共享内存
'''

from socket_preview import client,server
import sys,os
from threading import Thread

mode = int(sys.argv[1])
if mode == 1:
    server()
elif mode == 2:
    client('client:process=%s' %os.getpid())
else:
    for i in range(5):
        Thread(target=client,args=('client:thread = %s'%i)).start()