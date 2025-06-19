import pathlib

def ren():
    path=pathlib.Path("/home/cyc/Downloads/4Kcom")
    cnt=0
    for pp in path.iterdir():
        #pp.rename("{:04}.jpg".format(cnt))
        dst=pp.parent.joinpath("comm_{:04}.jpg".format(cnt))
        cnt = cnt + 1
        pp.rename(dst)
if __name__=="__main__":
    ren()
