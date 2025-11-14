def pp(buf):
    '''
input sampe as below: 
::CR1
PECEN ALERTEN SMBDEN SMBHEN GCEN WUPEN NOSTRETCH SBC RXDMAEN TXDMAEN Res. ANFOFF DNF,4 ERRIE TCIE STOPIE NACKIE ADDRIE RXIE TXIE PE
::CR2
PECBYTE AUTOEND RELOAD NBYTES,8 NACK STOP START HEAD10R ADD10 RD_WRN SADD,10
::OAR1
OA1EN Res. Res. Res. Res. OA1MODE OA1,10
::OAR2
OA2EN Res. Res. Res. Res. OA2MSK,3 OA2,7 Res.
::TIMIMGR
PRESC,4 Res. Res. Res. Res. SCLDEL,4 SDADEL,4 SCLH,8 SCLL,8
::TIMEOUTR
TEXTEN Res. Res. Res. TIMEOUTB,12 TIMOUTEN Res. Res. TIDLE TIMEOUTA,12
::ISR
ADDCODE,7 DIR BUSY Res. ALERT TIMEOUT PECERR OVR ARLO BERR TCR TC STOPF NACKF ADDR RXNE TXIS TXE
::ICR
ALERTCF TIMOUTCF PECCF OVRCF ARLOCF BERRCF Res. Res. STOPCF NACKCF ADDRCF Res. Res. Res

'''
    pname=None
    rname=None
    for line in buf:
        if line.startswith('::'):
            rname=line[2:-1]
            print()
            continue
        if line.startswith(':'):
            pname=line[1:-1]
            continue
        if len(line.strip())==0:
            continue
        fnames=line[:-1].split(' ')
        fnames.reverse()
        pos=0
        ba=bytearray()
        for fname in fnames:
            if fname=="Res.":
                pos = pos +1
                continue
            if fname.find(',')==-1:
                inc=1
                fna=fname
            else:
                fna,sz=fname.split(',')
                inc=int(sz)
            ba.clear()
            sz=25-len(fna)-len(rname)
            for _ in range(sz):
                ba.append(32)
            print("#define {}_{}_{}_pos{}{}".format(pname,rname,fna,ba.decode(),pos))
            pos = pos+inc
def src(fname):
    import os
    home=os.environ['HOME']
    strs=list()
    with open("{}/{}".format(home,fname)) as infile:
        for line in infile:
            strs.append(line)
        return strs
    return None
if __name__=='__main__':
    buf=src('arm32.txt')
    if buf:
        pp(buf)
        print("OK")
    else:
        print("error")
