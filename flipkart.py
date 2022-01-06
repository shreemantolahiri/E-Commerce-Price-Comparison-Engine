import codecs
import urllib
import requests
from bs4 import BeautifulSoup
import re
import webbrowser
import csv

# from pricecomparison.main import flipkart
# s1Q9rs #_1fQZEK
name=str(input("Enter item to search: "))
#name='trackpants'


name=name.replace(' ','+')
flip = (f"https://www.flipkart.com/search?q={name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
amaz = f"https://www.amazon.in/s?k={name}&crid=2HPXEJMH5RRW7&sprefix={name}%2Caps%2C204&ref=nb_sb_noss_2"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36."}
def flipkart():
    URL=flip
    page = requests.get(URL, headers=HEADERS)
    get=str(page.content)
    

    response = urllib.request.urlopen(URL)
    webContent = response.read().decode('UTF-8')

    f = open('search.html', 'w',encoding="utf-8")
    f.write(webContent)
    f.close


    file_open = codecs.open("search.html", "r", "utf-8")
    soup = BeautifulSoup(file_open,'html.parser')

    global links_list
    links_list = []

    fin = re.compile(r'href\s?=\s?[\'"]?([^\'" >]+)')
    # fin = re.compile('href="(.+?)"')
    #classchecker
    chck = soup.find_all('a', attrs={'target': '_blank', 'class': '_1fQZEK'})
    if len(chck)==0:
        class1= 's1Q9rs'
    else:
        class1='_1fQZEK'
    INFO=[]
    link=[]
    for a in soup.find_all('a', attrs={'target' :'_blank','class':class1}):
            a = str(a)
            se = (fin.findall(a))
            
            for i in se:
                full = ("https://www.flipkart.com" + i)
                link.append(full)
    
    for i in range(5):
        info=[]
        info.append(link[i])
        content=requests.get(link[i], headers=HEADERS)
        newsoup=BeautifulSoup(content.content,'html.parser')

        for a in newsoup.select(".B_NuCI , ._16Jk6d  "):
            for i in a:
                i=str(i)
                info.append(i)
        
        INFO.append(info)        
    for i in INFO:
        print(i)

if __name__ == "__main__":
    flipkart()
