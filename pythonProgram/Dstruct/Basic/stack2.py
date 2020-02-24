"一个多实例栈类"

class error(Exception):pass #导入时：本地一场

class Stack:
    def __init__(self,start=[]): #self是当前实例的引用
        self.stack = []         #start是任意的序列类型:栈等
        for x in start:
            self.push(x)
        self.stack.reverse()

    def push(self,obj):
        self.stack = [obj]+self.stack

    def pop(self):
        if not self.stack:raise error('underflow')
        top,*self.stack = self.stack
        return top

    def top(self):
        if not self.stack:raise error('underflow')
        return self.stack[0]

    def empty(self):
        return not self.stack
    #重载
    def __repr__(self):
        return '[Stack:%s]' % self.stack

    def __eq__(self,other):
        return self.stack == other.stack

    def __len__(self):
        return len(self.stack)

    def __add__(self,other):
        return Stack(self.stack + other.stack)

    def __mul__(self,reps):
        return Stack(self.stack * reps)

    def __getitem__(self,offset):
        return self.stack[offset]

    def __getattr__(self,name):
        return getattr(self.stack,name)