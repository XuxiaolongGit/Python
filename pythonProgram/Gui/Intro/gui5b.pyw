from gui5 import HelloButton

class MyButton(HelloButton):
    def __init__(self,parent=None,**configs):
        HelloButton.__init__(self,parent,**configs)
        self.pack()
        self.config(fg='red',bg='black',font=('courier',12),bd=5)
    def callback(self):
        print("Ignoring press!...")

if __name__=="__main__":
    MyButton(None,text="Hello subclass world").mainloop()