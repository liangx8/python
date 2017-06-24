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
def hexdump(file,width=16):
    f= open(file,'rb')
    buf=f.read()
    f.close()
    idx=0
    print('0000',end=' ')
    for b in buf:
        print('{:02x}'.format(b),end=' ')
        idx = idx +1
        if idx % width == 0:
            print()
            print('{:04x}'.format(idx),end=' ')
        

def x(a,b):
    x=int(a+b)
    x=int(x/2)
    x=int(x+a)
    return int(x/2)
core_table=(
    'Reset','NMI','HardFault','MemManage','BusFault','UsageFault',
    None,None,None,None,
    'SVCall','DebugMonitor',None,'PendSV','SystTick'
    )
def vector_table(xx):
    with open(xx,'r') as f:
        
        li=list()
        for l in f:
            c=len(l)
            
            if l[c-1] == '\n':
                l=l[:c-1]
            li.append(l)
        start=0x4
        for x in core_table:
            if x==None:
                print(".long\t0\t\t/* 0x0800 {:04x} Reserved*/".format(start))
            else:
                print(".long\t{}_handler\t\t/* 0x0800 {:04x} */".format(x,start))
            start = start + 4
        idx =0
        for x in li:
            if x[0]=='0':
                print(".long\t0\t\t/* {:2d} 0x0800 {:04x} Reserved*/".format(idx,start))
            else:
                print(".long\t{}_handler\t\t/* {:2d} 0x0800 {:04x} */".format(x,idx,start))
            start = start + 4
            idx = idx +1
        tmpl=".weak {}_handler\n.thumb_set {}_handler,Default_handler"
        for x in core_table:
            if x :
                print(tmpl.format(x,x))
        for x in li:
            if x[0]!='0':
                print(tmpl.format(x,x))

if __name__=='__main__':
    vector_table('/home/arm/git/python/stm32f10xxx.txt')

#    read("d:/lx/git/cpp/burn8051/x.bin",0xc00)
#    read("/home/arm/Downloads/x.bin",0)
#    readb("/home/arm/git/motor/c/eeprom.bin",0)
