N = int(input()) # 원숭이 수

cage = []
rival_num = []
for i in range(N):
    cage.append([])
    data = list(map(int, input().split()))
    for j in range(1, data[0]+1):
        cage[i].append(data[j]) # 앙숙데이터
    rival_num.append(data[0]) # 앙숙 수 데이터

cage_1 = [] 
cage_2 = []
count = 0

for idx, rival in enumerate(cage):
    for i in range(1,N+1): # 원숭이 수만큼 반복
        if idx+1 == i:
            for k in range(rival_num[i-1]):
                if rival[k] in cage_1:
                    count += 1 # 앙숙과 겹칠때마다 카운트
            if count >= 2:
                cage_2.append(idx+1) # 앙숙이 2명이상일 경우 2번케이지에 넣기
                count = 0 # 변수 초기화
            else:
                cage_1.append(idx+1) # 앙숙이 1명이하일 경우 1번케이지 넣기
                count = 0 # 변수 초기화


# 처음부터 끝까지 순서대로 진행했기때문에 오류가 있을 수 있으므로 검토하기
for idx, rival in enumerate(cage):
    for i in range(1,N+1): # 원숭이 수만큼 반복
        if idx+1 == i:
            for k in range(rival_num[i-1]):
                if rival[k] in cage_1:
                    count += 1
            if count >= 2:
                if idx+1 in cage_1:  # 1번케이지에 해당 원숭이가 들어씨고 앙숙이 2명이상 있을경우
                    cage_1.remove(idx+1) # 1번케이지에서 해당 원숭이 삭제
                    cage_2.append(idx+1) # 2번케이지에 대신 추가
                    count = 0
                else: # 앙숙이 2명이상 있지만 해당 케이지에 없는경우 -> 검토 통과
                    count = 0
            else:
                count = 0
    
# 시각효과를 위한 정렬
cage_1.sort() 
cage_2.sort()

# 검토로 인해 1번케이지, 2번케이지가 순서가 바뀌었으므로 바꿔서 출력
for i in range(len(cage_2)):
    print(cage_2[i], end=" ")
print("")
for i in range(len(cage_1)):
    print(cage_1[i], end=" ")
print("")


        