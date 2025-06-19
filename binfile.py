
import os
class binfile:
    def __init__(self,fn):
        self.__fn=fn
    def act(self):
        return open(self.__fn,"rb")
    def work(self):
        fh=open(self.__fn,"rb")
        fh.seek(1175607509,os.SEEK_SET)
        buf=fh.read(145+16)
        fh.close()
        return buf
def hexx(buf):
    cnt=0
    lleft=""
    lrigh=""
    for x in buf:
        if cnt == 16:
            cnt=0
            print(lleft,lrigh)
            lleft=""
            lrigh=""
            
        lleft=lleft + "{:02x} ".format(x)
        if x >= 0x20 and x < 127:
            lrigh = lrigh + chr(x)
        else:
            lrigh = lrigh + '.'
        cnt = cnt + 1
    print(lleft,lrigh)
if __name__=="__main__":
    bf=binfile('/home/com/big-data/chinaid/nameid.bin')
    xb=bf.work()
    hexx(xb)
