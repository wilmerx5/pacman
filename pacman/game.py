import pygame as pg
import sys 
import random as r
from pygame import sprite

pg.init()
#  configuracon pantalla
SCREEN_WIDTH=900
SCREEN_HEIGHT=600
SCREEN=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

RELOJ= pg.time.Clock()

# carga de imagenes
IMAGENES=[pg.image.load('img/r1.png').convert_alpha(),pg.image.load('img/r2.png').convert_alpha(),
          pg.image.load('img/l1.png').convert_alpha(),pg.image.load('img/l2.png').convert_alpha(),
          pg.image.load('img/u1.png').convert_alpha(),pg.image.load('img/u2.png').convert_alpha(),
          pg.image.load('img/d1.png').convert_alpha(),pg.image.load('img/d2.png').convert_alpha(),
          
          ]
CIRCLES=[
    [pg.image.load('img/CIRCLE.png').convert_alpha(),80,200],[pg.image.load('img/CIRCLE.png').convert_alpha(),160,200],[pg.image.load('img/CIRCLE.png').convert_alpha(),240,200],[pg.image.load('img/CIRCLE.png').convert_alpha(),320,200],[pg.image.load('img/CIRCLE.png').convert_alpha(),400,200],[pg.image.load('img/CIRCLE.png').convert_alpha(),480,200],[pg.image.load('img/CIRCLE.png').convert_alpha(),560,200],[pg.image.load('img/CIRCLE.png').convert_alpha(),650,200],[pg.image.load('img/CIRCLE.png').convert_alpha(),720,200],[pg.image.load('img/CIRCLE.png').convert_alpha(),800,200],
    [pg.image.load('img/CIRCLE.png').convert_alpha(),80,450],[pg.image.load('img/CIRCLE.png').convert_alpha(),160,450],[pg.image.load('img/CIRCLE.png').convert_alpha(),240,450],[pg.image.load('img/CIRCLE.png').convert_alpha(),320,450],[pg.image.load('img/CIRCLE.png').convert_alpha(),400,450],[pg.image.load('img/CIRCLE.png').convert_alpha(),480,450],[pg.image.load('img/CIRCLE.png').convert_alpha(),560,450],[pg.image.load('img/CIRCLE.png').convert_alpha(),650,450],[pg.image.load('img/CIRCLE.png').convert_alpha(),720,450],[pg.image.load('img/CIRCLE.png').convert_alpha(),800,450],
    [pg.image.load('img/CIRCLE.png').convert_alpha(),200,80],[pg.image.load('img/CIRCLE.png').convert_alpha(),200,160],[pg.image.load('img/CIRCLE.png').convert_alpha(),200,240],[pg.image.load('img/CIRCLE.png').convert_alpha(),200,320],[pg.image.load('img/CIRCLE.png').convert_alpha(),200,400],[pg.image.load('img/CIRCLE.png').convert_alpha(),200,480],[pg.image.load('img/CIRCLE.png').convert_alpha(),200,560],
    [pg.image.load('img/CIRCLE.png').convert_alpha(),650,80],[pg.image.load('img/CIRCLE.png').convert_alpha(),650,160],[pg.image.load('img/CIRCLE.png').convert_alpha(),650,240],[pg.image.load('img/CIRCLE.png').convert_alpha(),650,320],[pg.image.load('img/CIRCLE.png').convert_alpha(),650,400],[pg.image.load('img/CIRCLE.png').convert_alpha(),650,480],[pg.image.load('img/CIRCLE.png').convert_alpha(),650,560]
         ]
CIRCLES_COPY=CIRCLES[:]

FRUTAS=[[pg.image.load('img/fruta1.png').convert_alpha(),520,350],
        [pg.image.load('img/fruta2.png').convert_alpha(),100,400],
        [pg.image.load('img/fruta3.png').convert_alpha(),380,350],
        [pg.image.load('img/fruta4.png').convert_alpha(),80,200],
        [pg.image.load('img/fruta4.png').convert_alpha(),650,300],
        [pg.image.load('img/fruta2.png').convert_alpha(),650,500],


        ]

FRUTAS_COPY=FRUTAS[:]
start_img=pg.image.load('img/start.png').convert_alpha()
gover_img=pg.image.load('img/gover.png').convert_alpha()
died_img =pg.image.load('img/died.png').convert_alpha()
win_img = pg.image.load('img/win.png').convert_alpha()
# control movimientos
Game=True
LEFT=False
RIGHT=False
UP=False
DOWN=False
step_index=0
ghost_index=0
imagep= IMAGENES[0] if step_index//5==0 else IMAGENES[1]
image_rect= imagep.get_rect()
image_rect.x=300
image_rect.y=30
# carga sonidos
sound = pg.mixer.Sound('img/eat.mp3')
dead_sound = pg.mixer.Sound('img/dead.mp3')
game_over_sound = pg.mixer.Sound('img/game_over.mp3')

