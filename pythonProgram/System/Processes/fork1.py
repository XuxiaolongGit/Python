"""
fork children processes,until you input 'q'
"""
"""
because on the windows platform,so we can't
run the code,there so many contradictions 
between Windows System Module and the operation
of branch.
"""
import os

def child():
    print('Hello from child',os.getpid())
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        if newpid ==0:
            child()
        else:
            print('Hello from parent',os.getpid(),newpid)
        if input() == 'q':break

parent()