import math
def run():
    one=math.pi/180
    for dgr in range(180):
        d1=dgr+120
        if d1 >= 180:
            d1 = d1 - 180
        d2=d1+120
        if d2 >= 180:
            d2 = d2 - 180
        print("{:3} {:f} {:3} {:3}".format(dgr,math.sin(dgr*one),d1,d2))

if __name__=="__main__":
    run()
