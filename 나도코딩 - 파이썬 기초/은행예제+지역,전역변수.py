def deposit(money):
    global balance
    balance += money #새로 변수를 정의하려면 global을 써야함
    print("입금이 완료되었습니다. 잔액은 {}원 입니다." .format(balance))
    return balance

def withdraw(money):
    if (balance > money):
        print("출금이 완료되었습니다. 잔액은 {}원 입니다." .format(balance - money))
        return balance - money #바로 return할 경우, 안써도 됨
    else :
        print("잔액이 부족합니다. 잔액은 {}입니다." .format(balance))
        return balance

balance = 0

while True :
    print("온라인 뱅킹 서비스입니다.")
    print("거래를 원하시면 1, 종료하시려면 2를 눌러주세요.")
    k = int(input())

    if k == 1:
        print("입금를 원하시면 1, 인출을 원하시면 2를 눌러주세요.")
        m = int(input())
        
        if m == 1:
            print("원하시는 금액을 입력하세요.")
            money = int(input())
            balance = deposit( money)
            print()

        if m == 2:
            print("원하시는 금액을 입력하세요.")
            money = int(input())
            balance = withdraw(money)
            print()

    elif k == 2:
        print("이용해주셔서 감사합니다.")
        print()
        break

    else :
        print("1 또는 2만 눌러주세요.")
        print()
