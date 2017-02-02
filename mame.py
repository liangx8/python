import os
import sys


if __name__ == "__main__":
    path="/home/arm/.mame/roms"
    for root,dirs,roms in os.walk("/home/arm/.mame/roms"):
        total=len(roms)
        cur = 0
        for rom in roms:
            cur = cur + 1
            print("==[[{} ({}/{})]]==".format(rom,cur,total))
            cmd="sdlmame {}".format(rom)
            os.system(cmd)
            fullpath="{}/{}".format(path,rom)
            print("删除文件{}吗？".format(fullpath))
            
            while(True):
                y=sys.stdin.readline()
                if y=='y\n':
                    print("删除文件{}".format(fullpath))
                    os.system("rm {}".format(fullpath))
                    break
                if y=='q\n':
                    quit()
                if y== '\n':
                    os.system("cp {} ~/roms/{}".format(fullpath,rom))
                    os.system("rm {}".format(fullpath))
                    break
                print("不懂")
