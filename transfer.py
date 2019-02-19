import socket
import os.path
import sys
BUF_SIZE=128*1024
def sendFile(fn):
    units=("Byte","KB","MB","GB")
    fnsize=os.path.getsize(fn)
    count = 0
    stage = int(fnsize / 100)
    stage_idx = 0
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 50007              # Arbitrary non-privileged port
    unit=0
    showsize=fnsize
    while showsize >= 1024:
        showsize = int(showsize/1024)
        unit=unit+1
        if unit==2:
            break
    
    
    print("{} {}".format(showsize,units[unit]))
    with open(fn,'rb') as src:
        print('wait incoming request')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('file is sending...')
                
                while count < fnsize:
                    buf = src.read(BUF_SIZE)
                    t = len(buf)
                    count = count + t
                    conn.sendall(buf)
                    if count > stage * stage_idx:
                        stage_idx = stage_idx + 1
                        print("{}%".format(stage_idx))
        s.close()
def recvFile(fn):
    HOST = '127.0.0.1'    # The remote host
    PORT = 50007              # The same port as used by the server
    dst = open(fn,'wb')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024)
            if not data:break
            dst.write(data)
        s.close()
    dst.close()

if __name__ == "__main__":
    count = len(sys.argv)
    if count == 3 :
        if sys.argv[1] == '-s':
            sendFile(sys.argv[2])
    else:
        recvFile('/home/arm/x.mp4')
