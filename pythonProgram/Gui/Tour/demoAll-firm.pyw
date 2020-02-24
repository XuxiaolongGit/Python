'''
一个窗口上的4个演示类组件（子框架）
这一个窗口上5个Quitter按钮，每个按钮都能终止整个GUI，
在容器、独立窗口或进程中，GUI能够作为框架来重复使用
'''

from tkinter import *
from quitter import Quitter
demoModules = ['demoDlg','demoCheck','demoRadio','demoScale']

parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)
        part = module.Demo(root)
        part.config(bd=2,relief=GROOVE)
        part.pack(side=LEFT,expand=YES,fill=BOTH)
        parts.append(part)

def dumpState():
    for part in parts:
        print(part.__module__ + ':',end=' ')
        if hasattr(part,'report'):
            part.report()
        else:
            print('none')

root = Tk()
root.title('Frames')
Label(root,text='Multiple Frame demo',bg='white').pack()
Button(root,text='States',command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()