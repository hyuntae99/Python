import pygame

pygame.init() # 게임을 만드려면 무조건 해야함
screen_width = 448
screen_height = 710
screen = pygame.display.set_mode((screen_width, screen_height)) # 스크린 만들기
pygame.display.set_caption("Puzzle Bobble") # 게임 이름
clock = pygame.time.Clock() # FPS

running = True
while running:
    clock.tick(60) # fps 60으로 설정
    
    for event in pygame.event.get(): # 이벤트 변수
        if event.type == pygame.QUIT: # 창을 닫을때
            running = False
            

pygame.quit() # 게임 종료