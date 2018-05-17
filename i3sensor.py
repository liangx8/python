#!/usr/bin/python
import os
import os.path
import re

def item_idx(idx_max):
    idx_name="/run/user/{}/senses_item.idx".format(os.getuid())
    idx = 0
    try:
        with open(idx_name,"rb") as hidx:
            idx=int.from_bytes(hidx.read(2),'little')+1
            if idx >= idx_max:
                idx=0
    except FileNotFoundError:
        pass
    except:
        return 0

    try:
        with open(idx_name,'wb') as hidx:
            hidx.write(idx.to_bytes(2,'little'))
    except:
        return 0
    return idx
        
            
    
def sensorData():
    vcore=re.compile("Vcore Voltage: +(\\+.+?) (V)")
    pt_33=re.compile(" \\+3\\.3 Voltage: +(\\+.+?) (V)")
    pt_50=re.compile(" \\+5 Voltage: +(\\+.+?) (V)")
    pt_120=re.compile(" \\+12 Voltage: +(\\+.+?) (V)")
    cpu_fan=re.compile("CPU FAN Speed: +([0-9]+) (RPM)")
    ch_1_fan=re.compile("CHASSIS1 FAN Speed: +([0-9]+) (RPM)")
    ch_2_fan=re.compile("CHASSIS2 FAN Speed: +([0-9]+) (RPM)")
    ch_3_fan=re.compile("CHASSIS3 FAN Speed: +([0-9]+) (RPM)")
    pwr_fan=re.compile("POWER FAN Speed: +([0-9]+) (RPM)")
    cpu_temp=re.compile("CPU Temperature: +(\\+.+?)(°[C|F])")
    mb_temp=re.compile("MB Temperature: +(\\+.+?)(°[C|F])")
    core_0_temp=re.compile("Core 0: +(\\+.+?)(°[C|F])")
    core_1_temp=re.compile("Core 1: +(\\+.+?)(°[C|F])")
    core_2_temp=re.compile("Core 2: +(\\+.+?)(°[C|F])")
    core_3_temp=re.compile("Core 3: +(\\+.+?)(°[C|F])")
    data=list()
    
    buf=os.popen("sensors")

    for line in buf:
        m=vcore.match(line)
        if m:
            data.append(("VCore",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=pt_33.match(line)
        if m:
            data.append(("V3.3",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=pt_50.match(line)
        if m:
            data.append(("V5",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=pt_120.match(line)
        if m:
            data.append(("V12",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=cpu_fan.match(line)
        if m:
            data.append(("CPU Fan",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=ch_1_fan.match(line)
        if m:
            data.append(("CH1 Fan",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=ch_2_fan.match(line)
        if m:
            data.append(("CH2 Fan",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=ch_3_fan.match(line)
        if m:
            data.append(("CH3 Fan",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=pwr_fan.match(line)
        if m:
            data.append(("POWER Fan",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=cpu_temp.match(line)
        if m:
            data.append(("CPU TP",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=mb_temp.match(line)
        if m:
            data.append(("MB TP",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=core_0_temp.match(line)
        if m:
            data.append(("Core0 TP",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=core_1_temp.match(line)
        if m:
            data.append(("Core1 TP",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=core_2_temp.match(line)
        if m:
            data.append(("Core2 TP",m.groups(0)[0],m.groups(0)[1]))
            continue
        m=core_3_temp.match(line)
        if m:
            data.append(("Core3 TP",m.groups(0)[0],m.groups(0)[1]))
            continue
    buf.close()
    
    
    return data
if __name__ == "__main__":
    m=sensorData()
    if len(m)==0:
        print ("Not ready")
        print ()
        print ("#000088")
    else:
        idx=item_idx(len(m))
        print("{}: {}{}".format(m[idx][0],m[idx][1],m[idx][2]))
        print('')
        print('#00bbee')
