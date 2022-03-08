import pygame
import os, random, math

# 버블 클래스 
class Bubble(pygame.sprite.Sprite): # sprite를 사용해서 클래스 생성
    def __init__(self, image, color, position=(0,0), row_idx=-1, col_idx=-1): # self를 쓰고 필요한 값들을 변수로 받는다.
        super().__init__() #super로 상속받아야함 -> sprite 사용했을때
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position) # get_rect()를 이용해서 이미지에서 rect값을 받아옴
        self.radius = 18 # 공의 속도조절
        self.row_idx = row_idx
        self.col_idx = col_idx
        
    def set_rect(self, position):
        self.rect = self.image.get_rect(center=position)
      
    def draw(self, screen, to_x=None):
        if to_x: # to_x가 있으면
            screen.blit(self.image, (self.rect.x + to_x, self.rect.y))
        else:
            screen.blit(self.image, self.rect) 
        
    def set_angle(self, angle):
        self.angle = angle
        self.rad_angle = math.radians(self.angle) # 각도를 호도법으로 변환
    
    def move(self):
        to_x = self.radius * math.cos(self.rad_angle) # x = r cos a
        to_y = self.radius * math.sin(self.rad_angle) * -1 # 파이게임 좌표특성을 생각해서 -1곱하기
        
        self.rect.x += to_x
        self.rect.y += to_y
        
        # 경계를 벗어나면 튕겨나가기
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.set_angle(180 - self.angle) # 같은 각도로 다른 방향
        

    def set_map_index(self, row_idx, col_idx):
        self.row_idx = row_idx
        self.col_idx = col_idx
        
        
    def drop_downward(self, height):
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery + height))
        
        
# 발사대 클래스
class Pointer(pygame.sprite.Sprite): 
    def __init__(self, image, position, angle): 
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.angle = angle
        self.original_image = image
        self.position = position
    
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        # pygame.draw.circle(screen, (255,0,0), self.position, 3) # 중심 점 표시

    def rotate(self, angle):
        self.angle += angle # 원래 각도에 각도 변화를 줌
        
        # 최대, 최소 각도 조정
        if self.angle > 170:
            self.angle = 170
        elif self.angle < 10:
            self.angle = 10
            
        # 이미지 회전 (원본이미지를 이용해야 제대로 회전함)
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1) 
        self.rect = self.image.get_rect(center=self.position) # 회전한 포인트에 대한 rect정보 업데이트
        

# 맵 만들기
def setup():
    global map # 전역 공간의 map을 사용하기 위해서
    
    # 레벨 1
    map = [ # 이중 리스트
        # ["R", "R", "Y", "Y", "B", "B", "G", "G"]
        list("RRYYBBGG"), # 위와 같은 코드임
        list("RRYYBBG/"), # / : 버블이 위치할 수 없는 곳
        list("BBGGRRYY"),
        list("BGGRRYY/"),
        list("YYBBGGGR"), # . : 비어 있는 곳
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........")
    ]
    
    # # 레벨 2
    # map = [
	#     list("...YY..."),
	#     list("...G.../"),
	#     list("...R...."),
	#     list("...B.../"),
	#     list("...R...."),
	#     list("...G.../"),
	#     list("...P...."),
	#     list("...P.../"),
	#     list("........"),
	#     list("......./"),
	#     list("........")
    # ]    

    # # 레벨 3
    # map = [
	#     list("G......G"),
	#     list("RGBYRGB/"),
	#     list("Y......Y"),
	#     list("BYRGBYR/"),
	#     list("...R...."),
	#     list("...G.../"),
	#     list("...R...."),
	#     list("......./"),
	#     list("........"),
	#     list("......./"),
	#     list("........")    
    # ]
    
    
    for row_idx, row in enumerate(map): # row : list(~~)
        for col_idx, col in enumerate(row): 
            if col in [".", "/"]: # . , /이면 그리기 않고 건너뛰기
                continue
            position = get_bubble_position(row_idx, col_idx) # 위치에 대한 함수
            image = get_bubble_image(col) # 색에 대한 함수
            
            # bubble = Bubble(image, col, position) # 버블 객체 생성
            # bubble_group.add(bubble) # 버블 그룹에 객체에 추가
            bubble_group.add(Bubble(image, col, position, row_idx, col_idx)) # 한줄 코드
            
    
    
