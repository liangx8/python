import socket
import os.path
import sys
import getopt
import time
BUF_SIZE=128*1024
PORT = 50007              # Arbitrary non-privileged port
def sendFile(fn):
    fnsize=os.path.getsize(fn)
    count = 0
    stage = int(fnsize / 100)
    stage_idx = 0
    HOST = ''                 # Symbolic name meaning all available interfaces
    with open(fn,'rb') as src:
        print('wait incoming request')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('file is sending...')
                tstart=time.time_ns()
                while count < fnsize:
                    buf = src.read(BUF_SIZE)
                    t = len(buf)
                    count = count + t
                    conn.sendall(buf)
                    if count > stage * stage_idx:
                        stage_idx = stage_idx + 1
                        print("{}%".format(stage_idx))
                tend=time.time_ns()
                speed=count/(tend-tstart)* 1000000000 / (1024* 1024)
                
                print("{}/{}={:.2f}MB/sec".format(count,tend-tstart,speed))
            conn.close()
            s.close()
        
def recvFile(fn,host,port):
#    HOST = '127.0.0.1'    # The remote host
 #   PORT = 50007              # The same port as used by the server
    dst = open(fn,'wb')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            data = s.recv(1024)
            dst.write(data)
            if  not data:
                break
        s.close()
    dst.close()

if __name__ == "__main__":
    try:
        opts,args=getopt.getopt(sys.argv[1:],'s:c:a:',[])
        targetAddr=None
        saveName=None
        for o,a in opts:
            if o== '-s':
                sendFile(a)
                sys.exit(0)
            if o == '-c':
                saveName=a
            if o == '-a':
                targetAddr=a
        if targetAddr:
            recvFile(saveName,targetAddr,PORT)
    except getopt.GetoptError as err:
        print(err)
