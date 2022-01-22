from cProfile import label
from itertools import dropwhile
from lib2to3.pgen2.token import NAME
from turtle import heading
import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from tkinter import *
import webbrowser

DRIVER_PATH=str(Path('chromedriver.exe').resolve())
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36."}

def flipbut():
    l1=INFO[flipind][2]
    webbrowser.open(l1, new=1)

def amazbut():
    l2=items[amazonind][2]
    webbrowser.open(l2, new=2)
def close_new():
    comparison.destroy() 

def close():
    root.destroy()    
def spawn():

    global root
    root = Tk()
    root.title('E-Commerce-Price-Comparison-Engine')
    root.geometry('900x500')
    
    name=""
    var = StringVar()
    search_item=Label(root,textvariable=var)  
    search_item.grid(row=1,column=2,pady=50,padx=70,ipadx=10)
    var.set("SEARCH ITEM")
    global Entry_item
    Entry_item=Entry(root,width=50)
    Entry_item.grid(row=1,column=3,columnspan=40,padx=40)
    
    #************FLIPKART LABEL**********
    VAR2= StringVar()
    WEBSITE1=Label(root,textvariable=VAR2)
    WEBSITE1.grid(row=4,column=2,pady=50,padx=70,ipadx=25)
    VAR2.set("FLIPKART")

    #************AMAZON LABEL**********
    VAR3= StringVar()
    WEBSITE2=Label(root,textvariable=VAR3)
    WEBSITE2.grid(row=5,column=2,pady=50,padx=70,ipadx=25)
    VAR3.set("AMAZON")

    #************SEARCH BUTTON**********
    search_button=Button(root,text = 'SEARCH ON STORES', command = lambda: submit())
    search_button.grid(row=2,column=6,ipadx=25)

    #************RESET BUTTON**********
    reset_button=Button(root,text = 'RESET', command = lambda: reset())
    reset_button.grid(row=7,column=6,ipadx=25)

    #************COMPARE BUTTON**********
    compare_button=Button(root,text = 'COMPARE', command = lambda: compare())
    compare_button.grid(row=7,column=10,ipadx=25)

    #************EXIT BUTTON**********
    exit_button=Button(root,text = 'EXIT', command = lambda: close())
    exit_button.grid(row=7,column=20,padx=40,ipadx=25)
def reset():
    root.destroy()
    spawn()
    
