#홀수 좌석 출력하기

# 내 답변
for i in range(0,10):
    print("A" + str(2*i+1), end = " ")
print()

    
# 모범답안

for i in range(1,21):
    if i % 2 == 1: # i가 짝수일 경우
        print("A" + str(i), end = " ")
print()
        
        
for i in range(1,21)[::2]: #간격 설정 -> 1 3 5 ...
    print("A" + str(i), end = " ")