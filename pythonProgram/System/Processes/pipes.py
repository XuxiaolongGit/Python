'''
派生一个子进程/程序，连接我的stdin/stdout和子进程的
stdin/stdout,我的读写映射到派生程序的输出和输入上，很像利用
subprocess模块绑定流一样
'''

import os,sys

def spawn(prog,*args):   # 传入程序名称，命令行参数
    stdinFd = sys.stdin.fileno() #获得流的描述符
    stdoutFd = sys.stdout.fileno()  #一般stdin=0，stdout=1

    parentStdin ,childStdout = os.pipe()  #创建两个IPC管道频道
    childStdin,parentStdout = os.pipe()  #pip返回
                            #(输入流文件描述符，输出流文件描述符)
    pid = os.fork()

    if pid:
        os.close(childStdout)  #分支之后,在父进程中：
        os.close(childStdin)
        os.dup2(parentStdin,stdinFd)
        os.dup2(parentStdout,stdoutFd)
    else:
        os.close(parentStdin)
        os.close(parentStdout)
        os.dup2(childStdin,stdinFd)
        os.dup2(childStdout,stdoutFd)
        args=(prog,)+args
        os.execvp(prog,args)
        assert False,'execvp failed!'

if __name__=='__main__':
    mypid = os.getpid()
    spawn('python','pipes-testcihld.py','spam')

    print('Hello 1 from parent',mypid)
    sys.stdout.flush()
    reply = input()
    sys.stderr.write('Parent got: "%s"\n'%reply)

    print('Hello 2 from parent',mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: "%s"\n'%reply[:-1])