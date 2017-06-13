def b(v):
    if v>255:
        return '{:016b}'.format(v)
    return '{:08b}'.format(v)
def x(v):
    return '0x{:02x}'.format(v)
def bx(v):
    return '{} {}'.format(b(v),x(v))

def show(buf,w=16):
    i=0
    for b in buf:
        print(x(b), end=" ")
        i = i+1
        if i % w == 0:
            print()


def current(n):
    adc2a=1024*.8/1.1
    f="""1毫安时= 3.6安秒
2安秒的ADC值{}/2 * {}次 = {}(安秒ADC)
1毫安时的ADC值 = 3.6安秒 * 安秒ADC = {}
"""
    print(f.format(adc2a,n,adc2a/2 * n,adc2a/2 * n * 3.6))


def regularCalc(v,base,r=None):
    if not r:
        r=(110,33,47,4.7,1,10)
    vout = 0
    cp = 999
    r1 =0
    r2 =0
    for rr1 in r:
        for rr2 in r:
            vout1 = base * (rr1/rr2 + 1)
            cp1 = vout1 - v
            if cp1 > 0:
                if cp1 < cp:
                    cp=cp1
                    vout=vout1
                    r1=rr1
                    r2=rr2
    return vout,r1,r2
            

