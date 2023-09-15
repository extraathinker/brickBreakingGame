import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Brick Breaking')

box = pygame.image.load('holder.png')
box = pygame.transform.scale(box,(box.get_width()*2,box.get_height()))
boxX = 0
boxY = 450

ball = pygame.image.load('001-football.png')
ballX = 0
ballY = 442
ballXChange = 0
ballYChange = 0
state = 'ready'

brickImg = pygame.image.load('003-cell.png')
bricks = {}
brick = {}
def layer(rowNum):
    global brick,bricks
    numBricks = random.randint(2,20)
    posX = random.randint(0,400)
    for ab in range(rowNum):
        a = 0
        for i in range(numBricks):
            if posX + a > 700 or posX + a < 0:
                continue
            else:
                brick[i] = [posX + a, ab * 20]
                a += 60
        bricks[ab] = brick

layer(2)
print(bricks)
running = True
while running:
    
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            mx, my = pygame.mouse.get_pos()
            boxX = mx - 60
            if state == 'ready':
                ballX = mx - 10


        if event.type == pygame.MOUSEBUTTONDOWN:
            state = 'fire'
            ballXChange = 0.1
            ballYChange = -0.1

    if ballX > 775 and state == 'fire':
        ballXChange = -0.1
    elif ballX < 5 and state == 'fire':
        ballXChange = 0.1
    elif ballY < 5 and state == 'fire':
        ballYChange = 0.1
    elif abs(boxY - ballY) < 5 and abs(ballX - boxX) < 20 and state == 'fire':
        ballYChange = -0.1
    
    if ballY > 500:
        exit()


    ballX += ballXChange
    ballY += ballYChange
    screen.blit(box,(boxX,boxY))
    screen.blit(ball,(ballX,ballY ))
    for m in bricks.keys():
        for n in bricks[m]:
            screen.blit(brickImg,(bricks[m][n][0],bricks[m][n][1]))
            box11 = pygame.Rect(bricks[m][n][0],bricks[m][n][1],brickImg.get_width(),brickImg.get_height())
            if box11.collidepoint(ballX,ballY):
                pass
    pygame.display.update()