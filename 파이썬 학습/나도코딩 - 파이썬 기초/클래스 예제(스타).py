from random import *

def game_start():
    print("[알림] 게임을 시작합니다.")
def game_over():
    print("Player : gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")
    pass  #종료

class Unit: #일반유닛 생성메소드 - 부모클래스
    def __init__(self, name, hp, speed): #__init__ 와 self(자기자신)는 기본
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
            .format(self.name, location, self.speed)) 
        
    def damaged(self, damage): #타격 메소드
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
        
        
#공격 유닛
class AttackUnit(Unit): #공격유닛 생성메소드 - 자식클래스
    def __init__(self, name, hp, speed, damage): #__init__ 와 self는 기본
        Unit.__init__(self, name, hp, speed) #상속
        self.damage = damage
        
    def attack(self, location):  #공격 메소드
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) 
        #location = 전달받은 값, self.name은 클래스로 정의된 자기자신에 대한 값


#공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
              .format(self.name, location, self.flying_speed))
        
#공격 공중 유닛
class FlyableAttackUnit(AttackUnit, Flyable): #다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 속도 = 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)



#마린 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
        
    #스팀팩 : 이속, 공속 증가 단, 체력 10감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
        else :
            print("{} : 체력이 부족하여 사용할 수 없습니다.".format(self.name))

#탱크 클래스
class Tank(AttackUnit):
    #시즈모드 : 탱크를 고정(이동불가), 공격력 증가
    seize_develop = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_develop == False:
            return
        #시즈모드가 아닐때 -> 시즈모드
        if self.seize_mode == False:
            print("{} : 시즈모드롤 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #시즈모드 일때 -> 시즈모드 해제
        else:
            print("{} : 시즈모드롤 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

#레이스 클래스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80 ,20 ,5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print("{} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else :
            print("{} : 클로킹 모드를 실행합니다.".format(self.name))
            self.clocked = True


# #건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit. __init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) #self 쓰면 안됨
#         self.location = location

# #서플라이 : 건물, 8개 유닛 수용가능
# supply_depot = BuildingUnit("서플라이", 500, "7시")



# 벌처와 배틀크루저
# vulture = AttackUnit("벌쳐", 80, 10 ,20)
# battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# vulture.move("11시")
# # battlecrusier.fly(battlecrusier.fly, "5시")
# battlecrusier.move("5시")

#발키리
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


# 메딕 (힐러)
# medick = Unit("메딕", 100)
# print("{0}유닛이 생성되었습니다. \nhp는 {1}입니다.".format(medick.name, medick.hp)) 
       
       
# 파이어뱃 (공격유닛)
# firebat = AttackUnit("파이어뱃", 50 ,16)
# firebat.attack("5시")
# firebat.damaged(25)
# firebat.damaged(25)












#게임 진행

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")
    
Tank.seize_develop = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine): #isintance는 리스트 안의 클래스 파악
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
        
        
for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21))
    
game_over() 


