import pygame

# 시작화면 표시 함수
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 동그라미, 중심좌표는 start_button의 중심좌표, 반지름 60, 굻기 5

# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요!!)

# 화면 크기 설정
screen_width = 1280 # 가로 크기
screen_height = 700# 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("MEMORY GAME") # 게임 이름

# 시작 버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

# 색깔 변수
BLACK = (0,0,0)
WHITE = (255, 255, 255)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 화면을 까맣게 칠함
    screen.fill(BLACK)
        
    # 시작 화면
    display_start_screen()
    
    pygame.display.update()
    
    
pygame.quit()