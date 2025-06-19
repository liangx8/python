import subprocess
import io

class Cache:
    def __init__(self):
        rs = subprocess.run(["pacman","-Qil"],stdout=subprocess.PIPE)
        self.__bs = bytes(rs.stdout)
    def eachline(self,fn):
        lno=0
        for li in io.BytesIO(self.__bs):
            fn(lno,li)
            lno = lno + 1
def line(nu,s):
    print(nu,s)
if __name__ == "__main__":
    ch=Cache()
    ch.eachline(line)
