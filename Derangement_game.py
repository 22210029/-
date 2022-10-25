#Derangement_game.py
import pygame
a=0
ans=0

def f(n): #구하고자 하는 경우의 수 계산
    if n==1: #f(1)의 값=0
        return 0
    if n==2: #f(2)의 값=1
        return 1
    else:
        a,b=f(n-1), f(n-2)
        return (n-1)*(a+b)

pygame.init() #초기화
SCREEN_WIDTH=600
SCREEN_HEIGHT=600
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(20,60,120)

pygame.display.set_caption("Derangement")

robot=pygame.image.load("C:/Users/조인혜/Desktop/수학 주제 탐구/muchine_1.png")
robot_size = robot.get_rect().size
robot_width, robot_height = robot_size[0], robot_size[1]
robot_x_pos, robot_y_pos = (SCREEN_WIDTH/2)-(robot_width/2), SCREEN_HEIGHT/2-robot_height/2


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창을 닫는 이벤트가 발생했는가?
            running = False
        keys=pygame.key.get_pressed()

        if keys[pygame.K_0]:
            a=0
        if keys[pygame.K_1]:
            a=1
        if keys[pygame.K_2]:
            a=2
        if keys[pygame.K_3]:
            a=3
        if keys[pygame.K_4]:
            a=4
        if keys[pygame.K_5]:
            a=5
        if keys[pygame.K_6]:
            a=6
        if keys[pygame.K_7]:
            a=7
        if keys[pygame.K_8]:
            a=8
        if keys[pygame.K_9]:
            a=9
        if keys[pygame.K_PERIOD]:
            ans=f(a)

    font=pygame.font.SysFont('Gulim', 30, False, False)	
    if ans==0:
        text= font.render(str("사람의 수를 입력하시오."), True, BLACK, WHITE)
        text_size = text.get_rect().size
        text_width, text_height = text_size[0], text_size[1]
        text_x, text_y = (SCREEN_WIDTH/2)-(text_width/2), robot_y_pos-text_height/2-30


    else:
        text= font.render(str(ans), True, BLACK, WHITE)
        text_size = text.get_rect().size
        text_width, text_height = text_size[0], text_size[1]
        text_x, text_y = (SCREEN_WIDTH/2)-(text_width/2), robot_y_pos-text_height/2-30

    screen.fill(WHITE)    
    screen.blit(robot, (robot_x_pos,robot_y_pos))
    screen.blit(text, (text_x, text_y))
    
    pygame.display.update()






#종료
pygame.quit()


