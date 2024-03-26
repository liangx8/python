import sys
import os
import os.path


def dirs(d,fn):
    with os.scandir(d) as entries:
        for entry in entries:
            if entry.is_dir():
                dirs(entry.path,fn)
                return
            if fn(entry):
                return
                
        
def choose(ary):
    print(ary.path)


if __name__=="__main__":

    def ten(o):
        choose(o)
        return False
    if len(sys.argv)>1:
        dirs(sys.argv[1],ten)
    else:
        dirs("/home/tec/Downloads",ten)
