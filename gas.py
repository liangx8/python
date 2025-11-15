import datetime
gasdate = (datetime.datetime(2024,12,18),
           datetime.datetime(2025,2,10),
           datetime.datetime(2025,4,1),
           datetime.datetime(2025,6,18),
           datetime.datetime(2025,9,16),
           datetime.datetime(2025,11,4,9,59,59))
if __name__ == "__main__":
    cnt=len(gasdate)
    for x in range(cnt-1):
        a=gasdate[x]
        n=datetime.datetime(a.year,a.month,a.day)
        print(n,"~",gasdate[x+1],"=>",gasdate[x+1]-n)
