
def std_weight(height, gender):
    if gender == "남자":
        weight = round((height/100)**2*22,2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다." .format(height, weight))
    elif gender == "여자":
        weight = round((height/100)**2*21,2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다." .format(height, weight))

while True:
    print("표준 체중 계산기입니다.")
    print("이용을 원하시면 1을 종료하시려면 2를 입력하세요.")
    k = int(input())

    if k == 1:
        print("성별을 입력해주세요.")
        gen = str(input())
        if gen == "남자" or gen == "여자":
            print("키를 입력해주세요.")
            long = float(input())
            std_weight(long, gen)
            print()
        else :
            print("남자 또는 여자를 입력하세요!")

    elif k == 2:
        print("감사합니다.")
        break
    
    else :
        print("1 또는 2를 입력하세요!")
        print()