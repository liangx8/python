import socket
import logging
import sys
import os
CHAR_ENDIAN='little'

def readi32(reader):
    bs = reader.recv(4)
    if len(bs) < 4:
        logging.error("expect 4 bytes but %d", len(bs))
        os.exit(-1)
    return int.from_bytes(bs,CHAR_ENDIAN)
    
def readStr(reader):
    bs = reader.recv(2)
    if len(bs) < 2:
        logging.error("unknown incoming message %d", len(bs))
        os.exit(-1)
    fncnt=int.from_bytes(bs,CHAR_ENDIAN)
    return reader.recv(fncnt).decode('utf-8')

def transfer(pipeio):
    """ 文件传输服务
command:
  1 ls
  2 upload
  3 download
  4 remove
字符串定义
   0 ~ 1 字符串长度(utf8编码)
   2 ~ n 字符串内容，根据第0~1字节决定
数值定义
   4 bytes

发送命令格式:
  position 0: 命令
  position 1: 命令的参数(字符串)，零长度的字符串意味无参数
  position n: 只有upload命令需要这字段
返回结果
  成功
    position 0: 0
    position 1: rm, upload 无内容
                ls, 返回指定的目录"列文件实体格式"
                download 指定文件的内容	
  失败
    position 0: 1
    position 1: 失败原因(字符串)
文件实体格式
  position 0: uint32  size of file, 如果是目录则为0
  position 4: 文件名

列文件实体格式
  position 0: uint16 目录总数
  position 1~n:文件实体

"""
    try:
        bs=pipeio.recv(2)
        if len(bs) < 2:
            logging.error("unknown incoming message %d", len(bs))
            return False
        fncnt=int.from_bytes(bs,CHAR_ENDIAN)
        fn=pipeio.recv(fncnt).decode('utf-8')
        logging.info("message in %d bytes: %s",fncnt,fn)
        if fn=='quit':
            return True
        return False
    except Exception as e:
        logging.error(e)
        return True

def sendStr(io,s):
    if s:
        buf=s.encode('utf-8')
        bufsize=len(buf)
        io.send(bufsize.to_bytes(2,CHAR_ENDIAN))
        sock.send(buf)
    else:
        io.send(b"\0\0")
    
SOCKFILE='/tmp/copy.sock'
def returnDir(io):
    stat=io.recv(1)
    if stat[0] == 0:
        stat=io.recv(2)
        cnt=int.from_bytes(stat,CHAR_ENDIAN)
        print("total: {}".format(cnt))
        for idx in range(cnt):
            size=readi32(io)
            name=readStr(io)
            print("{:8d} {}".format(size,name))
    else:
        print("server say:",readStr(io))
# ls = 1
# upload = 2
# download = 3
# rm = 4
# quit = 5
if __name__== '__main__' :
    argc=len(sys.argv)
    if argc > 1:
        sock= socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
        sock.connect(SOCKFILE)
        if sys.argv[1] == 'ls':
            sock.send(b'\1')
            if argc > 2:
                sendStr(sock,sys.argv[2])
            else:
                sendStr(sock,None)
            returnDir(sock)
        elif sys.argv[1] == 'upload':
            pass
        elif sys.argv[1] == 'download':
            print("downloading {}".format(argc))
            if argc > 2:
                sock.send(b'\3')
                sendStr(sock,sys.argv[2])
            else:
                raise Exception('expected target of download')
            
        elif sys.argv[1] == 'quit':
            sock.send(b'\5')
        while True:
            data=sock.recv(4096)
            if not data :break
            print(data.decode('utf8'),end="")
        sock.close()
    else:
        logging.basicConfig(filename='copy.log',format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)
        sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
        try:
            sock.bind(SOCKFILE)
        except OSError as e:
            os.remove(SOCKFILE)
            sock.bind(SOCKFILE)
        sock.listen(1)
        while True:
            conn,addr = sock.accept()
            logging.info("connection from %s",addr)
            with conn:
                if transfer(conn):
                    break
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
          
                        
            
