import pygame,sys,random
pygame.init()
black=(100,0,0)
white=(255,255,255)
red=(255,0,0)
window_width=600
window_height=400
Screen=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake")
pygame.display.get_surface()
font=pygame.font.SysFont(None,25,bold=True)

def Quit():
    pygame.quit()
    sys.exit(0)

clock=pygame.time.Clock()
FPS=5
blockSize=20
noPixel=0

def snake(blockSize, snakelist):
    for size in snakelist:
        pygame.draw.rect(Screen, black,[size[0]+5,size[1],blockSize,blockSize],2)

def message(msg,color):
    text=font.render(msg,True,color)
    Screen.blit(text,[200,100])

def gameLoop():
    gameExit=False
    gameOver=False
    x=200
    y=100
    snakelist=[]
    snakelength=1
    randomAppleX = round(random.randrange(0, window_width - blockSize) // 10) * 10
    randomAppleY = round(random.randrange(0, window_height - blockSize) // 10) * 10
    global X,Y
    X=0
    Y=0
    while not gameExit:
        while gameOver:
            Screen.fill(white)
            message("Game over, press c to play again or q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=False
                    gameExit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameOver=False
                        gameExit=True
                    if event.key==pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    Quit()
                left=event.key==pygame.K_LEFT
                right=event.key==pygame.K_RIGHT
                up=event.key==pygame.K_UP
                down=event.key==pygame.K_DOWN
                if left:
                    X=-blockSize
                    Y=noPixel
                elif right:
                    X=blockSize
                    Y=noPixel
                elif up:
                    X=noPixel
                    Y=-blockSize
                elif down:
                    X=noPixel
                    Y=blockSize
            if x>=window_width or x<0 or y>=window_height or y<0:
                gameOver=True
        x+=X
        y+=Y
        Screen.fill(white)
        Apple=20
        pygame.draw.rect(Screen, red, [randomAppleX, randomAppleY, Apple, Apple])
        snakelist.append([x,y])
        if len(snakelist)>snakelength:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment==[x,y]:
                gameOver=True
        snake(blockSize,snakelist)
        pygame.display.update()
        if (randomAppleX + Apple)>=x >= randomAppleX:
            if (randomAppleY + Apple)>=y >= randomAppleY:
                randomAppleX = round(random.randrange(0, window_width - blockSize) / 10.0) * 10.0
                randomAppleY = round(random.randrange(0, window_height - blockSize) / 10.0) * 10.0
                snakelength += 1
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()