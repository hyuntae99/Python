def three():
    print("three", end=" ")
    return 3

def five():
    print("five", end=" ")
    return 5

def seven():
    print("seven", end=" ")
    return 7

# 메인코드
three() > five() > seven() 
# three() > five() and five() seven()
# 앞의 three() > five() : False 이므로 뒤의 코드는 실행X
# 따라서 three five

print()

print(3 > 5 > 7) # (3 > 5) and (5 > 7)