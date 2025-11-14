class IntegerIterator:
    def __init__(self,v):
        def gen():
            for x in v:
            	yield x
        self.__gen=gen()
    def __next__(self):
        return next(self.__gen)
class IntegerArray:
    def __init__(self):
        self.__values = list()
    def add(self,i):
        self.__values.append(i)
    def __iter__(self):
        return IntegerIterator(self.__values)

def lesson1():
    ia = IntegerArray()
    ia.add(1)
    ia.add("b")
    ia.add(True)
    ia.add(100)
    for i in ia:
        print(i)
        

def full(root):
    import os
    import os.path
    whole=os.listdir(root)
    for one in whole:
        strType="file"
        fpath=os.path.join(root,one)
        if os.path.isdir(fpath):
            strType="dir"
        print(strType,one)

def lesson2(root):
    full(root)
def lesson3():
    import math
    for x in range(180):
        if (x % 3) ==2:
            endc=',\n'
        else:
            endc=','
        print("SINE_DUTY(%.4ff)" % (math.sin(math.pi*x/180)),end=endc)
def lesson4():
    ar=("GIF","TCIF","HTIF","TEIF")
    bs=bytearray()
    for ch in range(7):
        for p in range(len(ar)):
            bs.clear()
            pp=ar[p]
            sz=len(pp)
            com=10-sz
            for _ in range(com):
                bs.append(32)
            print("#define DMA_IFCR_C{}{}_pos{}{}".format(pp,ch+1,bs.decode(),ch*4+p))
#            print("#define DMA_ISR_{}{}_pos{}{}".format(pp,ch+1,bs.decode(),ch*4+p))

if __name__ == "__main__":
    lesson2("/home/cyc")
