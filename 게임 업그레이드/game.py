import os
import pygame

class Charter(pygame.sprite.Sprite):
    def __init__(self, image, size, width, height, x_pos, y_pos):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=(x_pos, y_pos))
        self.size = size
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        

class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)



#########################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요!!)

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
#########################################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트, 속도)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 변환!
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

background = pygame.image.load(os.path.join(image_path, "background.png"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이 위에 캐릭터를 두기 위해서

character_image = pygame.image.load(os.path.join(image_path, "character.png")).convert_alpha()
character_size = character_image.get_rect().size
character = Charter(character_image, character_size, character_size[0], character_size[1], \
    screen_width / 2 - (character_size[0] / 2), screen_height - character_size[1] - stage_height)


ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "balloon2.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "balloon3.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "balloon4.png")).convert_alpha()
]





running = True # 게임이 진행중인가?를 확인
while running:

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 진행중이 아님
  
  
            
    # 3. 게임 캐릭터 위치 정의    

        
    # 4. 충돌 처리    

    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
 
 
    # 6. 계속 업데이트 해야함!
    pygame.display.update() # 게임화면을 다시 그리기! (계속 반복실행 되어야함!)


# 게임 종료
pygame.quit()