import requests
from bs4 import BeautifulSoup
import re

for year in range(2015, 2020):
    
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url) # 정보 받아오기
    res.raise_for_status() # 오류검사
    soup = BeautifulSoup(res.text, "lxml") # 정보 받아오기
 
    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        print(image_url)
        
        image_res = requests.get(image_url) 
        image_res.raise_for_status()
        
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)
        
        if idx >= 4: 
            break