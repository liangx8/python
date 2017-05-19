class FileObject:
    """fields:
    path:(2:size,...)
    type:(1:1=dir 2=link 3=regular 4=)
    size:(4:int)
    modified:(8:time)
"""
    def dump(self,output):
        buf=self.path.encode("UTF-8")
        length=len(buf)
        output.write(length.to_bytes(2,"big"))
        output.write(buf)
        output.write(self.type.to_bytes(1,"big"))
        output.write(self.size.to_bytes(4,"big"))


def strdump(v,output):
    buf=v.encode("utf-8")
    length=len(buf)
    output.write(length.to_bytes(2,"big"))
    output.write(buf)
def typedump(v,output):
    output.write(v.to_bytes(1,"big"))
import os
import os.path
def dirdump(prefix,output):
    strdump(prefix,output)
    if os.path.isfile(prefix):    
        typedump(3,output)
    if os.path.islink(prefix):
        typedump(2,output)
