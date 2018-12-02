import requests
from time import sleep

class Update_duration(object):

    duration = 1302580

    def __init__(self, unitid, itemId, cookie_str):
        self.itemId = itemId
        self.unitid = unitid
        self.set_headers()
        self.headers['Cookie'] = cookie_str

    def onTimeCallback(self, currentPosition):
        url = "http://cqucc.minghuaetc.com/study/updateDurationVideo.mooc"
        data = {
            "itemId": self.itemId,
            "isOver": 1,
            "currentPosition": currentPosition,
            "duration": self.duration
        }
        res = requests.post(url=url, data=data, headers=self.headers)
        print(res)

    def onCompleteCallback(self):
        url = "http://cqucc.minghuaetc.com/study/updateDurationVideo.mooc"
        data = {
            "itemId": self.itemId,
            "isOver": 1,
            "duration": self.duration,
            "currentPosition": self.duration,
        }
        res = requests.post(url=url, data=data, headers=self.headers)
        print(res)

    def set_headers(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "http://cqucc.minghuaetc.com/study/unit/"+self.unitid+".mooc"
        }

if __name__ == '__main__':
    cookie = "moocvk=c75a827b99274b8db47accf8b1ca6cad; sos=true; moocsk=7ea2f65437404b59bbdb212b7a6032b3; JSESSIONID=BC1C32A48FD2928FB2599BC45529AF1C.tomcat-host-1"
    dur = Update_duration(itemId=155895, cookie_str=cookie)
    for i in range(60200, 1350000, 60200):
        dur.onTimeCallback(i)
        sleep(6)
    dur.onCompleteCallback()