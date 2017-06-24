import os
import os.path
import sys

S_IFSOCK   =0o140000   #socket
S_IFLNK    =0o120000   #symbolic link
S_IFREG    =0o100000   #regular file
S_IFBLK    =0o060000   #block device
S_IFDIR    =0o040000   #directory
S_IFCHR    =0o020000   #character device
S_IFIFO    =0o010000   #FIFO

S_IFMT     =0o170000


def utf8str(w,strs):
    buf = strs.encode("utf-8")
    w.write(len(buf).to_bytes(2,"little"))
    w.write(buf)
def intWrite(w,size,v):
    w.write(v.to_bytes(size,"little"))
def deepwalk(prefix,wrt,file=""):
    """
串格式：
  ddcc...
  | `-- 字符串长度由dd指定
  `---- 长度2 字节
类型：
d - 一字节，1 目录，2 link, 3 普通文件， 4 其他
时间戳：
dddddddd - 8 字节,日期，

对象数组，如果不是类型1，没有这个字段
dd - 2字节，后面的对象的数量,
长度：
dddddddd - 8 字节,文件的长度
对象格式：
目录名(串):类型:时间戳:[对象数组|长度]
"""
    fullname=os.path.join(prefix,file)
    st=os.stat(fullname,follow_symlinks=False)
    if file=="":
        utf8str(wrt,prefix)
    else:
        utf8str(wrt,file)
    if (st.st_mode & S_IFMT) == S_IFDIR:
        wrt.write(b'\x01') #dir type
        intWrite(wrt,8,int(st.st_mtime))
        sub = os.listdir(fullname)
        intWrite(wrt,2,len(sub)) # sub dir num
        for x in sub:
            deepwalk(fullname,wrt,x)
        return
    btype=b'\x04'
    if (st.st_mode & S_IFMT) == S_IFREG:
        btype=b'\x03'
        
    if (st.st_mode & S_IFMT) == S_IFLNK:
        btype=b'\x02'
    wrt.write(btype) #link type
    intWrite(wrt,8,int(st.st_mtime))
    intWrite(wrt,8,st.st_size)

def binshow(p):
    
    f= open(p,'rb')
    bs=f.read()
    f.close()
    x=0
    for b in bs:
        print("{:02x} ".format(b),end='')
        x = x +1
        if x % 16 ==0: print()
            
            
        
if __name__ == "__main__":
    with open("/home/arm/fifo.bin","wb") as f:
        
        #s="/home/arm/租赁合同"
        s='/home/arm/Downloads'
        deepwalk(s,f)
