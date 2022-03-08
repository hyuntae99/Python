"""from random import *

# 1~20까지 리스트 만들기
id = [0] * 20
for i in range(20):
    id[i] = i+1

# 1등 당첨자 뽑기
s = sample(id,1)

# 중복없으므로 1등 당첨자를 제외한 리스트 만들기
id1 = [i for i in id if i not in s]

# 2~4등 당첨자 뽑기
s1 = sample(id1, 3)

#결과 출력
print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : " + str(s))
print("커피 당첨자 : " + str(s1))
print("-- 축하합니다. -- ")
"""

#모범 답안

from random import *

users = range(1, 21)
users = list(users)

shuffle(users)

winners = sample(users, 4)

print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : ", winners[0])
print("커피 당첨자 : ", winners[1:])
print("-- 축하합니다. -- ")