'''
可创建Process类的子类，就像threading.Thread一样；Queue和
queue.Queue的使用方法类似，不过它不是线程间的工具，而是进程间
的工具
'''
import os,time,queue
from multiprocessing import Process,Queue


class Counter(Process):
    label = '@'
    def _init__(self,start,queue):
        Process.__init__(self)
        self.state = start
        self.post = queue


    def run(self):  #新进程中调用start()开始运行
        for i in range(3):
            time.sleep(1)
            self.state += 1
            print(self.label,self.pid,self.state)
            self.post.put([self.pid,self.state])
        print(self.label,self.pid,'-')


if __name__ == '__main__':
    print('start',os.getpid())
    expected = 9

    post = Queue()
    p = Counter(0,post)   #新进程 start=0
    q = Counter(100,post)  #新进程 start = 100
    r = Counter(1000,post)  #新进程 start = 1000
    p.start();q.start();r.start()

    while expected:
        time.sleep(0.5)
        try:
            data = post.get(block=False)
        except queue.Empty:
            print('no data...')
        else:
            print('posted:',data)
            expected -= 1
    p.join();q.join();r.join()
    print('finish',os.getpid(),r.exitcode)