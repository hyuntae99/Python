site = str(input()) #사이트 입력받기

index = site.index("/")
index = site.index("/", index+1) #2번째 / 위치 찾기
site1 = site[index+1:] #2번째 / 위치 다음만 남기기

index1 = site1.find(".") #.위치 찾기
site2 = site1[:index1] #.위치 전까지만 남기기

many = len(site2) #남은 부분의 크기
k = site2.count("e") #남은 부분 중 e의 포함 개수
m = site2[0:3] #첫번째부터 세번째까지 남기기

print("생성된 비밀번호 : ", str(m) + str(many) + str(k) + "!")