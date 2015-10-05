import os
import re

def find(path,cp):

    for root,dirs,files in os.walk(path):
        for f in files:

            fullname=root+"/"+f
            if not filefilter(fullname):
                x=Search(fullname,cp)
                readbin(x)
def decode_byte(bs):
    try:
        return str(bs,'utf-8'),None
#    except UnicodeDecodeError as e:
    except:
        pass
    try:
        return str(bs,'latin_1'),None
    except Exception as e:
        return None,e

#f should be object Search
def readbin(f):
    inp = open(f.filename(),"rb")
    buf = inp.read()
    inp.close()
    l=bytearray()
    ln=0
    for n in buf:
        if n != ord('\n'):
            l.append(n)
        else:
            dc,e = decode_byte(l)
            if e:

                print("error at line: %d in file: %s" % (ln, f.filename()))
                print(e)

            else:
                f.proc(ln,dc)
            l=bytearray()
            ln = ln +1
def filefilter(path):
    m = re.search('\\.inc$|\\.asm$|\\.INC$|\\.h',path)
    if m:
        return False
    return True

class Search:
    def __init__(self,filename,cp):
        self.__show=False
        self.__fn=filename
        self.__cp=cp

    def proc(self,n,line):

        if self.__cp(line):
            if not self.__show:
                print(self.__fn)
                self.__show=True
            print ("%5d %s" % (n,line))
    def filename(self):
        return self.__fn
def comp(line):
    m=re.search("TL[01]|time_t",line)
    return m

if __name__=="__main__" :

    find("e:/motor/BLHeli-master",comp)
#    find("d:/p/mingw",comp)

