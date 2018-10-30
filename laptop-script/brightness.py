#!/bin/python

brightness_path='/sys/class/backlight/{}/brightness'

def read_value(kernel_name):
    cur=0
    try:
        with open(brightness_path.format(kernel_name)) as br:
            li=br.readline()
            cur = int(li[:len(li)-1])
            return cur
    except :
        return -1
def write_value(kernel_name,val):
    try:
        with open(brightness_path.format(kernel_name),"w+") as br:
            print(val,end='',file=br)
        return val
    except Exception as e:
        print(e)
        return -1
