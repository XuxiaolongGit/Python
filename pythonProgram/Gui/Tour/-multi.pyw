'''
4个实例类作为独立的程序进程运行：multiprocessing；
multiprocessing允许我们使用参数启动已命名的函数，
但不过阔lambda表达式，因为它们再Windows上是不能pickle的
multiprocessing也有其自己 的IPC工具，如用于通信的管道
'''

from tkinter import *
from multiprocessing import Process
demoModules = ['demoDlg','demoRadio','demoCheck','demoScale']

def runDemo(modname):
    module = __import__(modname)
    module.Demo().mainloop()

if __name__ == '__main__':
    for modname in demoModules:
        Process(target=runDemo,args=(modname,)).start()

    root = Tk()
    root.title('Processes')
    Label(root,text='Multiple program demo:multiprocessing',bg='white').pack()
    root.mainloop()
