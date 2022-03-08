import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 모든 html 값을 가지고 있음
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a 엘리멘트
# print(soup.a.attrs) # a 엘리멘트의 속성 정보
# print(soup.a["href"]) # a 엘리멘트의 href 속성 값을 출력


# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# # soup객체에 class:"Nbtn_upload인 a 엘리멘트를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"}))
# # class:"Nbtn_upload인 어떤 엘리멘트를 찾아줘

# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text()) # 텍스트만 가져옴
# # print(rank1.next_sibling) # 사이가 다른 공간이 있어서 2번해야함
# rank2 = rank1.next_sibling.next_sibling # 다음 값 가져오기
# print(rank3.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # 이전 값 가져오기
# print(rank2.get_text())
# print(rank1.parent) # 부모 값 가져오기
# rank2 = rank1.find_next_sibling("li") # next_sibling 상위호환
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li") # previous_sibling 상위호환
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li")) # 모든 형제 값 가져오기


webtoon = soup.find("a", text="퀘스트지상주의-19화 훔쳐보기 랭크 업이다!")
print(webtoon)

# <a onclick="nclk_v2(event,'rnk*p.cont','783052','2')" 
# href="/webtoon/detail?titleId=783052&amp;no=19" 
# title="퀘스트지상주의-19화 훔쳐보기 랭크 업이다!">퀘스트지상주의-19화 훔쳐보기 랭크 업이다!</a>