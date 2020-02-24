'''
使用多进程匿名管道进行通信。返回两个connection对象来分别代表
管道的两端：对象从一端发送，在另一端接收，不过管道默认是双向的
'''
import os
from multiprocessing import Process,Pipe

def sender(pipe):
    '''在匿名管道上向父进程发送对象'''
    pipe.send(['spam']+[42,'ages'])
    pipe.close()

def talker(pipe):
    '''通过管道发送和接收对象'''
    pipe.send(dict(name='Bob',spam=42))
    reply = pipe.recv()
    print('talker got:',reply)

if __name__ == "__main__":
    (parentEnd,childEnd) = Pipe()
    Process(target=sender,args=(childEnd,)).start()
    print('parent got:',parentEnd.recv())
    parentEnd.close()

    (parentEnd,childEnd) = Pipe()
    child = Process(target=talker,args = (childEnd,))
    child.start()
    print('parent got:',parentEnd.recv())
    parentEnd.send({x*2 for x in 'spam'})
    child.join()
    print('parent exit')
