import pygame
import time
import random


while True:
    
    pygame.init()
    
    white=(255,255,255)
    blue=(0,0,200)
    black=(0,0,0)
    yellow=(255,255,0)
    red=(255,0,0)
    pink=(255,105,180)
    grey=(169,169,169)
    silver=(192,192,192)
    triassic=(129,43,146)
    
    display_width=800
    display_height=600

    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('CONFUSION')
    bg1=pygame.image.load("bg1.jpg").convert_alpha()
    gameexit=False
    ball_x=display_width/2
    ball_y=display_height/2
    display_width=display_width-10
    display_height=display_height-10
    
    x_coordinate=0
    y_coordinate=0

    clock=pygame.time.Clock()

    block_size=5
    FPS=50
    font=pygame.font.SysFont(None, 80)
    
    def title(msg,color):
        screen_text=font.render(msg,True,color)
        gameDisplay.blit(screen_text,[100,250])

    gameDisplay.fill(black)
    gameDisplay.blit(bg1, (32,79))
    pygame.display.flip()
    pygame.display.update()
    title("^ CoNfUsIOn ^ ",yellow)
    pygame.display.update()
    time.sleep(3)
    font=pygame.font.SysFont("Arial", 50)
    def msg1(msg,color):
        screen_text=font.render(msg,True,color)
        gameDisplay.blit(screen_text,[120,300])
    def timer(msg,color):
        screen_text=font.render(msg,True,color)
        gameDisplay.blit(screen_text,[350,250])
        
    start=pygame.image.load("name.jpg").convert_alpha()
    gameDisplay.fill(black)
    gameDisplay.blit(start, (0,0))
    pygame.display.flip()
    
    pygame.display.update()
    time.sleep(2)
    
    gameDisplay.fill(black)
    msg1("GAME STARTS IN 3 SECONDS",yellow)
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)
    timer("** 3 **",red)
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)
    timer("** 2 **",red)
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)
    timer("** 1 **",red)
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)

    x=time.time()
    background_image=pygame.image.load("back.jpg").convert()
    water=pygame.image.load("water.jpg").convert_alpha()
    pygame.mixer.music.load("Laser.wav")
    x1=100
    y1=120
    x2=600
    y2=420
    x3=150
    y3=330
    while not gameexit:
        
        for event in pygame.event.get():
            if(pygame.time.get_ticks()%15==0):
                x1=random.randint(100,650)
                x2=random.randint(100,650)
                x3=random.randint(100,650)
                y1=random.randint(100,450)
                y2=random.randint(100,450)
                y3=random.randint(100,450)
                FPS=FPS+15
            if event.type==pygame.QUIT :
                gameexit=True
            if event.type==pygame.KEYDOWN:

                pygame.mixer.music.play()
                if event.key==pygame.K_LEFT:
                    x_coordinate=-block_size
                    y_coordinate=0
                elif event.key==pygame.K_RIGHT:
                    x_coordinate=block_size
                    y_coordinate=0
                elif event.key==pygame.K_UP:
                    x_coordinate=0
                    y_coordinate=-block_size
                elif event.key==pygame.K_DOWN:
                    x_coordinate=0
                    y_coordinate=block_size  
        if ball_x>=785 or ball_x<10 or ball_y>=585 or ball_y<10 or ((ball_x in range(x1,x1+80))and (ball_y in range(y1,y1+50))) or ((ball_x in range(x2,x2+80))and (ball_y in range(y2,y2+50)))or ((ball_x in range(x3,x3+80)) and (ball_y in range(y3,y3+50))) :
            gameexit=True
            time.sleep(1)
            y=time.time()
            
        gameDisplay.blit(background_image,[0, 0])
        gameDisplay.blit(water,[x1,y1])
        gameDisplay.blit(water,[x2,y2])
        gameDisplay.blit(water,[x3,y3])
        ball_x+=x_coordinate
        ball_y+=y_coordinate
        pygame.draw.rect(gameDisplay,blue,[0,0,800,10])
        pygame.draw.rect(gameDisplay,blue,[0,590,800,10])
        pygame.draw.rect(gameDisplay,blue,[0,790,10,-800])
        pygame.draw.rect(gameDisplay,blue,[790,5,10,800])
    
        pygame.draw.circle(gameDisplay,silver,(int(ball_x),int(ball_y)),8)
        pygame.display.update()
        
        clock.tick(FPS)
    time1=y-x
    time1=str(time1)
    
    gameDisplay.fill(black)
    msg1("YOU SURVIVED: "+time1[:4]+" seconds",silver)
    pygame.display.update()
    time.sleep(2)
    gameDisplay.fill(black)
    cont=pygame.image.load("continue.jpg").convert_alpha()
    gameDisplay.fill(black)
    gameDisplay.blit(cont, (0,0))
    pygame.display.flip()
    pygame.display.update()
    
    msg1("Press SPACE to Continue..",white)
    pygame.display.update()
    time.sleep(3)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                gameDisplay.fill(black)
                break
    else:
        #gameDisplay.fill(black)
        end=pygame.image.load("end.png").convert_alpha()
        gameDisplay.fill(black)
        gameDisplay.blit(end, (0,0))
        pygame.display.flip()
    
        pygame.display.update()
        time.sleep(3)
        break
    

pygame.quit()
quit()
