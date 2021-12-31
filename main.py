import requests
from bs4 import BeautifulSoup

name=input("ENTER THE SEARCH: ")
# name=""
name=name.replace(" ","+")

#_4rR01T---VERTICAL   s1Q9rs----HORIZONTAL
HEADERS={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
URL=""
flip=(f"https://www.flipkart.com/search?q={name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
amaz = (f"https://www.amazon.in/s?k={name}&crid=2HPXEJMH5RRW7&sprefix={name}%2Caps%2C204&ref=nb_sb_noss_2")

    

def flipkart():
    URL=flip
    page= requests.get(URL,headers=HEADERS)
    soup=BeautifulSoup(page.content,'html.parser') 
    class1='_4rR01T'
    anchor=soup.findAll(class_=class1)
    if len(anchor)==0:
        class1='s1Q9rs'
        info=[]
        anchor=soup.findAll(class_=class1)
        if len(anchor) == 0:
            class1 = 's1Q9rs'
        anchor = soup.findAll(class_=class1)
        info = []
        #for row in soup.findAll('a', attrs={'class': class1}):
            #print(type(row.a[title]))
            # info.append(row.a['title'])


        ctr = 0
        for i in anchor:
            

            if ctr < 5:

                i = str(i)
                # print(i,class1)

                L = i.split('title="')
                fin = L[1].split('>')
                fin1 = fin[0].rstrip('"')

                item_names = fin1.upper()
                # print(item_names)
                
                # verification
                search = name.upper()
                search = search.split('+')
                # print(search)
                checker = 0

                for i in range(len(search)):

                    if search[i] in item_names:
                        checker += 1

        
                    else:
                        
                        break

                    if checker == len(search):
                        print(item_names)
                        ctr += 1
        
        if ctr == 0:
        
            for i in anchor:
        
                if ctr < 5:
        
                    i = str(i)
                    L = i.split('title="')
                    fin = L[1].split('>')
                    fin1 = fin[0].rstrip('"')
        
                    item_names = fin1.upper()
                    print(item_names)
                    ctr += 1    
        
    
    else: 
        ctr=0
        for i in anchor:

            if ctr<5:

                i = str(i)
                # print(i,class1)
                new = i.lstrip(f'<div class="{class1}">').rstrip('</div>')
                item_names=new.upper()
                # print(item_names)
                # verification
                search=name.upper()
                search=search.split('+')
                # print(search)
                checker=0

                for i in range(len(search)):


                    if search[i] in item_names:
                        checker+=1
                        # print("he")

                    else:
                        # print("she")
                        break

                    if checker==len(search):
                        print(item_names)
                        ctr += 1

            #incase no output, verification method is skipped
            if ctr==0:

                for i in anchor:

                    if ctr < 5:

                        i = str(i)
                        new = i.lstrip(f'<div class="{class1}">').rstrip('</div>')
                        item_names = new.upper()
                        print(item_names)
                        ctr+=1
                        
def amazon():
    URL=amaz
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')

    anchor = soup.findAll(class_='a-size-medium a-color-base a-text-normal')
    ctr = 0
    for i in anchor:

        if ctr < 5:

            i = str(i)
            if "Did you mean" in i:
                continue
            new = i.lstrip('<span class="a-size-medium a-color-base a-text-normal">').rstrip('</span>')
            item_names = new.upper()
            # verification
            search = name.upper()
            search = search.split('+')
            checker = 0

            for i in range(len(search)):

                if search[i] in item_names:
                    checker += 1

                else:
                    break

                if checker == len(search):
                    print(item_names)
                    ctr += 1

    # incase no output, verification method is skipped
    if ctr == 0:

        for i in anchor:

            if ctr < 5:
                i = str(i)
                new = i.lstrip('<span class="a-size-medium a-color-base a-text-normal">').rstrip('</span>')
                item_names = new.upper()
                print(item_names)
                ctr += 1

                        
if __name__=="__main__":
    print("These are Flipkart results: ")
    flipkart()
    print("These are Amazon results: ")
    amazon()
