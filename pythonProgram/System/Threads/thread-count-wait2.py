'''
使用简单的共享全局数据（不是mutexes）在父/主线程中
探知线程何时结束；线程共享列表但不共享列表里的对象，
假设列表在内存中创建后不会移动
'''

import _thread as thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10

def counter(myId,count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s'%(myId,i))
        stdoutmutex.release()
    exitmutexes[myId] = True #向主线程发送信号

for i in range(10):
    thread.start_new_thread(counter,(i,100))

while False in exitmutexes:pass
print('Main thread exiting.')
