import codecs
import re


JMPS = { "brmi","rjmp","jmp","rcall","brne","brts","brcc","breq","brcs","brie","brpl","brtc" }
hexstr = "0123456789abcdef"
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
    
if __name__=="__main__" :
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


