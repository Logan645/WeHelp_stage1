import pandas as pd
data=pd.read_csv("googleplaystore.csv")
# print(data)
print("資料欄位：",data.columns)
print(data["Installs"])
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+Free]",""))
print(data["Installs"].mean())
condition=data["Installs"]>=100000
data=data[condition]
print(data["Installs"].mean())
print("安裝數量大於十萬的應用程式有：",data["Installs"].shape[0]) #shape會告訴我們有幾列幾欄

#基於資料的應用：關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字")
condition=data["App"].str.contains(keyword,case=False) #略大小寫
print("包含關鍵字的應用程式數量：",data["App"][condition].shape[0])
