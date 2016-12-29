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
