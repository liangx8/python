import json
import datetime
def json_data(fn,encoding='utf-8'):
    f=open(fn,"r",encoding=encoding)
    j=json.load(f)
    f.close()
    return j

if __name__ == "__main__":
    buf=json_data("d:/download/expense.json")
    for it in buf['data']:
        #t = datetime.date.fromtimestamp(int(it['issue_date']))
        t=int(it['issue_date'])
        
        d=datetime.datetime.fromtimestamp(int(t/1000))
        print (it.get("remark"),it['amount'],d,t)
