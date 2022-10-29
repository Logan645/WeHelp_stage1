import urllib.request as request #連線套件
import json #json讀取套件
import datetime as dt #辨別日期
from datetime import datetime 
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式

all_list=data["result"]["results"]

with open("data.csv",mode="w",encoding="utf-8") as file:
    for i in all_list: #i是指第幾個物件
            #寫入的每個欄位都要記得加i
            date_string=i['xpostDate']
            date_object=datetime.strptime(date_string,'%Y/%m/%d') 
            #AttributeError: type object 'datetime.datetime' has no attribute 'datetime'
            address=(i['address'])
            region=address[5:8] #只抓取特定位置的字
            file_url='https://'+i['file'].split('https://')[1]
            if date_object>dt.datetime(2014,12,31):
                file.write(i['stitle']+','+region+','+i['longitude']+','+i['latitude']+','+file_url+'\n')