win_sound = pg.mixer.Sound('img/win.mp3')
track = pg.mixer.Sound('img/track.mp3')
running = pg.mixer.Sound('img/running.mp3')
nan = pg.mixer.Sound('img/nan.mp3')




# movimiento player
def movement(step_ind,x,y):
    imagep= IMAGENES[0] if step_ind//5==0 else IMAGENES[1]
    if LEFT:
        imagep= IMAGENES[2] if step_ind//5==0 else IMAGENES[3]
    if UP:
        imagep= IMAGENES[4] if step_ind//5==0 else IMAGENES[5]
    
    if DOWN:
        imagep= IMAGENES[6] if step_ind//5==0 else IMAGENES[7]
    if DIED:
         imagep=died_img

    imagep =pg.transform.scale(imagep,(70,60))

    image_rect= imagep.get_rect()

    SCREEN.blit(imagep,(x,y))
    return image_rect


# muros

walls= [pg.Rect(160, 0, 5, 180),
        pg.Rect(260, 0, 5, 180),
        pg.Rect(710, 0, 5, 170),
        pg.Rect(610, 0, 5, 180),
        pg.Rect(710, 550, 5, 100),
        pg.Rect(160, 280, 5, 100),
        pg.Rect(380, 0, 5, 180),
        pg.Rect(500, 0, 5, 180), 
        pg.Rect(165, 500, 5, 100),

        pg.Rect(710, 250, 5, 180),
        pg.Rect(260, 270, 150, 5),
        pg.Rect(500, 270, 110, 5),
        pg.Rect(260, 270, 5, 150),
        pg.Rect(610, 270, 5, 150),
        pg.Rect(500, 415, 110, 5),
        pg.Rect(260, 415, 150, 5),
        pg.Rect(500, 510, 110, 5),
        pg.Rect(260, 510, 150, 5),
        pg.Rect(710, 165, 180, 5),
        pg.Rect(710, 250, 180, 5),
        pg.Rect(710, 430, 180, 5),
        pg.Rect(710, 550, 180, 5),
        pg.Rect(260, 595, 360, 5),
        pg.Rect(0, 175, 165, 5),
        pg.Rect(0, 280, 165, 5),
        pg.Rect(0, 380, 165, 5),
        pg.Rect(0, 500, 165, 5),
        pg.Rect(380, 180, 125, 5),
        ]


#ghost 
Ghosts=[
     pg.image.load('img/g11.png').convert_alpha(),
     pg.image.load('img/g12.png').convert_alpha(),
     pg.image.load('img/g21.png').convert_alpha(),
     pg.image.load('img/g22.png').convert_alpha(),
     pg.image.load('img/g31.png').convert_alpha(),
     pg.image.load('img/g32.png').convert_alpha(),

]
#movimiento fantasmas
YGHOST1=[True,180,50]
YGHOST2=[True,200,520]
YGHOST3=[True,300,320]
YGHOST4=[True,640,70]

def movGhost(stepind,images,Positions, rangos,posicionACmbiar):   
    ghost= Ghosts[images[0]] if stepind//5==0 else Ghosts[images[1]]
    ghost_rect= ghost.get_rect()
    ghost_rect.x=Positions[1]
    ghost_rect.y=Positions[2]
    if Positions[0]:
        Positions[posicionACmbiar] +=1
        if(Positions[posicionACmbiar]>=rangos[0]):
            Positions[0]=False
    else:
        Positions[posicionACmbiar]-=0.8
        if(Positions[posicionACmbiar]<=rangos[1]):
            Positions[0]=True 
    SCREEN.blit(ghost,(ghost_rect.x,ghost_rect.y))
    return ghost_rect

START=True
GOVER=False

DIED=False
WIN=False

fuente = pg.font.Font(None, 28)

#score
score=0
cont_sound_win=0
score_win=[]
#reproducti sonido caca cieerto tiempo
pg.time.set_timer(pg.USEREVENT, 900)
pg.time.set_timer(pg.USEREVENT + 1, 11400) 
track.play()

