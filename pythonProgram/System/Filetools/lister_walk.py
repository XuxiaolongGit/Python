'''
use os.walk accomplish the enumeration of
directory trees
'''

import sys,os
def lister(root): #根目录
    for (thisdir,subshere,fileshere) in os.walk(root):
        print('['+thisdir + ']')
        for fname in fileshere:
            path = os.path.join(thisdir,fname)
            print(path)


if __name__ == '__main__':
    lister(sys.argv[1])