# 세로(row_idx)와 가로(col_idx)를 입력받아서 게임화면의 position을 반환하는 함수
def get_bubble_position(row_idx, col_idx): 
    pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2) 
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2) + wall_height
    if row_idx % 2 == 1: # 세로가 홀수일 경우
        pos_x += (CELL_SIZE // 2)
    return pos_x, pos_y
    
def get_bubble_image(color):
    if color == "R":
        return bubble_images[0]
    elif color == "Y":
        return bubble_images[1]
    elif color == "B":
        return bubble_images[2]
    elif color == "G":
        return bubble_images[3]
    elif color == "P":
        return bubble_images[4]
    elif color == "B":
        return bubble_images[-1] # 리스트의 맨마지막 값


def prepare_bubbles():
    global curr_bubble, next_bubble
    if next_bubble: # 있으면 
        curr_bubble = next_bubble # 다음버블에 현재버블을 넣기
    else: # 없으면   
        curr_bubble = create_bubble() # 새 버블 만들기
        
    curr_bubble.set_rect((screen_width // 2, 624))
    next_bubble = create_bubble()
    next_bubble.set_rect((screen_width // 4, 678))


def create_bubble():
    color = get_ramdom_bubble_color()
    image = get_bubble_image(color)
    return Bubble(image, color)


def get_ramdom_bubble_color():
    # 현재 맵에 있는 색깔 내에만 버블 생성
    colors = []
    # 전체 맵 순회
    for row in map:
        for col in row:
            # 나오지 않은 색깔이거나 비어있는 버블인 경우에는 추가 X
            if col not in colors and col not in [".", "/"]:
                colors.append(col)
    return random.choice(colors) # 리스트에 있는 것중 하나 뽑는 함수


def process_collsion():
    global curr_bubble, fire, curr_fire_count
    # 현재 버블과 버블 그룹사이에 충돌한 것이 있으면
    hit_bubble = pygame.sprite.spritecollideany(curr_bubble, bubble_group, pygame.sprite.collide_mask) 
    # 버블이 충돌했거나 천장에 닿았을때
    if hit_bubble or curr_bubble.rect.top <= wall_height:
        row_idx, col_idx = get_map_index(*curr_bubble.rect.center) #(x, y) 튜플형태를 언패키징
        place_bublle(curr_bubble, row_idx, col_idx)
        # 같은 색깔이 3개이상 있으면 제거
        remove_adjacent_bubbles(row_idx, col_idx, curr_bubble.color)
        
        # 달라붙었기때문에 새로운 버블 발사하도록 설정  
        curr_bubble = None 
        fire = False
        curr_fire_count -= 1 # 기회 1번 감소
    
    
def get_map_index(x, y):
    row_idx = (y - wall_height) // CELL_SIZE
    col_idx = x // CELL_SIZE
    if row_idx % 2 == 1: # 세로가 홀수번째 일때
        col_idx = (x - (CELL_SIZE // 2)) // CELL_SIZE
        if col_idx < 0: # 왼쪽으로 살짝 벗어났을때
            col_idx = 0
        elif col_idx > MAP_COLUMN_COUNT - 2: # 오른쪽으로 벗어났을때
            col_idx = MAP_COLUMN_COUNT - 2
    return row_idx, col_idx


def place_bublle(bubble, row_idx, col_idx):
    map[row_idx][col_idx] = bubble.color # 충돌계산위치에 충돌한 버블 색깔 대입
    position = get_bubble_position(row_idx, col_idx) # 버블의 위치를 좌표로 계산함
    bubble.set_rect(position) # 버블 위치 업데이트
    bubble.set_map_index(row_idx, col_idx)
    bubble_group.add(bubble)
    

def remove_adjacent_bubbles(row_idx, col_idx, color):
    visited.clear() # 리스트 비우기
    visit(row_idx, col_idx, color)
    if len(visited) >= 3: # 같은 색상이 3개 이상있으면
        remove_visited_bubbles()
        remove_hanging_bubbles()
    

# 방문처리 (DFS알고리즘)
def visit(row_idx, col_idx, color=None): # 변수를 직접 설정하면 함수를 사용할때 해당 변수가 없어도 실행가능!
    # 맵의 범위를 벗어나는지 확인
    if row_idx < 0 or row_idx >= MAP_ROW_COUNT or col_idx < 0 or col_idx >= MAP_COLUMN_COUNT:
        return 
    # 현재 cell의 색상이 같은 색상의 버블인지 확인
    if color and map[row_idx][col_idx] != color: # color 값이 있어야만 실행
        return
    # 빈 공간이거나 버블이 존재할 수 없는 공간인지 확인
    if map[row_idx][col_idx] in [".", "/"]:
        return
    # 방문한 곳인지 확인
    if (row_idx, col_idx) in visited:
        return
    # 방문처리 등록
    visited.append((row_idx, col_idx))
    
    # 현재위치에서 움직일 수 있는 방법들
    rows = [0, -1, -1, 0 ,1 ,1] # 세로
    cols = [-1, -1, 0, 1, 0, -1] # 가로
    
    if row_idx % 2 == 1: # 세로가 홀수 일때 -> 오른쪽으로 절반만큼 이동했기때문에
        rows = [0, -1, -1, 0, 1, 1]
        cols = [-1, 0, 1, 1, 1, 0]
        
    # 재귀함수 이용!
    for i in range(len(rows)):
        visit(row_idx + rows[i], col_idx + cols[i], color)


def remove_visited_bubbles():
    bubbles_to_remove = [b for b in bubble_group if (b.row_idx, b.col_idx) in visited]
    for bubble in bubbles_to_remove:
        map[bubble.row_idx][bubble.col_idx] = "." # 지우고 "."으로 초기화
        bubble_group.remove(bubble)
        
def remove_not_visited_bubbles():
    bubbles_to_remove = [b for b in bubble_group if (b.row_idx, b.col_idx) not in visited]
    for bubble in bubbles_to_remove:
        map[bubble.row_idx][bubble.col_idx] = "."
        bubble_group.remove(bubble)

     
def remove_hanging_bubbles():
    visited.clear()
    for col_idx in range(MAP_COLUMN_COUNT):
        if map[0][col_idx] != ".": # 천장에 붙어있는 모든 경우
            visit(0, col_idx)
    remove_not_visited_bubbles()


def draw_bubbles():
    to_x = None
    if curr_fire_count == 2:
        to_x = random.randint(0, 2) - 1 # -1 ~ 1사이의 값
    elif curr_fire_count == 1:
        to_x = random.randint(0, 8) - 4 # -4 ~ 4사이의 값    
    
    for bubble in bubble_group:
        bubble.draw(screen, to_x)
        

def drop_wall():
    global wall_height, curr_fire_count
    wall_height += CELL_SIZE # 떨어질때마다 버블크기만큼
    for bubble in bubble_group:
        bubble.drop_downward(CELL_SIZE)
    curr_fire_count = FIRE_COUNT
    

def get_lowest_bubble_bottom():
    bubble_bottoms = [bubble.rect.bottom for bubble in bubble_group]
    return max(bubble_bottoms) # 최대값
    
    
def chage_bubble_image(image):
    for bubble in bubble_group:
        bubble.image = image # 모든 버블들은 받은 이미지로 변경
        
        
def display_game_over():
    txt_game_over = game_font.render(game_result, True, (255, 255, 255))
    rect_game_over = txt_game_over.get_rect(center=(screen_width//2, screen_height//2))
    screen.blit(txt_game_over, rect_game_over)
    
    
pygame.init() # 게임을 만드려면 무조건 해야함
screen_width = 448
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) # 스크린 만들기
pygame.display.set_caption("Puzzle Bubble") # 게임 이름
clock = pygame.time.Clock() # FPS

# 배경이미지 불러오기
current_path = os.path.dirname(__file__) # 실행하는 파일의 정보를 받아옴
image_path = os.path.join(current_path, "images") # image 파일 정보를 받아옴
background = pygame.image.load(os.path.join(image_path, "background.png")) # image 파일의 background.png를 가지고 옴
wall =  pygame.image.load(os.path.join(image_path, "wall.png"))


# 버블 이미지 불러오기 -> 다수의 이미지를 입력할때는 리스트를 사용!
# convert_alpha()를 사용하면 나중에 충돌처리할때 실제 이미지를 영역으로 충돌하게 할 수 있음
bubble_images = [
    pygame.image.load(os.path.join(image_path, "red.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "yellow.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "blue.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "green.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "pupple.png")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "black.png")).convert_alpha()
]

# 발사대 이미지 불러오기
pointer_image = pygame.image.load(os.path.join(image_path, "pointer.png"))
pointer = Pointer(pointer_image, (screen_width//2, 624), 90) # 최초 각도


# 게임 관련 변수
CELL_SIZE = 56 # 리스트로 만든 cell의 크기
BUBBLE_WIDTH = 56 # 버블의 가로
BUBBLE_HEIGHT = 62 # 버블의 세로
MAP_ROW_COUNT = 11 # 세로 최대 길이
MAP_COLUMN_COUNT = 8 # 가로 최대길이
FIRE_COUNT = 5 # 발사 기회

to_angle_left = 0
to_angle_right = 0
angle_speed = 1.5 # 각도 증가량

curr_bubble = None # 이번에 쏠 버블
next_bubble = None # 다음에 쏠 버블
fire = False # 발사 여부 -> False : 발사 가능상태
curr_fire_count = FIRE_COUNT
wall_height = 0 # 화면에 보여지는 벽의 높이

is_game_over = False
game_font = pygame.font.SysFont("arialrounded", 40)
game_result = None


map = [] # 맵
visited = [] # 방문여부기록용 리스트
bubble_group = pygame.sprite.Group() # 버블 그룹 생성

setup() # 맵 만들기 함수 실행

running = True
while running:
    clock.tick(60) # fps 60으로 설정
    
    for event in pygame.event.get(): # 이벤트 변수
        if event.type == pygame.QUIT: # 창을 닫을때
            running = False
        if event.type == pygame.KEYDOWN: # 키보드를 누를때
            if event.key == pygame.K_LEFT: # 키보드 왼쪽을 누를때
                to_angle_left += angle_speed # 각도가 증가
            elif event.key == pygame.K_RIGHT:
                to_angle_right -= angle_speed # 각도가 감소
            elif event.key == pygame.K_SPACE:
                if curr_bubble and not fire:
                    fire = True
                    curr_bubble.set_angle(pointer.angle)
        
        if event.type == pygame.KEYUP: # 키보드를 누르지 않을때
            # 왼쪽 키보드, 오른쪽 키보드에서 손을 땠을때
            if event.key == pygame.K_LEFT:
                to_angle_left = 0 # 각도 유지
            elif event.key == pygame.K_RIGHT:
                to_angle_right = 0
            

    if not curr_bubble:
        prepare_bubbles()
        
    if fire:
        process_collsion() #충돌처리 함수
        
    if curr_fire_count == 0:
        drop_wall()
        
    if not bubble_group: # 버블 그룹이 없으면
        game_result = "Mission Complete!"
        is_game_over = True
    elif get_lowest_bubble_bottom() > (len(map) * CELL_SIZE):
        game_result = "Game Over!"
        is_game_over = True
        chage_bubble_image(bubble_images[-1])
        
        
    screen.blit(background, (0, 0)) # background를 screen에 (0,0) 그리기
    screen.blit(wall, (0, wall_height - screen_height))
    
    #bubble_group.draw(screen) # bubble 그룹에 있는 모든 sprite를 screen에 그림
    draw_bubbles()
    
    # 왼쪽, 오른쪽 키를 누를때 딜레이 없애는 코드
    pointer.rotate(to_angle_left + to_angle_right) 
    pointer.draw(screen) # 그룹이 아니라서 draw를 쓸 수 없으므로 함수 만들기
    if curr_bubble:
        if fire: # 발사중이면
            curr_bubble.move() # 함수를 통해 이동시켜주고
        curr_bubble.draw(screen) # 그리기
    
    if next_bubble:
        next_bubble.draw(screen)  
    
    if is_game_over:
        display_game_over()
        running = False
    
    pygame.display.update() # 매순간 업데이트
    
pygame.time.delay(1500)
pygame.quit() # 게임 종료 