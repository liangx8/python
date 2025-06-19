import datetime
gasdate = (datetime.date(2024,12,18),datetime.date(2025,2,10),datetime.date(2025,4,1),datetime.date(2025,6,18))
if __name__ == "__main__":
    cnt=len(gasdate)
    for x in range(cnt-1):
        print(gasdate[x],"~",gasdate[x+1],"=>",gasdate[x+1]-gasdate[x])
