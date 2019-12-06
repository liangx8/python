#!/bin/python
import os
import re

class Bat(dict):
    def __init__(self):
        self['template']="""{{"version":1,
"color": "{0[color]}",
"full_text": "{0[icon]} {0[full_text]}"
}}"""
    def data(self):
        self["version"]=1
        with os.popen('acpi') as aa:
            for line in aa:
                self.work(line)
        self['color']='#f5af19'

        print(self['template'].format(self))

    def work(self,line):
        cp=re.compile('(\d+)%,')
        val=cp.search(line)
        if val :
            self['full_text']=" {}%".format(val.group(1))
            self['icon']='\U0001f50b'
            return
        cp=re.compile('Full')
        val=cp.search(line)
        if val:
            self['full_text']='100%'
            self['icon']='\U0001f50c'
            return

if __name__=='__main__':
    bat=Bat()
    bat.data()