def Imp(name):
    global flipkart_link
    global amazon_link

    flipkart_link = (f"https://www.flipkart.com/search?q={name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

    amazon_link = (f"https://www.amazon.in/s?k={name}&crid=2HPXEJMH5RRW7&sprefix={name}%2Caps%2C204&ref=nb_sb_noss_2")

def flipkart():
    
    URL=flipkart_link
    page = requests.get(URL, headers=HEADERS)



    soup = BeautifulSoup(page.content,'html.parser')



    fin = re.compile(r'href\s?=\s?[\'"]?([^\'" >]+)')
    chck = soup.find_all('a', attrs={'target': '_blank', 'class': '_1fQZEK'})
    if len(chck)==0:
        class1= 's1Q9rs'
    else:
        class1='_1fQZEK'
    global INFO
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
        # print(INFO[i])
        FLIPKARTTITLE.append(INFO[i][0])
        FLIPKARTPRICE.append(INFO[i][1])
def get_html(url):
    global dropctr
    dropctr=0
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
    global items        
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
    
    for i in range(len(items)):
        # print(items[i])
        AMAZONTITLE.append(items[i][0])
        AMAZONPRICE.append(items[i][1])
def submit():
    global FLIPKARTTITLE
    global FLIPKARTPRICE
    global AMAZONTITLE
    global AMAZONPRICE
    AMAZONTITLE=[]
    FLIPKARTTITLE=[]
    AMAZONTITLE=[]
    FLIPKARTTITLE=[]
    AMAZONPRICE=[]
    FLIPKARTPRICE=[]
    OPENER=[]
    
    
    name=str(Entry_item.get())
    Imp(name)
    flipkart()
    amazon()
             

    

    name=name.replace(' ','+')

    

        #*******PRODUCTS FROM FLIPKART**********        
    global Options1
    Options1=[
    FLIPKARTTITLE[0],
    FLIPKARTTITLE[1],
    FLIPKARTTITLE[2],
    FLIPKARTTITLE[3],
    FLIPKARTTITLE[4]  
    ]
    global variable1
    variable1 = StringVar(root)
    variable1.set("SEARCH RESULTS FROM FLIPKART")

    #************DROP DOWN FOR FLIPKART**********
    global dropFLIPKART
    
    dropFLIPKART=OptionMenu(root,variable1,*Options1)
    dropFLIPKART.grid(row=4,column=6,columnspan=40,padx=40)
        
    



        # #*******PRODUCTS FROM AMAZON************        
    global Options2    
    Options2=[
    AMAZONTITLE[0],
    AMAZONTITLE[1],
    AMAZONTITLE[2],
    AMAZONTITLE[3],
    AMAZONTITLE[4]
    ]
    global variable2
    variable2 = StringVar(root)
    variable2.set("SEARCH RESULTS FROM AMAZON")
    global dropAMAZON
    #************DROP DOWN FOR AMAZON**********
    dropAMAZON=OptionMenu(root,variable2,*Options2)
    dropAMAZON.grid(row=5,column=6,columnspan=40,padx=40)

    

    print("These are Flipkart results: ")
    SITE1=flipkart()
    print(FLIPKARTTITLE)
    print("These are Amazon results: ")
    SITE2=amazon()
    print(AMAZONTITLE)

def compare():
    
    global comparison
    comparison=Toplevel(root)
    comparison.geometry('700x500')
    comparison.title('Comparison Page')
    #***********HEADING 1**********
    var = StringVar()
    PRODUCT=Label(comparison,textvariable=var,font=('Helvetica', 10, 'bold'))
    PRODUCT.grid(row=1,column=2,pady=20,padx=50,ipadx=10)
    var.set("FLIPKART RESULTS")
    
    #**********PRODUCT NAME LABEL*********
    varia=StringVar()
    PROTI=Label(comparison,textvariable=varia)
    PROTI.grid(row=2,column=2,pady=20,padx=50,ipadx=10)
    varia.set("PRODUCT NAME")
    
    #*************PRODUCT PRICE LABEL*********
    vari=StringVar()
    PAISA=Label(comparison,textvariable=vari)
    PAISA.grid(row=3,column=2,pady=20,padx=50,ipadx=10)
    vari.set("PRODUCT PRICE")
    
    #*************NAME OF PRODUCT***********
    var1=StringVar()
    TITLE=Label(comparison,textvariable=var1,relief=SUNKEN)
    global flipind
    flipind=(Options1.index(str(variable1.get())))
    TITLE.grid(row=2,column=3,pady=20,padx=50,ipadx=10)
    var1.set(variable1.get())
    
    #*************PRICE OF PRODUCT***********
    var2=StringVar()
    PRICE=Label(comparison,textvariable=var2,relief=SUNKEN)
    PRICE.grid(row=3,column=3,pady=20,padx=50,ipadx=10)
    var2.set(str(FLIPKARTPRICE[flipind]))  
    
    
    #***********HEADING 2***************
    var3 = StringVar()
    PRODUCT=Label(comparison,textvariable=var3,font=('Helvetica', 10, 'bold'))
    PRODUCT.grid(row=5,column=2,pady=20,padx=50,ipadx=10)
    var3.set("AMAZON RESULTS")
    var4=StringVar()
    
    #****************PRODUCT NAME LABEL*************
    varia=StringVar()
    PROTI=Label(comparison,textvariable=varia)
    PROTI.grid(row=6,column=2,pady=20,padx=50,ipadx=10)
    varia.set("PRODUCT NAME")
    
    #***************PRODUCT PRICE LABEL*******************
    vari=StringVar()
    PAISA=Label(comparison,textvariable=vari)
    PAISA.grid(row=7,column=2,pady=20,padx=50,ipadx=10)
    vari.set("PRODUCT PRICE")
    
    #*************NAME OF PRODUCT********
    TITLE=Label(comparison,textvariable=var4,relief=SUNKEN)
    global amazonind
    amazonind=(Options2.index(str(variable2.get())))
    TITLE.grid(row=6,column=3,pady=20,padx=50,ipadx=10)
    var4.set(variable2.get())
    
    #**************PRICE OF PRODUCT**********
    var5=StringVar()
    PRICE=Label(comparison,textvariable=var5,relief=SUNKEN)
    PRICE.grid(row=7,column=3,pady=20,padx=50,ipadx=10)
    var5.set(str(AMAZONPRICE[amazonind]))

    #************FLIP BUTTON**********
    flip_button=Button(comparison,text = 'OPEN', command = lambda: flipbut())
    flip_button.grid(row=4,column=3,padx=40,ipadx=25)

    #************AMAZ BUTTON**********
    flip_button=Button(comparison,text = 'OPEN', command = lambda: amazbut())
    flip_button.grid(row=8,column=3,padx=40,ipadx=25)

    #************EXIT BUTTON**********
    exitt_button=Button(comparison,text = 'CLOSE', command = lambda: close_new())
    exitt_button.grid(row=15,column=3,padx=40,pady=20,ipadx=25)
    
    comparison.mainloop()

if __name__ == "__main__":
    spawn()
    root.mainloop()
    
