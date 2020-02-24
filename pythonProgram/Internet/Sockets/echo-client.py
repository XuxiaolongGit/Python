"""
客户端：使用套接字来发送数据到服务器，输出服务器答复的每条信息行；
'localhost'意味着，服务器和客户端是运行在同一机器上的，可以让我们在
同一台机器上测试客户端和服务器；为了测试互联网，在远程机器上运行服务器，
并设置server Host 或 argv[1]到机器域名或IP得知；Python的套接字是一个
可以指的BSD的套接字接口，在系统C库中可获得标准套接字调用的对象方法
"""
import sys
from socket import *
serverHost = 'localhost'
serverPort = 50007

message = [b'Hello network world']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode for x in sys.argv[2:])

sockobj = socket(AF_INET,SOCK_STREAM)

for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    print("Client received:",data)
sockobj.close()