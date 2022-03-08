import pygame
import os

# 버블 클래스 
class Bubble(pygame.sprite.Sprite): # sprite를 사용해서 클래스 생성
    def __init__(self, image, color, position): # self를 쓰고 필요한 값들을 변수로 받는다.
        super().__init__() #super로 상속받아야함 -> sprite 사용했을때
        self.image = image
        self.color = color
        self.rect = image.get_rect(center=position) # get_rect()를 이용해서 이미지에서 rect값을 받아옴


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
        pygame.draw.circle(screen, (255,0,0), self.position, 3) # 중심 점 표시

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
    map = [ # 이중 리스트
        # ["R", "R", "Y", "Y", "B", "B", "G", "G"]
        list("RRYYBBGG"), # 위와 같은 코드임
        list("RRYYBBG/"), # / : 버블이 위치할 수 없는 곳
        list("BBGGRRYY"),
        list("BGGRRYY/"),
        list("........"), # . : 비어 있는 곳
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........")
    ]
    
    for row_idx, row in enumerate(map): # row : list(~~)
        for col_idx, col in enumerate(row): 
            if col in [".", "/"]: # . , /이면 그리기 않고 건너뛰기
                continue
            position = get_bubble_position(row_idx, col_idx) # 위치에 대한 함수
            image = get_bubble_image(col) # 색에 대한 함수
            
            # bubble = Bubble(image, col, position) # 버블 객체 생성
            # bubble_group.add(bubble) # 버블 그룹에 객체에 추가
            bubble_group.add(Bubble(image, col, position)) # 한줄 코드
            
    
    
# 세로(row_idx)와 가로(col_idx)를 입력받아서 게임화면의 position을 반환하는 함수
def get_bubble_position(row_idx, col_idx): 
    pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)
    if row_idx % 2 == 1: # 홀수일 경우
        pos_x += (CELL_SIZE // 2)
    return pos_x, pos_y
    
def get_bubble_image(color):
    if color == "R":
        return bubbl_images[0]
    elif color == "Y":
        return bubbl_images[1]
    elif color == "B":
        return bubbl_images[2]
    elif color == "G":
        return bubbl_images[3]
    elif color == "P":
        return bubbl_images[4]
    elif color == "B":
        return bubbl_images[-1] # 리스트의 맨마지막 값
    

pygame.init() # 게임을 만드려면 무조건 해야함
screen_width = 448
screen_height = 710
screen = pygame.display.set_mode((screen_width, screen_height)) # 스크린 만들기
pygame.display.set_caption("Puzzle Bobble") # 게임 이름
clock = pygame.time.Clock() # FPS

# 배경이미지 불러오기
current_path = os.path.dirname(__file__) # 실행하는 파일의 정보를 받아옴
image_path = os.path.join(current_path, "images") # image 파일 정보를 받아옴
background = pygame.image.load(os.path.join(image_path, "background.png")) # image 파일의 background.png를 가지고 옴

# 버블 이미지 불러오기 -> 다수의 이미지를 입력할때는 리스트를 사용!
# convert_alpha()를 사용하면 나중에 충돌처리할때 실제 이미지를 영역으로 충돌하게 할 수 있음
bubbl_images = [
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

to_angle_left = 0
to_angle_right = 0
angle_speed = 1.5 # 각도 증가량

map = [] # 맵
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
        
        if event.type == pygame.KEYUP: # 키보드를 누르지 않을때
            # 왼쪽 키보드, 오른쪽 키보드에서 손을 땠을때
            if event.key == pygame.K_LEFT:
                to_angle_left = 0 # 각도 유지
            elif event.key == pygame.K_RIGHT:
                to_angle_right = 0
            

    screen.blit(background, (0, 0)) # background를 screen에 (0,0) 그리기
    bubble_group.draw(screen) # bubble 그룹에 있는 모든 sprite를 screen에 그림
    # 왼쪽, 오른쪽 키를 누를때 딜레이 없애는 코드
    pointer.rotate(to_angle_left + to_angle_right) 
    pointer.draw(screen) # 그룹이 아니라서 draw를 쓸 수 없으므로 함수 만들기
    pygame.display.update() # 매순간 업데이트

pygame.quit() # 게임 종료