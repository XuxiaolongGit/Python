"一般代码timer工具"

def test(reps,func,*args):
    import time
    start = time.clock()
    for i in range(reps):
        func(*args)
    return time.clock() - start
