import os
import re
def renames(root,dstname):
    seq = 0;
    os.chdir(root)
    for pp in os.listdir():
        dst=dstname(seq,pp)
        seq = seq + 1
        os.rename(pp,dst)
def pn(seq,pa):
    alpha=re.compile("^(\d*)(.+)$")
    cp=alpha.match(pa)
    return "{:03}{}".format(seq,cp.groups()[1])
    
##    print("{:03}-{}".format(seq,pa.name))
if __name__=="__main__":
    root="/home/tec/Downloads/Telegram Desktop"
##    pt = re.compile("母|妈")

    renames(root,pn)
