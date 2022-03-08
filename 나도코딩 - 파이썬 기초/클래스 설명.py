class Unit:
    def __init__(self, name, hp, damage): #__init__ 와 self는 기본
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}" .format(self.hp, self.damage))
        
marine1 = Unit("마린", 40, 5)       #위의 name, hp, damage 변수를 모두 대입해야 실행됨
marine2 = Unit("마린", 40, 5)       
tank1 = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80 , 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) 
# 새로운 객체에 name, hp, damage 사용가능

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True #clocking 이라는 새로운 변수 추가가능! 단 wrait2에게만 있음

if wraith2.clocking == True:
    print("현재 {}는 클로킹 상태입니다.".format(wraith2.name))