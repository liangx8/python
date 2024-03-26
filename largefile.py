#!/bin/python
# search big file

import os
import time

def walk(root,fn,err):
    try:
        for de in os.scandir(root):
            if de.is_symlink():
                continue
            if de.is_dir():
                if walk(de.path,fn,err):
                    return True
            else:
                if fn(de.path):
                    return True
##    except PermissionError as e1:
        
    except OSError as e2:
        return err(e2)
   
    return False
class Stats:
    def __init__(self):
        self.__cnt=0
        self.__errcnt=0
    def fileCnt(self,ph):
        cnt=self.__cnt
        self.__cnt = cnt + 1
        return False
    def onError(self,err):
        self.__errcnt = self.__errcnt + 1
        return False
    def total(self):
        return (self.__cnt,self.__errcnt)
def fsize(ph):
    print(ph.name,ph.stat().st_size)
if __name__ == "__main__":

    st=Stats()
    walk("/home",st.fileCnt,st.onError)
    print("total:",st.total())
    



