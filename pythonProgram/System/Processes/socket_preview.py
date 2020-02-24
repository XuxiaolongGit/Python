"""
套接字用于跨任务通信：启动线程，相互通过套接字通信；也适用于独立程序，
因为套接字是系统级别的，类似FIFO，；书中GUI和Internet部分有更贴近
实践的套接字用例；某些套接字服务器可能还需要与线程或进程中的客户端通信；
套接字传输字节字符串，后者可以是pickle后的对象或编码后的Unicode文本；
注意，如果线程中打印输出可能重叠的话，仍需要同步化操作
"""

from socket import socket,AF_INET,SOCK_STREAM

port = 50008
host = 'localhost'

def server():
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind(('',port))
    sock.listen(5)
    while True:
        conn,addr = sock.accept()
        data = conn.recv(1024)
        reply = 'server got: [%s]'%data
        conn.send(reply.encode())

def client(name):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect((host,port))
    sock.send(name.encode())
    reply = sock.recv(1024)
    sock.close()
    print('client got: [%s]'%reply)


if __name__ == '__main__':
    from threading import Thread
    sthread = Thread(target=server)
    sthread.daemon = True
    sthread.start()
    for i in range(5):
        Thread(target=client,args=('client%s'%i,)).start()