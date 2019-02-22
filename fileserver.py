import socket
import logging
import sys
import os.path
CHAR_ENDIAN='little'

def transfer(pipeio):
    """ 文件传输服务
0 ~ 1 文件名长度(utf8编码)
2 ~ n 文件名，根据第0~1字节决定"""
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
SOCKFILE='/tmp/copy.sock'
if __name__== '__main__' :
    if len(sys.argv) > 1:
        sock= socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
        sock.connect(SOCKFILE)
        buf=sys.argv[1].encode('utf-8')
        bufsize=len(buf)
        sock.send(bufsize.to_bytes(2,CHAR_ENDIAN))
        sock.send(buf)
        sock.close()
    else:
        logging.basicConfig(filename='copy.log',format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)
        if os.path.exists(SOCKFILE):
            os.remove(SOCKFILE)
        sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
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
          
                        
            