while Game:
    # current_time = pg.time.get_ticks()

    
    texto = fuente.render(f'Score: {str(round(score))}', True, (255, 255, 255))   
    keys= pg.key.get_pressed()
         
    RELOJ.tick(50)
    SCREEN.fill((60,60,100))
    SCREEN.blit(texto,(760,30))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Game=False
        elif event.type == pg.USEREVENT and not GOVER and START==False and WIN==False:
             running.play()
        elif event.type == pg.USEREVENT+1 and not GOVER :
             track.play()
    player=movement(step_index,image_rect.x,image_rect.y)
    if keys[pg.K_d] and image_rect.x < SCREEN_WIDTH-player.width :
            LEFT=False
            RIGHT=True
            UP=False
            DOWN=False
            image_rect.x+=1.4
    if keys[pg.K_a] and image_rect.x>0:
            LEFT=True
            RIGHT=False
            UP=False
            DOWN=False
            image_rect.x-=1.4

            
    if keys[pg.K_w] and image_rect.y > 0:
            LEFT=False
            RIGHT=False
            UP=True
            DOWN=False
            image_rect.y-=1.4

            
    if keys[pg.K_s]  and image_rect.y <SCREEN_HEIGHT-player.height:
            LEFT=False
            RIGHT=False
            UP=False
            DOWN=True
            image_rect.y+=1.4


    
    ghosts=[movGhost(ghost_index,[0,1],YGHOST1,[500,50],2),movGhost(ghost_index,[2,3],YGHOST2,[600,170],1),movGhost(ghost_index,[3,4],YGHOST3,[570,300],1),movGhost(ghost_index,[0,1],YGHOST4,[500,50],2)]
    for ghost in ghosts:
        # pg.draw.rect(SCREEN, (255, 0, 0), ghost, 2)

        if ghost.colliderect(image_rect):

            img=pg.transform.scale(died_img,(100,100))
            SCREEN.blit(img,(image_rect.y,image_rect.y))
            dead_sound.play()

            GOVER= True
            pg.time.delay(2000)
            game_over_sound.play()
            score=0
            image_rect.x=1000

    for circle in CIRCLES:
        circle_img = pg.transform.scale(circle[0], (10, 10))
        circle_rect = circle_img.get_rect()
        circle_rect.x=circle[1]
        circle_rect.y=circle[2]
        SCREEN.blit(circle_img, (circle_rect.x,circle_rect.y))
    
    # Verifica la colisión con el jugador
        if image_rect.colliderect(circle_rect):
             score+=100
             CIRCLES.remove(circle)
             sound.play()
    for fruta in FRUTAS:
        fruta_rect = fruta[0].get_rect()
        fruta_rect.x=fruta[1]
        fruta_rect.y=fruta[2]
        SCREEN.blit(fruta[0], (fruta_rect.x,fruta_rect.y))
    
    # Verifica la colisión con el jugador
        if image_rect.colliderect(fruta_rect):
             score+=500
             FRUTAS.remove(fruta)
             nan.play()


    for wall in walls:
        pg.draw.rect(SCREEN,(255,0,0),wall)
        if wall.colliderect(image_rect) and keys[pg.K_a]:
             image_rect.x+=1 
        if wall.colliderect(image_rect) and keys[pg.K_d]:
             image_rect.x-=1  
        if wall.colliderect(image_rect) and keys[pg.K_w]:
             image_rect.y+=1
        if wall.colliderect(image_rect) and keys[pg.K_s]:
             image_rect.y-=1    
    # pg.draw.rect(SCREEN, (255, 0, 0), image_rect, 2)
    # pg.draw.rect(SCREEN, (255, 0, 0), prueba_rect, 2)
    
    if step_index>=10:
         step_index=0
    step_index+=1
    if ghost_index>=10:
         ghost_index=0
    ghost_index+=0.2

    
    if START:
        SCREEN.blit(start_img,(0,0))
        if keys[pg.K_RETURN]:
             START=False
             
    
    if GOVER:
        SCREEN.blit(gover_img,(0,0))
        if keys[pg.K_RETURN]:
              GOVER=False
              CIRCLES=CIRCLES_COPY[:]
              FRUTAS=FRUTAS_COPY[:]

              image_rect.x=300
              image_rect.y=0
              score=0
    else:
        score+=00.1
    if len(FRUTAS) ==0 and len(CIRCLES)==0:
         WIN=True
    if WIN:
         score_win.append(score)
         score=score_win[0]
         SCREEN.blit(win_img,(0,0))
         SCREEN.blit(texto,(400,500))
         image_rect.x=1000

         if keys[pg.K_RETURN]:      
              WIN=False
              CIRCLES=CIRCLES_COPY[:]
              FRUTAS=FRUTAS_COPY[:]

              image_rect.x=300
              image_rect.y=0
              score=0
              cont_sound_win=0
         if cont_sound_win<1:  
            win_sound.play()
         cont_sound_win+=1
    pg.display.flip() 
    pg.display.update()
