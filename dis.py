import codecs
import re


JMPS = { "brmi","rjmp","jmp","rcall","brne","brts","brcc","breq","brcs","brie","brpl","brtc" }
hexstr = "0123456789abcdef"
m48_reg = {
0x60:"WDTCSR",
0x61:"CLKPR",
0x64:"PRR",
0x66:"OSCCAL",
0x68:"PCICR",
0x69:"EICRA",
0x6b:"PCMSK0",
0x6c:"PCMSK1",
0x6d:"PCMSK2",
0x6e:"TIMSK0",
0x6f:"TIMSK1",
0x70:"TIMSK2",
0x78:"ADCL",
0x79:"ADCH",
0x7a:"ADCSRA",
0x7b:"ADCSRB",
0x7c:"ADMUX",
0x7e:"DIDR0",
0x7f:"DIDR1",
0x80:"TCCR1A",
0x81:"TCCR1B",
0x82:"TCCR1C",
0x84:"TCNT1L",
0x85:"TCNT1H",
0x86:"ICR1L",
0x87:"ICR1H",
0x88:"OCR1AL",
0x89:"OCR1AH",
0x8a:"OCR1BL",
0x8b:"OCR1BH",
0xb0:"TCCR2A",
0xb1:"TCCR2B",
0xb2:"TCNT2",
0xb3:"OCR2A",
0xb4:"OCR2B",
0xb6:"ASSR",
0xb8:"TWBR",
0xb9:"TWSR",
0xba:"TWAR",
0xbb:"TWDR",
0xbc:"TWCR",
0xbd:"TWAMR",
0xc0:"UCSR0A",
0xc1:"UCSR0B",
0xc2:"UCSR0C",
0xc4:"UBRR0L",
0xc5:"UBRR0H",
0xc6:"UDR0",
0x03:"PINB",
0x04:"DDRB",
0x05:"PORTB",
0x06:"PINC",
0x07:"DDRC",
0x08:"PORTC",
0x09:"PIND",
0x0a:"DDRD",
0x0b:"PORTD",
0x15:"TIFR0",
0x16:"TIFR1",
0x17:"TIFR2",
0x1b:"PCIFR",
0x1c:"EIFR",
0x1d:"EIMSK",
0x1e:"GPIOR0",
0x1f:"EECR",
0x20:"EEDR",
0x21:"EEARL",
0x22:"EEARH",
0x23:"GTCCR",
0x24:"TCCR0A",
0x25:"TCCR0B",
0x26:"TCNT0",
0x27:"OCR0A",
0x28:"OCR0B",
0x2a:"GPIOR1",
0x2b:"GPIOR2",
0x2c:"SPCR",
0x2d:"SPSR",
0x2e:"SPDR",
0x30:"ACSR",
0x31:"MONDR",
0x33:"SMCR",
0x34:"MCUSR",
0x35:"MCUCR",
0x37:"SPMCSR",
0x3f:"SREG",
0x3e:"SPH",
0x3d:"SPL"
}

m8_reg = {
"0x3f":"SREG", 
"0x3d":"SPL", 
"0x3e":"SPH", 
"0x3b":"GICR", 
"0x3a":"GIFR", 
"0x39":"TIMSK", 
"0x38":"TIFR", 
"0x37":"SPMCR", 
"0x36":"TWCR", 
"0x35":"MCUCR", 
"0x34":"MCUCSR", 
"0x33":"TCCR0", 
"0x32":"TCNT0", 
"0x31":"OSCCAL", 
"0x30":"SFIOR", 
"0x2f":"TCCR1A", 
"0x2e":"TCCR1B", 
"0x2c":"TCNT1L", 
"0x2d":"TCNT1H", 
"0x2a":"OCR1AL", 
"0x2b":"OCR1AH", 
"0x28":"OCR1BL", 
"0x29":"OCR1BH", 
"0x26":"ICR1L", 
"0x27":"ICR1H", 
"0x25":"TCCR2", 
"0x24":"TCNT2", 
"0x23":"OCR2", 
"0x22":"ASSR", 
"0x21":"WDTCR", 
"0x20":"UBRRH", 
"0x20":"UCSRC", 
"0x1e":"EEARL", 
"0x1f":"EEARH", 
"0x1d":"EEDR", 
"0x1c":"EECR", 
"0x18":"PORTB", 
"0x17":"DDRB", 
"0x16":"PINB", 
"0x15":"PORTC", 
"0x14":"DDRC", 
"0x13":"PINC", 
"0x12":"PORTD", 
"0x11":"DDRD", 
"0x10":"PIND", 
"0x0f":"SPDR", 
"0x0e":"SPSR", 
"0x0d":"SPCR", 
"0x0c":"UDR", 
"0x0b":"UCSRA", 
"0x0a":"UCSRB", 
"0x09":"UBRRL", 
"0x08":"ACSR", 
"0x07":"ADMUX", 
"0x06":"ADCSRA", 
"0x04":"ADCL", 
"0x05":"ADCH", 
"0x03":"TWDR", 
"0x02":"TWAR", 
"0x01":"TWSR", 
"0x00":"TWBR"
}


ioopcode1 = ("out","cbi","sbi","sbic","sbis","sts")
ioopcode2 = ("in","lds")
def reladdr(addr,s):
    new_addr=addr+int(s[1:])+2
    while new_addr < 0:
        new_addr=new_addr + 8192
    while new_addr >8191:
        new_addr = new_addr-8192
        
    return new_addr
