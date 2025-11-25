import io
f421_crm='''
:CRM
::APB2RST
TMR17RST TMR16RST TMR15RST REV. USART1RST REV. SPI1RST TMR1RST REV. ADCRST REV.,7 EXINTRST SCFGCMPRST
::APB1RST
PWCRST REV.,5 I2C2RST I2C1RST REV.,3 USART2RST REV.,2 SPI2RST REV.,2 WWDTRST REV.,2 TMR14RST REV.,3 TMR6RST REV.,2 TMR3RST REV.
::AHBEN
GPIOFEN REV.,2 GPIOCEN GPIOBEN GPIOAEN REV.,10 CRCEN REV. FLASHEN REV. SRAMEN REV. DAM1EN
::APB2EN
TMR17EN TMR16EN TMR15EN REV. USART1EN REV. SPI1EN TMR1EN REV. ADC1EN REV.,8 SCFGCMPEN
::APB1EN
PWCEN REV.,5 I2C2EN I2C1EN REV.,3 USART2EN REV.,2 SPI2EN REV.,2 WWDTEN REV.,2 TMR14EN REV.,3 TMR6EN REV.,2 TMR3EN REV.
'''

def fmt(buf):
    pname=None
    rname=None
    rsize=0
    spbuf=bytearray()
    endout=io.StringIO()
    for li in buf.splitlines():
        if len(li)>0:
            if ord(li[-1])==10:
                li=li[:-1]
            if li.startswith('::'):
                rname=li[2:]
                rsize=len(rname)
                print()
                endout.seek(0)
                endout.truncate()
                print("#define {}_{}_VALUE (".format(pname,rname),file=endout,end='')
                continue
            if li[0]==':':
                pname=li[1:]
                continue
            fields=li.split(' ')
            fields.reverse()
            pos=0
            for field in fields:
                spbuf.clear()
                fname=None
                fwide=1
                if field.find(',')<0:
                    fname=field
                else:
                    fs=field.split(',')
                    fwide=int(fs[1])
                    fname=fs[0]
                cur_pos=pos
                pos = pos + fwide
                if fname=="REV.":
                    continue
                fsize=len(fname)
                cnt=25-rsize
                for x in range(cnt):
                    spbuf.append(32)
                if cur_pos<10:
                    spbuf.append(32)
                print("#ifdef CLK_{}\n#ifndef _VALUABLE\n#define _VALUABLE 1\n#endif".format(fname))
                print("#define {}_{}_{}{}(1<<{})".format(pname,rname,cur_pos,spbuf.decode(),cur_pos))
                print("#else\n#define {}_{}_{}{}0".format(pname,rname,cur_pos,spbuf.decode()))
                print("#endif")
                print(" {}_{}_{}".format(pname,rname,cur_pos),file=endout,end=' |\\\n')
#                print("#define {}_{}_{}_pos{}{}".format(pname,rname,fname,spbuf.decode(),cur_pos))
            print("#ifdef _VALUABLE")
            endout.seek(endout.tell()-4)
            endout.truncate()
            endout.write(')')
            print(endout.getvalue())
            print("#undef _VALUABLE\n#endif")
if __name__=='__main__':
    fmt(f421_crm)
