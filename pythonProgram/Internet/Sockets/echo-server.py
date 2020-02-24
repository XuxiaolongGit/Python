'''
服务器端：在某一端口上开启一个TCP/IP套接字，监听来自客户端的消息，并且
发送一个应答；这是一个简单的客户端的每一次的listen/reply会话，但它进入
一个无限循环来监听更多的客户端，只要这个服务器脚本一直运行客户端上可能运
行在远程机器上，或者如果使用“本地主机”作为服务器，那么就在同一台计算机
上运行
'''
from socket import *
myHost = ''
myPort = 50007

sockobj = socket(AF_INET,SOCK_STREAM)
sockobj.bind((myHost,myPort))
sockobj.listen(5)

while True:
    connection,address = sockobj.accept()
    print("Server connected by",address)
    while True:
        data = connection.recv(1024)
        if not data:break
        connection.send(b'Echo=>'+data)
        connection.close()
