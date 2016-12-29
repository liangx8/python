import http.client

if __name__ == '__main__':
    h=http.client.HTTPConnection("192.168.30.1:3000")
    h.reqeust("GET","/")
    r=h.getresponse()
    print(r.read())
    
