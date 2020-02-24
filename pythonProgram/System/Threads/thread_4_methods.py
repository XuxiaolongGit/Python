import threading,_thread

def action(i):
    print(i**32)

#带有状态的子类
class Mythread(threading.Thread):
    def __init__(self,i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):
        print(self.i**2)

Mythread(2).start()

#传入行为
thread = threading.Thread(target=(lambda:action(2)))
thread.start()                 #run调用target

#同上，但是没有lambda函数将状态封装起来

threading.Thread(target=action,args=(2,)).start()  #可调用对象及其参数

#基本的线程模块
_thread.start_new_thread(action,(2,))  #所有函数都适用的接口

#带有状态的非线程类，OOP方式
class Power:
    def __init__(self,i):
        self.i = i
    def action(self):
        print(self.i ** 32)

obj = Power(2)
threading.Thread(target=obj.action).start() #线程运行绑定方法


#利用嵌套作用域保留状态
def action2(i):
    def power():
        print(i**32)
    return power

threading.Thread(target=action2(2)).start()

#用基本的线程模块实现二者
_thread.start_new_thread(obj.action,())
_thread.start_new_thread(action(2),())