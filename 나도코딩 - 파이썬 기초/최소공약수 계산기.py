import math

print("최대공약수 계산기 입니다.") 
print("원하는 두 수를 입력 후 엔터키를 입력하세요.") 
data = list(map(int, input().split()))

def 최대공약수 (a, b):
    
    answer = math.gcd(a, b)

    if answer == 1 :
        print(a, "과",b, "는 서로소입니다.")
        print(a, "과" ,b, "의 최대공약수는", answer, "입니다.")

    else :
        print(a, "과" ,b, "의 최대공약수는", answer, "입니다.")


최대공약수 (data[0], data[1])
