#设置表单对话框为模态；必须在销毁前通过输入取回

from tkinter import *
from entry2 import makeform,fetch,fields

def show(entries,popup):
    fetch(entries)
    popup.destroy()

def ask():
    popup=Toplevel()
    ents = makeform(popup,fields)
    Button(popup,text='OK',command=(lambda:show(ents,popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()

root = Tk()
Button(root,text='Dialog',command=ask).pack()
root.mainloop()