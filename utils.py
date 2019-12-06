
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
if __name__ == "__main__":
    gbk("中文")
