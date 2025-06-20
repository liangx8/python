#!/usr/bin/python
import zipfile
import argparse
import os
import sys

def list_content(zfile):
    for n in zfile.infolist():
        if not n.is_dir():
            print(n.filename)
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
    parser.add_argument('-p',nargs=1,help="password")

    args = parser.parse_args()
    try:
        pwd = None
        if args.p:
            pwd=args.p[0]
        if args.l :
            with zipfile.ZipFile(args.zfile[0]) as zp:
                list_content(zp)
            exit()
        if args.x :
            with zipfile.ZipFile(args.zfile[0]) as zp:
                #extract_content(zip,None,pwd.encode())
                if pwd != None:
                    zp.extractall(pwd=pwd.encode())
                else:
                    zp.extractall()
            exit()
        if args.c :
            if len(args.zfile)==1:
                exit()
            with zipfile.ZipFile(args.zfile[0],"w") as zp:
                
                for sub in args.zfile[1:]:
                    if os.path.islink(sub): continue
                    if os.path.isfile(sub):
                        zp.write(sub)
                        continue
                    walk_file(sub,zp)
    except zipfile.BadZipfile as e:
        #print("Error: '{}' is not zip format".format(args.zfile))
        print(e)
    except OSError as e:
        print(e)
