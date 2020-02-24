'''
使用多进程共享内存对象进行通信。传输的对象是共享的，但在windows下
不共享全局对象。这里最后那个测试代表了通常的用例：分配工作
'''

import os
from multiprocessing import Process,Value,Array

procs = 3
count = 0            #每个进程各自的全局对象，并非共享

def showdata(label,val,arr):
    '''在这个进程中打印数据值'''
    msg = '%-12s: pid:%4s,global:%s,value:%s,array:%s'
    print(msg%(label,os.getpid(),count,val.value,list(arr)))

def updater(val,arr):
    '''通过共享内存进行通信'''
    global count
    count+=1
    val.value+=1
    for i in range(3):arr[i]+=1

if __name__ == '__main__':
    scalar = Value('i',0)
    vector = Array('d',procs)

    showdata('parent start',scalar,vector)

    p = Process(target=showdata,args=('child',scalar,vector))
    p.start();p.join()

    print('\nloop1(updates in parent,serial children)...')
    for i in range(procs):
        count += 1
        scalar.value +=1
        vector[i] +=1
        p = Process(target=showdata,args=(('process %s'%i),scalar,vector))
        p.start();p.join()

    print('\nloop2 (updates in parent,parallel children)...')
    ps = []
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i]+=1
        p = Process(target= showdata,args=(('process %s'%i),scalar,vector))
        p.start()
        ps.append(p)
    for p in ps:p.join()

    print('\nloop3 (updates in serial children)...')
    for i in range(procs):
        p =Process(target = updater,args=(scalar,vector))
        p.start()
        p.join()
    showdata('parent temp',scalar,vector)
    ps =[]
    print('\nloop4 (updates in parallel children)...')
    for i in range(procs):
        p = Process(target=updater,args=(scalar,vector))
        p.start()
        ps.append(p)
    for p in ps:p.join()

    showdata('parent end',scalar,vector)