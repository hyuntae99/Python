import os
import pygame
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

character = pygame.image.load(os.path.join(image_path, "character.png")).convert_alpha()
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

character_to_x = 0
character_speed = 0.5
 
weapon = pygame.image.load(os.path.join(image_path, "weapon.png")).convert_alpha()
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

# 무기는 한번에 여러 발 발사 가능
weapons = []
weapon_speed = 0.5


# 공 만들기
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "balloon2.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "balloon3.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "balloon4.png")).convert_alpha()]

# 공 크기에 따른 스피드 설정
ball_speed_y = [-15, -12, -9, -6]

# 각각의 공에 대한 정의
balls = []

balls.append({
    "pos_x" : 50, # 공의 x좌표
    "pos_y" : 50, # 공의 y좌표
    "img_idx" : 0, # 공의 이미지 인덱스
    "to_x" : 3, # 공의 x축 이동 방향
    "to_y" : -6, # 공의 y축 이동 방향
    "init_spd_y" : ball_speed_y[0]}) # y 최초 속도

# 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

# 폰트 정의
game_font = pygame.font.Font(None, 40)
total_time = 60
start_ticks = pygame.time.get_ticks()

# 게임 종료 메세지
game_result = "GAME OVER"



running = True # 게임이 진행중인가?를 확인
while running:
    dt = clock.tick(30) 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 진행중이 아님
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
                
  
            
    # 3. 게임 캐릭터 위치 정의    
    
    character_x_pos += character_to_x * dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 100, 200 -> 100, 190 -> 100, 180
    weapons = [[w[0], w[1] - (weapon_speed * dt)] for w in weapons]
    
    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]
    
    
    # 공 위치 정의 
    #enumerate -> 참조.py
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        
        # 가로 벽에 닿았을 떄 튕겨져서 나오게 하기
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] *= -1
            
        if ball_pos_y >= screen_height - stage_height  - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    
    # 4. 충돌 처리    
    
    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    # 공 rect 정보 업데이트
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        
        # 공과 캐릭터 충돌처리
        if character_rect.colliderect(ball_rect):
        # if pygame.sprite.collide_mask(character_rect, ball_rect): # 스프라이트 클래슥가 있어야지 사용가능!
            running = False
            break
        
        # 공과 무기 충돌처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]
            
            # 무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
            
            # 충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 해당 무기 없애기 값 설정 
                ball_to_remove = ball_idx # 해당 공 없애기 값 설정
                
                # 가장 작은 크기의 공이 아니라면 다음 단계 공으로 나누어주기
                if ball_img_idx < 3:
                    
                    # 현재 공 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]
                    
                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]
                    
                    # 왼쪽으로 튕겨져나가는 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y좌표
                        "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                        "to_x" : -3, # 공의 x축 이동 방향
                        "to_y" : -6, # 공의 y축 이동 방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]}) # y 최초 속도
                    
                    # 오른쪽으로 튕겨져나가는 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y좌표
                        "img_idx" :  ball_img_idx + 1, # 공의 이미지 인덱스
                        "to_x" : 3, # 공의 x축 이동 방향 
                        "to_y" : -6, # 공의 y축 이동 방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]}) # y 최초 속도
                break
        # 계속 게임 진행
        else :
            continue # 안쪽 for문 조건이 맞지않으면 continue. 바깥은 계속 함
        break # 안쪽 for문에서 break를 만나면 여기로 진입.
               
    # 충돌된 공, 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    
    if len(balls) == 0:
        game_result = "MISSION COMPLETE"
        runnung = False
        break 
    
    
    # 5. 화면에 그리기 - 앞에 실행되는 것이 가려짐
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]  
        ball_pos_y = val["pos_y"] 
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
        
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("TIME : {}" .format(int(total_time - elapsed_time)), True, (0, 255, 255))
    screen.blit(timer, (10, 10))
    
    if total_time - elapsed_time <= 0:
        game_result = "TIME OVER"
        running = False
        
 
    # 6. 계속 업데이트 해야함!
    pygame.display.update() # 게임화면을 다시 그리기! (계속 반복실행 되어야함!)

# 게임 오버 메세지
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()


pygame.time.delay(1000)

# 게임 종료
pygame.quit()