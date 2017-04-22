def read(fn,pos):
    with open(fn,'rb') as f:
        cols=4
        
        f.seek(pos)
#        a=int.from_bytes(f.read(2),byteorder='little')
#        print('%i,%i' % ( a-65536,a1))
#        print('%i' % a1)
        for i in range(128):
            v1=int.from_bytes(f.read(2),byteorder='little')
            if v1 > 65536/2 :
                v1 = v1-65536
#            v1=int.from_bytes(f.read(1),byteorder='big')*256+v1
            if i % cols ==0 :
                print('\n%i:\t %i' % (i/cols,v1),end="\t")
            else:
                print(v1,end="\t")
        print()

def readb(fn,pos):
    with open(fn,'rb') as f:
        f.seek(pos)
        for i in range(256):
            v=ord(f.read(1))
            if i % 6 == 0:
                print()
                print('%i\t%i' % (i,v),end="\t")
            else:
                print(v,end="\t")
        print()
def x(a,b):
    x=int(a+b)
    x=int(x/2)
    x=int(x+a)
    return int(x/2)

if __name__=="__main__" :
#    read("d:/lx/git/cpp/burn8051/x.bin",0xc00)
#    read("d:/lx/git/motor/atmel/x.bin",0)
    readb("/home/arm/git/motor/c/eeprom.bin",0)
