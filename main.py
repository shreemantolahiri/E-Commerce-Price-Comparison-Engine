import requests
from bs4 import BeautifulSoup
URL="https://www.amazon.in/dp/B074WZJ4MF/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=8bc2212eee66e1c1bdca057df16f612f&hsa_cr_id=2722802130102&pd_rd_plhdr=t&pd_rd_r=135b3806-45ad-402d-9df7-0f14d458f874&pd_rd_w=19o2S&pd_rd_wg=TBmei&ref_=sbx_be_s_sparkle_mcd_asin_0_title"
HEADERS={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

def getPrice():
    page= requests.get(URL,headers=HEADERS)

    # print(htmlcontent)
    soup=BeautifulSoup(page.content,'html.parser')
    # print(soup.prettify)
    title=soup.find(class_= "a-price-whole").get_text()
    
    print(title)

if __name__=="__main__":
    getPrice()