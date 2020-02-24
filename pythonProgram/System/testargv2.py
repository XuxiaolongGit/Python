"collect command-line options in a dirctionary"

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0]== '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:] #this step eliminates the first argument : filename testargv2.py
    return opts

if __name__ == "__main__":
    from sys import argv
    myargs = getopts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    print(myargs)