# -*- coding:utf-8 -

def more(text,numlines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['y','Y']:break

if __name__ == '__main__':
    import sys
    print(open(sys.argv[0],encoding='utf-8').read(),10)