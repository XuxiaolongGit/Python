'''deriving children threads until you input 'q' '''

import _thread

def child(tid):
    print('Hello from thread',tid)

def parent():
    i=0
    while True:
        i += 1
        _thread.start_new_thread(child,(i,))
        #receive a function ojbect and an arguments tuple
        if input() == 'q':break

if __name__ == "__main__":
    parent()