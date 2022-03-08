import pygame

# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요!!)

# 화면 크기 설정
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("MEMORY GAME") # 게임 이름


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            running = False
            
pygame.quit()