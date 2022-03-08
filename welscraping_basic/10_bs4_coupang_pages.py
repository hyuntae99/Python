import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

for i in range(1,6): # 페이지 수
    
    print("페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
    
    res = requests.get(url, headers=headers) # 유저인척 하는 방법
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())

    for item in items:
        
        # 광고 제품은 제외 
        ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print(" <광고 상품은 제외합니다>")
            continue
        
        name = item.find("div", attrs={"class":"name"}).get_text()
        
        # 애플 제품 제외
        if "Apple" in name:
            # print(" <Apple상품 제외 합니다>")
            continue
        
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        
        # 리뷰 100개이상, 평점 4.5이상만 조회
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점 없음"
            # print(" <평점 없는 상품 제외합니다>")
            continue
        
        rating_count = item.find("span", attrs={"class":"rating-total-count"})
        if rating_count:
            rating_count = rating_count.get_text() # (26) 
            rating_count = rating_count[1:-1] # 1번부터 뒤쪽 앞까지 받기
        else:
            rating_count = "평점 수 없음"
            # print(" <평점 수 없는 상품 제외합니다>")
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]
        
        
        if float(rate) >= 4.5 and int(rating_count) >= 100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rating_count}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-" * 120)
        