#사용자 정의 에러
class BignumberError(Exception):
    def __init__ (self, msg):
        self.msg = msg
    def __str__ (self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BignumberError("입력값 : {0}, {1}".format(num1, num2)) #임의로 에러발생 가능
    print("{0} / {1} = {2}".format(num1, num2, round(num1/num2,2)))
except ValueError:
    print("한 자리 숫자만 가능합니다.")
except BignumberError as err:
    print("에러가 발생했습니다.")
    print(err) #사용자정의 에러는 출력 안되는듯??
    
finally: #오류가 발생하든 아니든 마지막순서로 무조건 실행됨(except에 설정된 오류가 아니어도)
    print("계산기를 이용해주셔서 감사합니다.")