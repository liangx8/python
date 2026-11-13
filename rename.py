import os
import os.path
def rename(dname,prefix):
    with os.scandir(dname) as itr:
        seq = 0
        for ent in itr:
            if ent.is_file():
                picn=ent.name
                for suf in ('.jpg','.png'):
                    if picn.endswith(suf):
                        src=f'{dname}{picn}'
                        while True:
                            dst='{}{}{:04d}{}'.format(dname,prefix,seq,suf)
                            if os.path.exists(dst):
                                seq = seq + 1
                            else:
                                break
                        print(src,dst)
                        os.rename(src,dst)
                        seq = seq + 1
                    

if __name__=='__main__':
    rename('/home/cyc/wallpapers/','bg')
