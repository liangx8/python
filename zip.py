#!/usr/bin/python
import zipfile
import argparse
import os

def list_content(zfile):
    for n in zfile.infolist():
        if not n.is_dir():
            print(n.filename)
def extract_content(zfile,dst=None):
    if dst == None:
        zfile.extractall()
    else:
        zfile.extractall(dst)
def walk_file(path,z):
    for root,dirs,files in os.walk(path):
        for f in files:
            z.write("{}/{}".format(root,f))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='zip utility')
    parser.add_argument("zfile",metavar="target | sources ...",
                        type=str,
                        nargs='+',
                        help="zip a package")
    parser.add_argument('-l',action='store_true',help="list content")
    parser.add_argument('-x',action="store_true",help="extract content to current directory")
    parser.add_argument('-c',action="store_true",help="create zip file")

    args = parser.parse_args()
    try:
        if args.l :
            with zipfile.ZipFile(args.zfile[0]) as zip:
                list_content(zip)
            exit()
        if args.x :
            with zipfile.ZipFile(args.zfile[0]) as zip:
                extract_content(zip)
            exit()
        if args.c :
            if len(args.zfile)==1:
                exit()
            with zipfile.ZipFile(args.zfile[0],"w") as zip:
                
                for sub in args.zfile[1:]:
                    if os.path.islink(sub): continue
                    if os.path.isfile(sub):
                        zip.write(sub)
                        continue
                    walk_file(sub,zip)
    except zipfile.BadZipfile as e:
        #print("Error: '{}' is not zip format".format(args.zfile))
        print(e)
    except OSError as e:
        print(e)
