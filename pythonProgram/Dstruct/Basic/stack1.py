"一个共享栈模块"

stack = []  #第一次导入时

class error(Exception):pass   #本地异常:stack1.error

def push(obj):
    global stack        #用"global"来修改
    stack = [obj] + stack #把元素添加到列表前面

def pop():
    global stack
    if not stack:
        raise error('stack under flow') #抛出本地异常
    top,*stack = stack      #从列表前面弹出元素
    return top

def top():
    if not stack:             #抛出本地异常
        raise error('stack underflow') #也可以抛出IndexError
    return stack[0]

#判断栈是否为空？
def empty():
    return not stack

#判断元素是否存在？
def member(obj):
    return obj in stack

#根据位置返回栈中元素
def item(offset):
    return stack[offset]

#返回栈的长度
def length():
    return len(stack)

def dump():
    print('<Stack:%s>'%stack)