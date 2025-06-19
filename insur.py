def insur(total):
    num=20
    slg=total/num
    byear=2010
    ary=[]
    
    itrt=0
    rate=0.02
    
    for seq in range(num):
        val=slg*(seq+1)+itrt
        itrt=val * rate
        ary.append((seq+byear,val,itrt))
    val = ary[-1][1]
    for seq in range(30):
        val=val+itrt
        itrt=val * rate
        ary.append((seq+byear+20,val,itrt))
    for row in ary:
        print(row)
    row=ary[-1]
    print(row[0],row[1]/total/50)
    print((row[1]-total)/50/total)

if __name__=="__main__":
    insur(32400)
