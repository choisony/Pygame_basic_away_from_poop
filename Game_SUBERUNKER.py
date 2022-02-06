import pygame
import random
############################################################
############################################################
#기본 초기화( 반드시 해야하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("유빈이의 똥 피하기")

#fps
clock = pygame.time.Clock()
############################################################
############################################################

#1. 사용자 게임 초기화( 배경화면, 게임이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("background.png")

character = pygame.image.load("human.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height-character_height

to_x = 0
to_y = 0

character_speed = 0.5
enemy_speed = 7

enemy = pygame.image.load("poop.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0,screen_width-enemy_width)
enemy_y_pos = 0

running = True #게임이 진행중인가?
while running:
    dt = clock.tick(130) #게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key== pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x *dt
    enemy_y_pos  += enemy_speed

    ##가로경계값
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width -character_height

    if enemy_y_pos>screen_height:
        enemy_x_pos = random.randrange(0, screen_width - enemy_width)
        enemy_y_pos = 0

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기

pygame.quit()
