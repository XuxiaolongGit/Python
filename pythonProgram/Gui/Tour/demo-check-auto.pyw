# 复选按钮，简单的方法

from tkinter import *
root = Tk()
states = []
for i in range(10):
    var = IntVar()
    chk = Checkbutton(root,text=str(i),variable=var)
    chk.pack(side=LEFT)
    states.append(var)
root.mainloop()
print([var.get() for var in states])
print(list(map(lambda var:var.get(),states)))