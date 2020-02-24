''''''
'''
because on the windows platform,so we can't
run the code,there so many contradictions 
between Windows System Module and the operation
of branch.
'''

import os,time
def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s spawned'% (os.getpid(),i))
    for i in range(5):
        pid = os.fork()
        if pid != 0:
            print('Process %d spawned'%pid)
        else:
            counter(5)
            os._exit(0)
    print('Main process exiting.')