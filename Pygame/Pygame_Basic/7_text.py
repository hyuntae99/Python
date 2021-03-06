import pygame

pygame.init() # 초기화 (반드시 필요!!)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS
clock = pygame.time.Clock()


# 배경 이미지 불러오기 
# 1. 원하는 배경을 png파일로 저장 후 같은 폴더에 저장
# 2. 우클릭해서 경로를 복사
# 3. 경로를 아래 코드에 붙혀넣기 (\를 모두 /로 변환해야함!!!)
background = pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_Basic/Background.png")

# 캐릭터(스트라이프) 불러오기
character = pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_Basic/Character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
# 캐릭터의 크기도 고려해서 위치를 선정해야함!!!
character_x_pos = (screen_width / 2) - (character_width / 2)# 화면 가로의 절반크기에 위치
character_y_pos = screen_height - character_height # 화면 세로 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6


# 적 캐릭터 생성
enemy = pygame.image.load("C:/Users/조현태/OneDrive/바탕 화면/PythonWorkspace/Pygame_Basic/Enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1] 
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2)- (enemy_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

start_ticks = pygame.time.get_ticks() # 시작 시간

# 이벤트 루프
running = True # 게임이 진행중인가?를 확인
while running:
    dt = clock.tick(60) # 게임화면 초당 프레임 수
    print("fps : " + str(clock.get_fps())) # 초당 프레임 확인
    
# 캐릭터가 1초동안 100만큼 이동
# 10 fps : 1초 동안 1번에 10만큼 이동
# 20 fps : 1초동안 1번에 5만큼 이동!
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 진행중이 아님
            
        if event.type == pygame.KEYDOWN: # 키가 눌렀는지?
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래쪽으로
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                
    character_x_pos += to_x * dt # 프레임속도 조정을 위해 (* dt)
    character_y_pos += to_y * dt
    
    # 경계값 처리
    if character_x_pos < 0: # 왼쪽을 벗어날때
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 오른쪽을 벗어날때
        character_x_pos = screen_width - character_width
    elif character_y_pos < 0: # 위쪽을 벗어날때
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height: # 아래쪽을 벗어날때
        character_y_pos = screen_height - character_height
        
        
    # 충돌 처리를 위한 rect정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("출동했어요.")
        running = False
    
    
    screen.blit(background, (0, 0)) # 배경 그리기 (좌표기준으로 오른쪽 아래로)
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    
    # 타이머 
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간 계산
    # 경과 시간을 1000으로 나누어서 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # render (시간, True, 색상)
    screen.blit(timer, (10, 10))
    
    if total_time - elapsed_time <= 0:
        print("타임 아웃!")
        running = False

    pygame.display.update() # 게임화면을 다시 그리기! (계속 반복실행 되어야함!)

# 잠시 대기
pygame.time.delay(2000) # 2초 대기

# 게임 종료
pygame.quit()