#    return str.format("X%04x" % new_addr)
def parse1(s):
    m = re.search('^ ',s)
    r = list()
    lbl=None

    if m :
        l = re.split('\\t',s)
        cur_addr=addr(l[0])
        r.append(cur_addr)
        r.append(l[2])
        if l[2] in JMPS:
            v_addr=reladdr(cur_addr,l[3])
            r.append(str.format("X%04x" % v_addr))
            lbl=v_addr
        else:
            if len(l)>3:
                r.append(l[3])
            else:
                r.append('\t')
        if l[2] in ['cbi','out','sbi']:
            r[2]=first_opcode(r[2])
        if l[2] == 'in':
            r[2]=second_opcode(r[2])
            
        r.append("; %s %s" % (l[0],l[1]))
        if len(l)>4:
            r.append(l[4])
        return lbl,r
    return None,None
def second_opcode(s):
    l=re.split(', ',s)
    return "%s,%s" % (l[0],m8_reg[l[1]])
def first_opcode(s):
    l=re.split(',',s)
    return "%s,%s" % (m8_reg[l[0]],l[1])
def addr(s):
    index=len(s)-2
    m=1
    su=0
    while True :
        if s[index]== ' ':
            break
        i=0
        while i <16:
            if hexstr[i]==s[index]:
                break
            i=i+1
        if i>0 :
            su=su+i*m
        index=index-1
        m=m*16
    return su

def disa():
    ll=list()
    l_addr=list()
    with codecs.open("e:/tgy/super.lst","r","utf-8") as f:
        for line in f:
            lbl_adr,r=parse1(line[0:len(line)-2])
            if r :
                ll.append(r)
            if lbl_adr != None:
                l_addr.append(lbl_adr)
    target = open("e:/tgy/super.asm","w")
    print(';avr-objdump -m avr -D <filename>',file=target)
    print('.include "m8def.inc"\n.cseg\n.org 0',file=target)
    for l in ll:
        if l[0] in l_addr:
            print("X%04x:" % l[0],file=target)
        print("\t%s\t%s %s" % (l[1],l[2],l[3]),end=' ',file=target)
        if len(l)>4:
            print(l[4],file=target)
        else:
            print(file=target)
    print(".exit",file=target)
    target.close()

def parse_opcode(s):
    for opcode in ioopcode1:
        idx=s.find(opcode+"\t")
        if idx >=0 :
            op=s[idx:]
            pstart=op.find("0")
            pend=op.find(",")
            k=int(op[pstart:pend],16)
            if k < 0x100:
                return "{} {}{}".format(s[:idx+pstart],m48_reg[k],s[idx+pend:len(s)-1])
    #for opcode in ioopcode2:
    #    idx=s.find(opcode+"\t")
    #    if idx >=0 :
    #        print(s[idx:],end="")
    #        return
    return s[:len(s)-1]
        
def ioname():
    """atmel相关"""
    target = open("/home/arm/git/motor/c/hall.ast","w")
    with codecs.open("/home/arm/git/motor/c/hall.lss","r","utf-8") as f:
        for line in f:
            print(parse_opcode(line),file=target)
    target.close
def register():
    """把寄存器的格式变成PYHON格式
cat /usr/avr/include/avr/iomx8.h | grep "IO8" > <target file>
cat /usr/avr/include/avr/iomx8.h | grep "MEM8" >> <target file>
"""
    with codecs.open("/home/arm/m48.h","r","utf-8") as f:
        for line in f:
            st = line.strip()
            al = st.split(" ")
            length=len(st)
            print("\"{}\":\"{}\",".format(st[length-5:length-1],al[1]))
def info(line):
    """info of return: ITNAME,ITNUM,COMMENT"""
    cp=re.compile(r"(\w+) += +(-?\d+),? +(/\*.*\*/)")
    r=cp.match(line)
    g=r.groups()
    return g[0],g[1],g[2]
def handler(s):
    cnt=len(s)
    return s[:cnt-4]+"Handler"
def stm_vtable(xx):
    """STM32中断向量表"""
    ss=list()
    with open(xx,'r') as f:
        for line in f:
            sline=line.strip()
            cnt=len(sline)
            if cnt and not sline.startswith('/*'):
                s=info(sline)
                ss.append((s[0],int(s[1]),s[2]))
    def cmp(x):
        return x[1]
    maxv=max(ss,key=cmp)
    minv=min(ss,key=cmp)

    base=0x8000000-4
    ss.sort(key=cmp)
    idx=0
    rr=list()
    vmin=minv[1]-2
    for num in range (vmin,maxv[1]+1):
        base = base + 4
        if num == vmin:
            rr.append(("_estack",num,"/*!< {} 0x{:08x} Top of stack*/".format(num,base)))
            continue
        if num == vmin+1:
            rr.append(("Reset_Handler",num,"/*!< {} 0x{:08x} Reset Interrupt*/".format(num,base)))
            continue
        
        if num == ss[idx][1]:
            cmt=ss[idx][2][:4]+" {} 0x{:08x}"+ss[idx][2][4:]
            rr.append((handler(ss[idx][0]),num,cmt.format(num,base)))
            idx = idx + 1
        else:
            rr.append(("0",num,"/*!< {} 0x{:08x} Reserved*/".format(num,base)))
        
    for s in rr:
        print(".long\t{}\t\t{}".format(s[0],s[2]))

    for s in rr:
        if  s[0] != '0':
            print(".weak {}\n.thumb_set {}, Default_Handler".format(s[0],s[0]))
        
                
if __name__=="__main__" :
    #ioname()
    stm_vtable('stm32f10xxx.txt')

