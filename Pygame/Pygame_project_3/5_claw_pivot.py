import pygame

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.position = position
        self.offset = pygame.math.Vector2(default_offset_x_claw,0)
        
    
    def update(self): # 캐릭터 가만히 놔두면 숨쉬는 것 같은 동작을 해줌
        rect_center = self.offset + self.position
        self.rect = self.image.get_rect(center=rect_center)
        
        
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3) # 중심점 표시
           
        
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

# 색깔 변수 
RED = (255, 0, 0)

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
    
    screen.blit(background, (0,0))
    
    gemstone_group.draw(screen) # group일때만 내장 함수 draw 쓸 수 있음
    claw.update()
    claw.draw(screen)
    
    pygame.display.update()
    
pygame.quit()