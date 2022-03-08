import pygame

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(center=position)
        
        self.position = position
        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        
        self.direction = LEFT # 집게의 이동방향
        self.angle_speed = 2.5 # 집게의 좌우 이동속도
        self.angle = 10 # 최초 각도 정의
        
        
    
    def update(self, to_x): # 캐릭터 가만히 놔두면 숨쉬는 것 같은 동작을 해줌
        if self.direction == LEFT:
            self.angle += self.angle_speed # 이동속도만큼 각도 증가
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed
            
        # 허용 각도 범위 처리
        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)
        
        self.offset.x += to_x
        
        self.rotate()

        
    def rotate(self):
        # 회전 대상 이미지, 회전각도, 이미지 크기 변경
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)
        
        offset_rotated = self.offset.rotate(self.angle)
        
        self.rect = self.image.get_rect(center=self.position+offset_rotated) 
        # pygame.draw.rect(screen, RED, self.rect, 1)
        
        
    def set_direction(self, direction):
        self.direction = direction
        
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3) # 중심점 표시
        # 중심점부터 집게중심점까지 선을 그리기
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5)
           
    def set__init__state(self):
        self.offset.x = default_offset_x_claw
        self.direction = LEFT
        
        
# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position) 


def setup_gemstone():
    # 작은 금
    small_gold = Gemstone(gemstone_images[0], (200, 380)) # 0번째 이미지를 좌표에 
    gemstone_group.add(small_gold) # 그룹에 추가
    
    # 큰 금
    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    
    # 다이아
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 420)))


pygame.init()
screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")
clock = pygame.time.Clock()

# 게임 관련 변수
default_offset_x_claw = 40 # 중심점 부터 집게까지의 거리
to_x = 0 # x좌표 기준으로 집게이미지를 이동시킬 변수

# 속도변수
move_speed = 12 # 발사할떄 스피드 (x좌표 기준)
return_speed = 20 # 아무것도 없이 돌아올때 스피드

# 방향변수
LEFT = -1
RIGHT = 1
STOP = 0

# 색깔 변수 
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_project_3/images/background.png")


# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아)
gemstone_images = [
    pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_project_3/images/small_gold.png"),
    pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_project_3/images/big_gold.png"),
    pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_project_3/images/stone.png"),
    pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_project_3/images/diamond.png")]

# 보석 그룹 만들기
gemstone_group = pygame.sprite.Group()
setup_gemstone()

# 집게
claw_image = pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_project_3/images/claw.png")
claw = Claw(claw_image, (screen_width // 2, 110))

running = True
while running:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN: # 마우스를 누를때
            claw.set_direction(STOP)
            to_x = move_speed
        
    # 집게 충돌처리(화면)
    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed
        
    if claw.offset.x < default_offset_x_claw: # 원위치에 오면
        to_x = 0
        claw.set__init__state() # 처음 상태로 되돌리기
    
    screen.blit(background, (0,0))
    
    gemstone_group.draw(screen) # group일때만 내장 함수 draw 쓸 수 있음
    claw.update(to_x)
    claw.draw(screen)
    
    pygame.display.update()
    
pygame.quit()