#抓取ptt八卦版的網頁原始碼(html)
import urllib.request as req
def getdata(url):
    #建立一個request物件，附加request header的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #解析原始碼，取得 每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser") #讓beautifulsoup協助我們解析html格式文件
    print(root.title.string)
    titles=root.find_all("div", class_="title") #尋找class="title"的div標籤
    for title in titles:        
        if title.a!=None: #如果標籤包含a標籤（沒有被刪除），印出來
            print(title.a.string)
    #抓取上一頁的連結標籤
    nextlink=root.find("a",string="‹ 上頁")
    return nextlink["href"]
pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"
page=0
while page<5:
    pageurl="https://www.ptt.cc"+getdata(pageurl)
    page+=1
