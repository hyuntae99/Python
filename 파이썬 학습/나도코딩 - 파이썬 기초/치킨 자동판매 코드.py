class SoldOutError(Exception):
    def __init__ (self):
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")

chicken = int(input("사장님, 오늘 치킨 총 수량을 입력해주세요."))
waiting = 1
while True:
    try:
        if chicken == 0:
            raise SoldOutError() #self값을 넣어야 하므로 ()
        print("[남은 치킨 : {0}마리]".format(chicken))
        order = int(input("손님, 치킨을 몇 마리 주문하시겠습니까??"))
        if order < 1:
            raise ValueError
        elif order > chicken:
            print("재료가 부족합니다.")
        else:
            print("대기번호 {0}번 손님. {1}마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order   
                    
    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except SoldOutError:
        break
    