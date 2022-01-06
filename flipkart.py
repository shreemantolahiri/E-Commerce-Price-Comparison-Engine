
import requests
from bs4 import BeautifulSoup
import re


# s1Q9rs #_1fQZEK
name=str(input("Enter item to search: "))


name=name.replace(' ','+')
flip = (f"https://www.flipkart.com/search?q={name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36."}
def flipkart():
    URL=flip
    page = requests.get(URL, headers=HEADERS)



    soup = BeautifulSoup(page.content,'html.parser')



    fin = re.compile(r'href\s?=\s?[\'"]?([^\'" >]+)')
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
    
    for j in range(5):
        info=[]
        
        content=requests.get(link[j], headers=HEADERS)
        newsoup=BeautifulSoup(content.content,'html.parser')

        for a in newsoup.select(".B_NuCI , ._16Jk6d  "):
            for i in a:
                i=str(i)
                info.append(i)
        info.append(link[j])
        INFO.append(info)        
    for i in range(len(INFO)):
        if (len(INFO[i])==5):
            INFO[i].pop(1)
            INFO[i].pop(1)
        price=str(INFO[i][1])
        price=price.lstrip("₹")
        price=''.join(price.split(','))
        INFO[i][1]=price
        print(INFO[i])
        

if __name__ == "__main__":
    flipkart()
