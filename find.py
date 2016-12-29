import os
import re
import types

class ContentFind:
    def __init__(self,root,fmatch):
        self.__root=root
        self.__fmatch=fmatch

    def find(self,cp):
        for root,dirs,files in os.walk(self.__root):
            for f in files:
                fullname=fullname="{}/{}".format(root,f)
                if type(self.__fmatch)==types.FunctionType:
                    if self.__fmatch(fullname):

                        self.readbin(fullname,cp)
    def readbin(self,fullname,cp):
        inp = open(fullname,"rb")
        buf=inp.read()
        inp.close()
        showf=True
        l=bytearray()
        pattern=None
        if type(cp)==str:
            pattern=re.compile(cp)
        ln=0
        for n in buf:
            if n!=ord('\n'):
                l.append(n)
            else:
                ln=ln+1
                dc,e = decode_byte(l)
                if e:
                    print("error at line: %d in file: %s" % (ln,fullname))
                    print(e)
                else:
                    result=False
                    if pattern:

                        if pattern.search(dc):result=True
                    else:
                        if type(cp)==types.FunctionType:
                            if cp(dc): result=True

                        
                    if result:
                        if showf:
                            print(fullname)
                            showf=False
                        print("%5d %s" % (ln,dc))
                l.clear()
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

def comp(line):
    m=re.search("RSTSRC",line)
    return m
if __name__=="__main__" :
    
    ff=re.compile("lua$")
    def asmfilter(path):
        return ff.search(path)
    cf=ContentFind("/home/arm/factorio/data/base",asmfilter)
# cf.find("Flags0\\.PWM_ON")
    
    cf.find("steel-plate")

