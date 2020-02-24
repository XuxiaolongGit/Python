'''
传入所有线程共享的mutex对象而非所有全局对象；和上下文管理器
语句一起使用，实现锁的自动获取/释放；添加休眠功能的调用以避免
繁忙的循环并模拟真实工作
'''

import _thread as thread,time

stdoutmutex = thread.allocate_lock()

numthreads = 5
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]

def counter(myId,count,mutex):
    for i in range(count):
        time.sleep(1/(myId+1))
        with mutex:
            print('[%s] => %s'%(myId,i))
    exitmutexes[myId].acquire()

for i in range(numthreads):
    thread.start_new_thread(counter,(i,5,stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes):
    time.sleep(0.25)     #循环并没有执行

print('Main thread exiting.')
#线程0 :     0     1     2     3     4    time.sleep(1)
#线程1 :   0  1  2  3  4              time.sleep(1/2)
#线程2 : 0 1  2 3  4                 time.sleep(1/3)
#线程3 : 0 1 2 3 4                   time.sleep(1/4)
#线程4 :01234                        time.sleep(1/5)