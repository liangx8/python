class docs:
    """
李明:级别 0x20fb
第一个字节：8?（?为0~E） 80为归属值，代表刘备这边的人物。8E为战死或还没有出现的人物（即目前在野）
第二个字节：?? 为人物----不甩它
第三、四、五个字节：通常都为 00 00 64----没研究过----照样不甩它
第六、七个字节：?? ?? 是兵力（即带的兵数），这里有一点是比较特殊的，因为内存里的16进制分配不同，所以你在用计算器进行16进制转换十进制的时候要反过来算（看着迷忙的话，继续看下去就会明白的），例如：兵力为： E2 04 时，代表的十六进制数为：04E2--转换为十进制后为：1250，即有1250的兵力；要改成兵力为5000，怎么改呢？很简单，换算成十六进制数为1388，但是，改的时候就要颠倒过来，把E2改为88，把04改为13。这样就可以了。
第八个字节：兵种。（兵种的取值范围从00到12，00-短兵，01-长兵，02-战车，03-弓兵，04-连弩兵， 05-投石军，06-轻骑兵，07-重骑兵，08-近卫军，09-山贼， 0A-恶贼，0B-义贼，0C-军乐队，0D猛兽兵团，0E-武术家，0F-妖术师，10-异民族，11-民众，12-运输队。）尽量不要改刘备的兵种，很容易死机。
第九个字节：就是大家所熟悉的等级了。记着修改的时候要改的是十六进制数非十进制。例如：99级为：63。50级为：32。
第十个字节：为经验值。本人觉得没有改的必要。
第十一至第十八个字节：物品栏。（00-遁甲天书，01-青囊书，02-鼓吹具，03-孙子兵法，04-孟德新书， 05-黄爪飞龙，06-的卢马，
07-赤兔马，08-玉玺，09-倚天剑， 0A-青虹剑，0B-七星剑，0C-青龙偃月刀，0D-三尖刀，0E-方天画戟， 0F-蛇矛，10-弓术指南术，
11-马术指南术，12-剑术指南术，13-长枪， 14-步兵车，15-连弩，16-发石车，17-马铠，18-近卫铠，19-无赖精神， 1A-侠义精神，
1B-酒，1C-特级酒，1D-老酒，1E-豆，1F-麦，20-米， 21-炸弹，22-落石书，23-山崩书，24-山洪书，25-漩涡书，26-浊流书， 27-海啸书，28-焦热书，29-火龙书，2A-猛火书，2B-浓雾书，2C-雷阵雨书， 2D-豪雨书，2E-援队书，2F-援部书，30-援军书，31-平气书，
32-活气书， 33-勇气书，34-伤药，35-中药，36-茶，37-赦命书，38-援军报告， 39-雌雄双剑，3A-英雄之剑，3B-霸王之剑，3C-六韬， 3D-三略，3E-吴子兵法，FF-没有物品。）
"""
    pass
def intLittle(buf):
    n=len(buf) - 1
    s=buf[n]
    n = n -1
    while n>= 0:
        s = s * 256 + buf[n]
        n = n-1
    return s
def shiftIn(buf,b):
    n = len(buf)
    for i in range(n-1):
        buf[i]=buf[i+1]
    buf[n-1]=b
def search(f1,value,width,cb):
    """ width is only accepts 2,4,8 """
    idx=0
    o1=open(f1,"rb")

    buf=list()
    for i in range (width):
        buf.append(ord(o1.read(1)))
    while True:
        xx=intLittle(buf)
        if xx==value:
            cb(idx)
        b=o1.read(1)
        idx = idx+1
        if b:
            shiftIn(buf,ord(b))
        else:
            break

    o1.close()
def diff(f1,f2,cb):
    idx=0
    o1=open(f1,"rb")
    o2=open(f2,"rb")
    while True:
        b1=o1.read(1)
        b2=o2.read(1)
        if b1 and b2:
            if b1!=b2:
                cb(idx,b1,b2)
        else:
            break
        idx = idx +1
    o2.close()
    o1.close()
def  run(idx,b1,b2):
    #print("{:04x} {:02x} {:02x}".format(idx,ord(b1),ord(b2)))
    if ord(b1)==93 and ord(b2)==30:
        print("{:04x}".format(idx))
if __name__=='__main__':
    #diff('/home/arm/dos/Reko3/REKO3/MSAVE1.R3S','/home/arm/dos/Reko3/REKO3/MSAVE2.R3S',run)
    diff('/home/arm/dos/SAN5X/NBDATA.S5','/home/arm/dos/SAN5X/nbdata.s5.old',run)

