import os
import os.path
import sys
import pathlib

def list_pic(pn):
    seq =0
    for root,dirs,files in  os.walk(pn):
        print("root:",root)
        #print(seq,dirs,files)
        if(len(files)>0):
            for f in files:
                print("     ",os.path.join(root,f))
        seq = seq+1
        

if __name__=="__main__":
    
    if len(sys.argv)>1:
        dirname=sys.argv[1]
    else:
        dirname=os.getcwd()
    pn=pathlib.Path(dirname)
    if pn.exists():
        list_pic(pn)
    else:
        print(f"'{pn}' is not exists")

