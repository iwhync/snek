import pygame
import time
import random
import winsound
from pygame import mixer
import time
from time import sleep

mymixer = pygame.mixer
mymixer.init()
mysound = mymixer.Sound("snemm.wav")
mysound.play(-1)

pygame.init()

freq = 500
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (130, 10, 110)
ran1 = (111,1,56)
ran2 = (50,130,200)
ran3 = (31,70,1)

dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Shit Snake")
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 13
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
            
  
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            mysound.stop()
            dis.fill(red)
            message("You Suck. C to try again, Q to quit", yellow)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        mysound.play(-1)
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        
        if Length_of_snake % 4 == 0:
            dis.fill(ran2)
        if Length_of_snake % 5 == 0:
            dis.fill(ran3)
        if Length_of_snake % 7 == 0:
            dis.fill(ran1)
        
        
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        if Length_of_snake % 3 == 0:
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        if Length_of_snake % 4 == 0:
            pygame.draw.rect(dis, purple, [foodx, foody, snake_block, snake_block])
        if Length_of_snake % 5 == 0:
            pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
        if Length_of_snake % 7 == 0:
            pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])  
            
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            winsound.Beep(500,50)
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 3

 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
