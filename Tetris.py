#Author: Jose Galarza


import pygame
from figuras import Cuadrado, R, R_inv, Z, Z_inv, Linea
from random import randint

pygame.init()

size = WIDTH, HEIGTH = 160, 200

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf',15)
font_1 = pygame.font.Font('freesansbold.ttf',13)
font_2 = pygame.font.Font('freesansbold.ttf',20)

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GRAY = (44, 62, 80)

state_screen = True
score = 0


#INSTANCIANDO ELEMENTOS

cuadrado = Cuadrado()
linea = Linea()
figR = R()
figR_inv = R_inv()
figZ = Z()
figZ_inv = Z_inv()
############################3

pulse_up=0
pulse_R=False
pulse_L=False

bloques_finales=[]
posicionesObject=[]
bandera_next_aleatorio=True

Figuras_Finales = [Cuadrado(), Linea(), R(), R_inv(), Z(), Z_inv()]
Figuras_Finales_NEXT = [Cuadrado(), Linea(), R(), R_inv(), Z(), Z_inv()]

valorAletorio = randint(0,5)

Limite = [HEIGTH for a in range(12)]

def drawFigure(Figure,pulse_up,pulse_R,pulse_L,screen):
    Figure.update(pulse_up,pulse_R,pulse_L)
    Figure.draw(screen)

def get_position(Figure):
    return Figure.get_position()

def restart_total(Figure):
    Figure.restart()

def draw_next(Figure,screen):
    Figure.draw_next(screen)

while state_screen:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state_screen =  False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pulse_up = 1
            if event.key == pygame.K_RIGHT:
                pulse_R = True
            if event.key == pygame.K_LEFT:
                pulse_L = True

    screen.fill(BLACK)
    pygame.draw.rect(screen,BLUE,[100,0,10,200])

    for x in range(0,100,10):
        for y in range(0,200,10):
            pygame.draw.rect(screen,GRAY,[x,y,10,10],1)

    #### Dibujo de bloques 
    for bloque in bloques_finales:
        pygame.draw.rect(screen,WHITE,[bloque[0],bloque[1],10,10], 2)
    ####

    #Limitación de movimiento
    for element in posicionesObject:
        if element[0] <= 0:
            pulse_L=False
            break
        if element[0] >= 90:
            pulse_R=False
            break
    ####

    #Dibujo de la figura manejable y la siguiente figura
    drawFigure(Figuras_Finales[valorAletorio],pulse_up,pulse_R,pulse_L,screen)
   
    if bandera_next_aleatorio:
        valorAletorio_next=randint(0,5)
        bandera_next_aleatorio=False

    draw_next(Figuras_Finales_NEXT[valorAletorio_next],screen)
    ####

    # Texto de salida
    OUT_score_1 = font_1.render("Score:",False, RED)
    screen.blit(OUT_score_1,(115, 10))
    score_text = str(score)
    OUT_score_2 = font.render(score_text,False, RED)
    screen.blit(OUT_score_2,(130, 25))

    OUT_score = font.render("Next:",False, RED)
    screen.blit(OUT_score,(115, 60))
    ##

    # Detección si se perdio
    for block in Limite:
        if block <= 0:
            bloques_finales=bloques_finales[len(bloques_finales):]
            OUT_Lose = font_2.render("LOSE",False, RED)
            screen.blit(OUT_Lose,(20, 100))

            pygame.display.flip()
            pygame.time.delay(1000)
            Limite = [HEIGTH for a in range(12)]
            score = 0
    ###

    pygame.display.flip()
    clock.tick(10)

    

    ###Recolectando datos
    posicionesObject=get_position(Figuras_Finales[valorAletorio])

    count = 0
    for pos in posicionesObject:
        
        if (pos[1] == (Limite[int(pos[0]/10)] - 10)):
            count+=1
            if count==1 :
                
                for i in range(4):
                    if (posicionesObject[i][1] < Limite[int(posicionesObject[i][0]/10)]):
                        Limite[int(posicionesObject[i][0]/10)] = posicionesObject[i][1]

                for pos in posicionesObject:
                    bloques_finales.append(pos)
                
                valorAletorio=valorAletorio_next
                restart_total(Figuras_Finales[valorAletorio])
                bandera_next_aleatorio=True
               

    #Solo permite un giro
    pulse_up=0
    pulse_R=False
    pulse_L=False

    #Detección de linea completa

    bloque_final_Y=[]
    for Y in bloques_finales:
        bloque_final_Y.append(Y[1])

    uniq_bloque_Y = list(set(bloque_final_Y))

    for element in uniq_bloque_Y:
        num_Repeticiones_Y = bloque_final_Y.count(element) 

        if num_Repeticiones_Y == 10:
            seq_eliminar=[]
            for bloque in bloques_finales:
                if bloque[1] == element:
                    seq_eliminar.append(bloques_finales.index(bloque))

            for x in reversed(seq_eliminar):
                bloques_finales.pop(x)

            for block in bloques_finales:
                if block[1] < element:
                    block[1]+=10

            for i in range(len(Limite)):
                if Limite[i] <= HEIGTH:
                    Limite[i]+=10

            score+=1
    ###
    
    
pygame.quit()




