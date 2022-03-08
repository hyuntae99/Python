import pygame

pygame.init() # 초기화 (반드시 필요!!)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기 
# 1. 원하는 배경을 png파일로 저장 후 같은 폴더에 저장
# 2. 우클릭해서 경로를 복사
# 3. 경로를 아래 코드에 붙혀넣기 (\를 모두 /로 변환해야함!!!)
background = pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_Basic/Background.png")


# 이벤트 루프
running = True # 게임이 진행중인가?를 확인
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 진행중이 아님
    
    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 255, 0)) # RGB값으로 배경 그리기 가능
    
    pygame.display.update() # 게임화면을 다시 그리기! (계속 반복실행 되어야함!)

# 게임 종료
pygame.quit()