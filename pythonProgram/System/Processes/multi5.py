'''
使用multiprocessing起始新程序，不论os.fork是否可用
'''

import os
from multiprocessing import Process

def runprogram(arg):
    os.execlp('python','python','child.py',str(arg))

if __name__ == '__main__':
    for i in range(5):
        Process(target=runprogram,args=(i,)).start()
    print('parent exit')