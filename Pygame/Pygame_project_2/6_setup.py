import pygame
from random import *
import time

# 레벨에 맞게 설정
def setup(level):
    # 얼마동안 숫자를 보여줄 것인가?
    global display_time
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1) # 1보다 짧아져도 무조건 1까지
    
    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 3) + 5
    number_count = min(number_count, 10) # 20을 초과해도 20까지
    
    # 화면에 grid형태로 숫자 랜덤 배치
    shuffle_grid(number_count)
    
# 숫자 섞기
def shuffle_grid(number_count):
    rows = 5
    columns = 9
    
    cell_size = 130 # cell 별 가로, 세로 크기
    button_size = 110 # cell 안의 버튼의 크기
    screen_left_margin = 55 # 왼쪽 여백
    screen_top_margin = 20 # 위쪽 여백
    
    
    # [0,0,0,0,0,0,0,0]
    grid = [[0 for col in range(columns)]for row in range(rows)] # 5 X 9
    
    number = 1
    while number <= number_count:
        row_idx = randint(0,rows-1)
        col_idx = randint(0,columns-1)
        
        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1
            
            # 현재 geid cell 위치 기준으로 x,y 구함
            center_x = screen_left_margin + (col_idx * cell_size) +(cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) +(cell_size / 2)
            
            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)
            
            number_buttons.append(button)
            
    print(grid)


# 시작화면 표시 함수
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 동그라미, 중심좌표는 start_button의 중심좌표, 반지름 60, 굵기 5
    
    # 현재 레벨 표시
    msg = gmae_font.render(f"Level {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))

    screen.blit(msg, msg_rect)
    
    
# 게임 화면 표시 함수
def display_game_screen():
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 초단위로 변경
        msg = gmae_font1.render(str(int(display_time - elapsed_time)), True, (0,255,255))
        msg_rect = msg.get_rect(center=(45, 45))
        screen.blit(msg, msg_rect)
        
        if elapsed_time > display_time:
            hidden = True
    
    for idx, rect in enumerate(number_buttons, start = 1):
        if hidden: # 숨김 처리
            # 버튼 사각형 그리기
            pygame.draw.rect(screen, WHITE, rect)
        
        else:
            # 숫자 텍스트 만들기
            cell_text = gmae_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)
            
    
# pod에 해당하는 버튼 확인
def check_buttons(pos):
    global start, start_ticks
    
    if start: # 게임 시작했으면?
        check_number_buttons(pos)
            
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks() # 현재 시간 저장
        
def check_number_buttons(pos):
    global hidden, start, curr_level
    
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]: # 올바른 숫자 클릭할떄

                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                game_over()
            break
                
    if len(number_buttons) == 0: # 모든 숫자를 다 맞혔다면 다시 시작화면으로
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)
        
# 게임 종료 처리
def game_over():
    global running
    running = False
    msg = gmae_font.render("Game Over!", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2-60))
    msg1 = gmae_font.render(f"Your level is {curr_level}", True, WHITE)
    msg1_rect = msg.get_rect(center=(screen_width/2-30, screen_height/2+60))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)
    screen.blit(msg1, msg1_rect)
    

# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요!!)

# 화면 크기 설정
screen_width = 1280 # 가로 크기
screen_height = 700 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("MEMORY GAME") # 게임 이름
gmae_font = pygame.font.Font(None, 120)
gmae_font1 = pygame.font.Font(None, 90)


# 시작 버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

# 색깔 변수
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

number_buttons = [] # 버튼 관리 리스트
curr_level = 1
display_time = None
start_ticks = None

# 게임 시작 여부
start = False

# 숫자 숨김 여부
hidden = False

# 게임 시작 전 게임 설정 함수 
setup(curr_level)


# 게임 루프
running = True
while running:
    click_pos = None
    
    # 이벤트 루프
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos() # 클릭 좌표를 받음
            
    # 화면을 까맣게 칠함
    screen.fill(BLACK)
    
    if start:
        display_game_screen() # 게임 화면 표시
    else: 
        display_start_screen() # 시작 화면 표시
    
    
    # 사용자가 클릭한 좌표가 있다면 
    if click_pos:
        check_buttons(click_pos)
    
    # 화면 업데이트
    pygame.display.update()    

pygame.time.delay(2000)    

pygame.quit()