
print("팩토리얼 계산기 입니다.")
n = int(input("원하는 숫자를 입력하세요 : "))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(n)
print("{0}! = {1}입니다".format(n, result))

