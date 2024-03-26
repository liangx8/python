
def uint8(cs):
    print("// `{}' size: {} ".format(cs,len(cs)))
    print("const uint8_t holder[]",end="={")
    for c in cs:
        print("0x{:02x}".format(ord(c)),end=",")
    print("}")
def gbk(cs):
    buf=cs.encode("gbk")
    print("// `{}' size: {}".format(cs,len(buf)))
    print("const uint8_t holder[]", end="={")
    for b in buf:
        print("0x{:02x}".format(b),end=",")
    print("}")
def vtable8051(data):
    template=".org 0x{:02x}\nsjmp infinity ;{}"
    print(".org 0\nljmp reset")
    for num in range(len(data)):
        print(template.format(num*8+3,data[num]))
        
if __name__ == "__main__":
    #gbk("中文")
    tba = []
    with open('/home/tec/git/esc8051/c8051f330.vtb','r') as tb:
        
        for ll in tb.readlines():
            l=ll[:-1]
            tba.append(l)
    vtable8051(tba)
    
