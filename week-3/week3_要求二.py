title_list=[]
def PTT_movie_crawler(url):
    import urllib.request as req #連線套件
    #建立request物件，附帶上headers，模擬使用者行為
    request=req.Request(url, headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        })
    with req.urlopen(request) as response:
        data=response.read().decode('utf-8')
    import bs4 #使用beautifulsoap
    root=bs4.BeautifulSoup(data,"html.parser")  #讓beautifulsoup協助我們解析html格式文件 
    # print(root.title.string) #印出網頁標題
    titles=root.find_all('div',class_='title') #尋找所有class="title"的div標籤
    # print(titles) #這是一個list
    # title_list=[]
    for title in titles:
        if title.a!=None:  #先判別title.a是否存在
            title_string=title.a.string
            condition1=title_string.startswith('[好雷]')
            condition2=title_string.startswith('[普雷]')
            condition3=title_string.startswith('[負雷]')
            if condition1 or condition2 or condition3:
                # print(title.a.string)
                title_list.append(title.a.string)
    # print(title_list)
    next_page=root.find("a",string='‹ 上頁')
    next_page_url='https://www.ptt.cc/'+next_page['href']
    # print(next_page_url)
    return next_page_url

page_url="https://www.ptt.cc/bbs/movie/index9508.html"
page=0
while page<5:
    page_url=PTT_movie_crawler(page_url)
    page+=1
print(len(title_list))

with open("movie.txt",mode="w",encoding="utf-8") as file:
    for i in title_list:
        if i.startswith('[好雷]'):
            file.write(i+'\n')
    for i in title_list:
        if i.startswith('[普雷]'):
            file.write(i+'\n')
    for i in title_list:
        if i.startswith('[負雷]'):
            file.write(i+'\n')
