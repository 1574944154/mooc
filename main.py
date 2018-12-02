import requests
from lxml import etree
from time import sleep

from duration.duration import Update_duration

url = "http://cqucc.minghuaetc.com/portal/session/unitNavigation/3768.mooc"

cookie_str = ""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Referer": "http://cqucc.minghuaetc.com/",
    "Cookie": cookie_str,
}

res = requests.get(url, headers=headers)
selector = etree.HTML(res.content)
units = selector.xpath('//div[@class="lecture-title"]')  #每一讲

for unit in units:
    unitid = unit.xpath('a/@unitid')[0]
    for item in unit.xpath('div[@class="lecture-action-group"]'):
        # itemids = item.xpath('a/@itemid')
        itemids_avai = item.xpath('a/i[contains(@class, "icon-disabled")]/../@itemid')
        for itemid in itemids_avai:
            print(unitid, itemid)
            dur = Update_duration(unitid,itemid,cookie_str)
            for i in range(60200, 1350000, 60200):
                dur.onTimeCallback(i)
                sleep(6)
            dur.onCompleteCallback()
