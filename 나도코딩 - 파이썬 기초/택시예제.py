from random import *

customers = range(0,51) #50명의 손님 리스트 

count = 1 #횟수 변수

for i in customers: #50번 실행
    time = randint(5,50) #매 실행마다 시간변수 설정
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)" .format(i, time))
        count += 1 #탑승할때마다 횟수변수 더해주기
    else :
        continue

print("총 탑승 승객 : {}명" .format(count))