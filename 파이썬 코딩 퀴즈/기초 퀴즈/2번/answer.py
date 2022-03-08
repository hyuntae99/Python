from random import *

words = ["apple","banana", "orange"]
word = choice(words)
print("answer : " + word)

letters = ""

while True:
    succed = True
    print()
    for w in word: # 변수 in 문자열
        if w in letters:
            print(w, end=" ")
        else:
            print("_",end = " ")
            succed = False
    print()
    
    if succed == True:
        print("Success!")
        break
    
    letter = input("Input Letter >> ")
    
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Correct")
    else:
        print("Wrong")
    
