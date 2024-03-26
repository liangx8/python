import sys
import datetime
tmformat="%H:%M:%S.%f"
def totime(sr,sec):
    tm=datetime.datetime.strptime(sr,tmformat)
    
    return (tm+sec).strftime(tmformat)[1:11]
    
def st(dst,src,sec):
    delta=datetime.timedelta(seconds=sec)
    buf=list()
    with open(src,encoding="utf-8") as f:
        for xx in f:
            if xx[:9]=="Dialogue:":
                yy = xx.split(",")
                yy[1]=totime(yy[1],delta)
                yy[2]=totime(yy[2],delta)
                s=","
                r=s.join(yy)
                buf.append(r)
            else:
                buf.append(xx)
    with open(dst,"w+",encoding="utf-8") as wt:
        for x in buf:
            print(x,end="",file=wt)
        print("done")
def short(idx,sec):
    pre="/home/com/video/rwby/session02/S2/"
    dst="{}s2ep{:02}.ass".format(pre,idx)
    src="{}RWBY S2 EP{:02}.ass".format(pre,idx)
    st(dst,src,sec)
    print("`{}` is OK".format(dst))
if __name__=="__main__":
    cnt=len(sys.argv)
    if(cnt>3):
        st(sys.argv[2],sys.argv[1],int(sys.argv[3]))
    else :
        print("{} src dst sec".format(sys.argv[0]))
 
