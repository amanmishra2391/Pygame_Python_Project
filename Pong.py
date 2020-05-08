import pygame,sys
pygame.init()
clock = pygame.time.Clock()
Screen=pygame.display.set_mode((600,401))
pygame.display.set_caption("Pong")
Red=(255,0,0)
Black=(0,0,0)
White=(255,255,255)
Green=(0,255,0)
Blue=(0,0,255)
x=250
X=0
y=380
b_x=50
b_y=50
b_X=5
b_Y=5
score=0
def Quit():
    pygame.quit()
    sys.exit(0)
def drawrect(Screen,a,b):
    if a<0:
        a=0
    if a>499:
        a=499
    pygame.draw.rect(Screen,Blue,[a,b,100,20])
Gameover=False
font=pygame.font.SysFont(None,25)
def message():
    Screen.blit(font.render("Game Over.", True, Green), [250, 200])
    Screen.blit(font.render(("Your score is "+str(score)), True, Green), [250, 220])
    Screen.blit(font.render(" Press any key to continue", True, Green), [250, 240])
def Score():
    string="Score: "+str(score)
    text=font.render(string,True,White)
    Screen.blit(text,[500,50])
while not Gameover:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Gameover=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                Gameover=True
                Quit()
            if event.key==pygame.K_LEFT:
                x -= 5
            if event.key==pygame.K_RIGHT:
                x += 5
    Screen.fill(Black)
    drawrect(Screen,x,y)
    pygame.draw.rect(Screen,Red,[b_x,b_y,10,10])
    Score()
    if b_y+10>=y and x+90>=b_x>=x:
        score+=1
        b_Y=-5
    if b_y+10>=400:
        score=0
        Gameover=True
    if b_y==0:
        b_Y=5
    if b_x==0:
        b_X=5
    elif b_x+10>=599:
        b_X=-5
    b_x+=b_X
    b_y+=b_Y
    pygame.display.update()
    if b_Y<0:
        clock.tick(20)
    else :
        clock.tick(5)
message()
pygame.display.update()
key=True
while key:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            key=False
pygame.quit()
quit()