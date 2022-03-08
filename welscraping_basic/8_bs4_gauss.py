import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class" : "title"})
# title = cartoons[0].a.get_text() # 첫번째 제목
# link = cartoons[0].a["href"] # 링크 가져오기
# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목과 링크 가져오기
# for cartoon in cartoons: 
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)
    
    
# 평점 분석하기    
total_rates = 0
cartoons = soup.find_all("div", attrs={"class" : "rating_type"}) 
# 상위 div에 있는 rating_type에 속한 모든 값

for cartoon in cartoons: 
    rate = cartoon.find("strong").get_text() # strong이 들어간 모든 값(텍스트만)
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ",round(total_rates,3))
print("평균 점수 : ",round(total_rates / len(cartoons),3))