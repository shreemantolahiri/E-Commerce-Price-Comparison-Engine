
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
        
def get_html(url):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    browser=webdriver.Chrome(executable_path=DRIVER_PATH,options=op)
    browser.get(url)
    return browser.page_source

def amazon():
    URL = amazon_link
    amazon_home ='https://www.amazon.in'
    html= get_html(URL)
    soup = BeautifulSoup(html, 'lxml')

    prod_cards=soup.find_all('div',attrs={'data-asin': True,'data-component-type':'s-search-result'})
    cls1='sg-col-4-of-12'
    cls2='s-result-item'
    ctr1=0

    for i in prod_cards:

        if ctr1<1:
            cls=i.get('class')
            if cls1==cls[0]:
                typ=1
            elif cls2==cls[0]:
                typ=2
            ctr1+=1
        else:
            break

    items=[]
    ctr=0
    for card in prod_cards:
        if ctr<5:
            item=[]
            try:
                h2=card.h2
            except:
                title=''
                link=''
            else:
                if typ==1:

                    b=''
                    if card.h5:
                        b=card.h5.text.strip()
                        b=b+' '

                    title= b+h2.text.strip()
                    link=amazon_home + h2.a.get('href')

                else:
                    title = h2.text.strip()
                    link = amazon_home + h2.a.get('href')

            try:
                price=card.find('span',attrs={'class':'a-price-whole'}).text.strip('.').strip()
            except:
                price=''
            else:

                price=''.join(price.split(','))
            item=[title,price,link]
            items.append(item)
            ctr+=1
        else:
            break

    for i in items:
        print(i)


if __name__ == "__main__":
    flipkart()
    amazon()
