import pygame
import os
import random

pygame.init()

# 화면 크기 설정
screen_width = 1500 # 가로 크기
screen_height = 800 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Apple Game") # 게임 이름

# FPS
clock = pygame.time.Clock()


current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 폰트 설정
game_font = pygame.font.Font(None, 40)

# 타이머
total_time = 120
start_time = pygame.time.get_ticks()

# 점수
score = 0

# 사과 만들기
apple1 = pygame.image.load(os.path.join(image_path, "apple1.png"))
apple2 = pygame.image.load(os.path.join(image_path, "apple2.png"))
apple3 = pygame.image.load(os.path.join(image_path, "apple3.png"))
apple4 = pygame.image.load(os.path.join(image_path, "apple4.png"))
apple5 = pygame.image.load(os.path.join(image_path, "apple5.png"))
apple6 = pygame.image.load(os.path.join(image_path, "apple6.png"))
apple7 = pygame.image.load(os.path.join(image_path, "apple7.png"))
apple8 = pygame.image.load(os.path.join(image_path, "apple8.png"))
apple9 = pygame.image.load(os.path.join(image_path, "apple9.png"))

apple_sel1 = pygame.image.load(os.path.join(image_path, "apple_sel1.png"))
apple_sel2 = pygame.image.load(os.path.join(image_path, "apple_sel2.png"))
apple_sel3 = pygame.image.load(os.path.join(image_path, "apple_sel3.png"))
apple_sel4 = pygame.image.load(os.path.join(image_path, "apple_sel4.png"))
apple_sel5 = pygame.image.load(os.path.join(image_path, "apple_sel5.png"))
apple_sel6 = pygame.image.load(os.path.join(image_path, "apple_sel6.png"))
apple_sel7 = pygame.image.load(os.path.join(image_path, "apple_sel7.png"))
apple_sel8 = pygame.image.load(os.path.join(image_path, "apple_sel8.png"))
apple_sel9 = pygame.image.load(os.path.join(image_path, "apple_sel9.png"))

removed_apple = pygame.image.load(os.path.join(image_path, "removed_apple.png"))

 
apple_idxs= [apple1, apple2, apple3, apple4, apple5, apple6, apple7, apple8, apple9]
apple_sel_idxs=[apple_sel1, apple_sel2, apple_sel3, apple_sel4, apple_sel5, apple_sel6, apple_sel7, apple_sel8, apple_sel9]
 
apple_rects=[]

def creat_apple():
    apples = []
    for col in range(28):
        for row in range(14):
            x = col * 50 + 60
            y = row * 50 + 60
            number = random.randint(1, 9)
            apple = {
                "rect": pygame.Rect(x, y, 40, 40),
                "number": number,
                "selected": False,
                "remove" : False
            }
            apples.append(apple)
            apple_rect = apple['rect']
            apple_rects.append(apple_rect)
            
    return apples



def draw_apples(apples):
    for apple in apples:
        if apple['remove']:
            screen.blit(removed_apple, (apple['rect']))
        else:
            if apple['selected']:
                screen.blit(apple_sel_idxs[apple['number']-1],(apple['rect']))
            else:
                screen.blit(apple_idxs[apple['number']-1],(apple['rect']))


def remove_selected_apples(apples):
    sum = 0
    for apple in apples:
        if apple["selected"]:
            sum += apple["number"]
    if sum == 10:
        for idx in selected_idx:
            if apples[idx]["number"] == 0:
                continue
            apples[idx]['number'] = 0
            apples[idx]['remove'] = True
            global score 
            score += 1
    else:
        for idx in selected_idx:
                apples[idx]['selected'] = False

start = (0,0)
end = (0,0)
dSize = (0,0)
drawing = False

RED = (255,0,0)

running = True

apples= creat_apple()

screen.blit(background,(0,0))
draw_apples(apples)



while running:
    dt= clock.tick(120)
    
 # 2. 이벤트 처리 (마우스, 키보드 등)

    # 타이머 생성
    screen.blit(background,(0,0))
    draw_apples(apples)
    elapsed_time = (pygame.time.get_ticks()- start_time) /1000
    timer =  game_font.render("TIME : {}".format(int(total_time-elapsed_time)), True , (0,0,0))   # 출력 할 글자, True, 색상
    screen.blit(timer,(60,20))
    if (total_time-elapsed_time) <=0:
        game_result ="Time Over"
        running = False


    # 점수 생성
    record = game_font.render("SCORE : {}".format(int(score)), True, (0,0,0))
    screen.blit(record,(1300,20))

    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: 
            running = False 

        elif event.type == pygame.MOUSEBUTTONDOWN:
            start = event.pos
            dSize = 0,0
            drawing = True
            selected_idx=[]
            
        elif event.type == pygame.MOUSEBUTTONUP: 
            drawing = False
            remove_selected_apples(apples)
            screen.blit(background,(0,0))
            draw_apples(apples) 
            screen.blit(timer,(60,20))
            screen.blit(record,(1300,20))
            selected_apples = []
            
        elif event.type == pygame.MOUSEMOTION and drawing:
            end = event.pos
            dSize = end[0]-start[0], end[1]-start[1]
            screen.blit(background,(0,0))
            draw_apples(apples)  
            screen.blit(timer,(60,20))
            screen.blit(record,(1300,20))
            pygame.draw.rect(screen,RED,(start,dSize),2)
            rectangle_rect = pygame.Rect(start, dSize)
            for apple_rect in apple_rects:
              if rectangle_rect.colliderect(apple_rect):
                idx= apple_rects.index(apple_rect)
                apples[idx]['selected'] = True  
                selected_idx.append(idx)   
                selected_idx = list(set(selected_idx))
            
    

    pygame.display.update() 


msg = game_font.render(game_result, True , (0,0,0))
msg_rect = msg.get_rect(center = (int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
screen.blit(record,(int(screen_width/2 - 70), int(screen_height/2 + 10)))

pygame.display.update() 

pygame.time.delay(2000)

pygame.quit()
