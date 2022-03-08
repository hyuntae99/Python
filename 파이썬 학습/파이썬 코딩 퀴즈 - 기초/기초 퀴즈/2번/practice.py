from random import *

print("게임에 사용할 단어를 입력해주세요.")
print("단어을 다 등록하셨으면 ENTER 를 입력하세요.")
answers = []
while True:
    word = str(input())
    if len(word) == 0: #ENTER키 활용 
        break
    answers.append(word)
    
answer = choice(answers)
answer = list(answer)

A = ["_"] * len(answer)
for i in range(len(answer)):
        print(A[i], end=" ")
        
while True:
    print()
    a = str(input("Input Letter >> "))
    for i in range(len(answer)):
        if a == answer[i]:
            A[i] = answer[i]
        else:
            pass
        
    for i in range(len(answer)):
        print(A[i], end=" ")
            
    if A == answer:
        print()
        print("\nSuccess!")
        break