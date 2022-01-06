from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver



name=str(input("Enter item to search: "))
name=name.replace(' ','+')
amazon_link = (f"https://www.amazon.in/s?k={name}&crid=2HPXEJMH5RRW7&sprefix={name}%2Caps%2C204&ref=nb_sb_noss_2")
DRIVER_PATH=str(Path('chromedriver').resolve())
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
    amazon()





