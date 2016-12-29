#!/usr/bin/python
import zipfile
import argparse
import os

def list_content(zfile):
    for n in zfile.namelist():
        print(n)
def extract_content(zfile,dst=None):
    if dst == None:
        zfile.extractall()
    else:
        zfile.extractall(dst)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='zip utility')
    parser.add_argument("zfile",metavar="<zip file>",
                        type=str,
                        help="target zip file")
    parser.add_argument('-l',action='store_true',help="list content")
    parser.add_argument('-x',action="store_true",help="extract content to current directory")
    args = parser.parse_args()
    try:
        if args.l :
            with zipfile.ZipFile(args.zfile) as zip:
                list_content(zip)
            exit()
        if args.x :
            with zipfile.ZipFile(args.zfile) as zip:
                extract_content(zip)
            exit()
            
    except zipfile.BadZipfile as e:
        #print("Error: '{}' is not zip format".format(args.zfile))
        print(e)
    except OSError as e:
        print(e)
