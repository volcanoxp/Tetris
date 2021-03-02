import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED_X = (231, 76, 60 )
VIOLET_X = (155, 89, 182)
BLUE_X = (46, 134, 193 )
YELLOW_X = (241, 196, 15)
GREEN_X =(39, 174, 96 )

class Cuadrado():

    def __init__(self):
        self.WIDTH = 10
        self.HEIGTH = 10
        self.POS_X = 40
        self.POS_Y = -10
        self.position_state = 0
        self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X+10,self.POS_Y], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X+10,self.POS_Y+10]]
        self.velocidad = 10

    def restart(self):
        self.POS_X=40
        self.POS_Y=-10

    def update(self,pulse,pulse_R, pulse_L):

        if (pulse_R):
            self.POS_X+=10

        if (pulse_L):
            self.POS_X-=10

        self.pos_init = [[self.POS_X,self.POS_Y], 
                                 [self.POS_X+10,self.POS_Y], 
                                 [self.POS_X,self.POS_Y+10], #center
                                 [self.POS_X+10,self.POS_Y+10]]

        self.POS_Y+=self.velocidad
     

    def draw(self,screen):
        for posF in self.pos_init:
            pygame.draw.rect(screen,WHITE,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

    def get_position(self):
        return self.pos_init

    def draw_next(self,screen):
        POS_X_N = 130
        POS_Y_N = 80
        pos_init_next = [[POS_X_N,POS_Y_N], 
                        [POS_X_N+10,POS_Y_N], 
                        [POS_X_N,POS_Y_N+10], #center
                        [POS_X_N+10,POS_Y_N+10]]

        for posF in pos_init_next:
            pygame.draw.rect(screen,WHITE,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

class Linea():
    
    def __init__(self):
        self.WIDTH = 10
        self.HEIGTH = 10
        self.POS_X = 40
        self.POS_Y = -10
        self.position_state = 0
        self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X+10,self.POS_Y], #center
                                [self.POS_X+20,self.POS_Y],
                                [self.POS_X+30,self.POS_Y]]
        self.velocidad = 10

    def restart(self):
        self.POS_X=40
        self.POS_Y=-10

    def state(self, pulse):
        self.position_state += pulse
        
        if(self.position_state == 2):
            self.position_state=0    
        return self.position_state

    def update(self, pulse, pulse_R, pulse_L):

        position_state = self.state(pulse)
        
        if (pulse_R):
            self.POS_X+=10

        if (pulse_L):
            self.POS_X-=10


        if(position_state == 0):
            self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X+10,self.POS_Y], #center
                                [self.POS_X+20,self.POS_Y], 
                                [self.POS_X+30,self.POS_Y]]
        elif(position_state == 1):
            self.pos_init =  [[self.POS_X+10,self.POS_Y-10], 
                                [self.POS_X+10,self.POS_Y], #center
                                [self.POS_X+10,self.POS_Y+10], 
                                [self.POS_X+10,self.POS_Y+20]]

        self.POS_Y+=self.velocidad        

    def draw(self, screen):
        for posF in self.pos_init:
            pygame.draw.rect(screen,RED_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

    def get_position(self):
        return self.pos_init

    def draw_next(self, screen):
        POS_X_N = 130
        POS_Y_N = 80
        pos_init_next = [[POS_X_N,POS_Y_N], 
                        [POS_X_N,POS_Y_N+10], #center
                        [POS_X_N,POS_Y_N+20],
                        [POS_X_N,POS_Y_N+30]]
        for posF in pos_init_next:
            pygame.draw.rect(screen,RED_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

class R():

    def __init__ (self):
        self.WIDTH = 10
        self.HEIGTH = 10
        self.POS_X = 40
        self.POS_Y = -10
        self.position_state = 0
        self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X+10,self.POS_Y], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X,self.POS_Y+20]]
        self.velocidad = 10

    def restart(self):
        self.POS_X=40
        self.POS_Y=-10

    def state(self, pulse):
        self.position_state += pulse
        
        if(self.position_state == 4):
            self.position_state=0    
        return self.position_state

    def update(self, pulse, pulse_R, pulse_L):
        position_state = self.state(pulse)
        
        if (pulse_R):
            self.POS_X+=10

        if (pulse_L):
            self.POS_X-=10

        if(position_state == 0):
            self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X+10,self.POS_Y], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X,self.POS_Y+20]]
        elif(position_state == 1):
            self.pos_init = [[self.POS_X+10,self.POS_Y+10], 
                                [self.POS_X+10,self.POS_Y+20], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X-10,self.POS_Y+10]]
        elif(position_state == 2):
            self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X,self.POS_Y+20], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X-10,self.POS_Y+20]]
        elif(position_state == 3):
            self.pos_init = [[self.POS_X-10,self.POS_Y], 
                                [self.POS_X-10,self.POS_Y+10], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X+10,self.POS_Y+10]]
        self.POS_Y+=self.velocidad

    def draw(self, screen):
        for posF in self.pos_init:
            pygame.draw.rect(screen,BLUE_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

    def get_position(self):
        return self.pos_init

    def draw_next(self, screen):
        POS_X_N = 130
        POS_Y_N = 80
        pos_init_next = [[POS_X_N,POS_Y_N], 
                        [POS_X_N+10,POS_Y_N], 
                        [POS_X_N,POS_Y_N+10], #center
                        [POS_X_N,POS_Y_N+20]]
        for posF in pos_init_next:
            pygame.draw.rect(screen,BLUE_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

class R_inv():

    def __init__ (self):
        self.WIDTH = 10
        self.HEIGTH = 10
        self.POS_X = 40
        self.POS_Y = -10
        self.position_state = 0
        self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X-10,self.POS_Y], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X,self.POS_Y+20]]
        self.velocidad = 10

    def restart(self):
        self.POS_X=40
        self.POS_Y=-10

    def state(self, pulse):
        self.position_state += pulse
        
        if(self.position_state == 4):
            self.position_state=0    
        return self.position_state


    def update(self, pulse, pulse_R, pulse_L):
        position_state = self.state(pulse)
        
        if (pulse_R):
            self.POS_X+=10

        if (pulse_L):
            self.POS_X-=10

        if(position_state == 0):
            self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X-10,self.POS_Y], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X,self.POS_Y+20]]
        elif(position_state == 1):
            self.pos_init = [[self.POS_X+10,self.POS_Y], 
                                [self.POS_X+10,self.POS_Y+10], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X-10,self.POS_Y+10]]
        elif(position_state == 2):
            self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X,self.POS_Y+20], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X+10,self.POS_Y+20]]
        elif(position_state == 3):
            self.pos_init = [[self.POS_X-10,self.POS_Y+20], 
                                [self.POS_X-10,self.POS_Y+10], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X+10,self.POS_Y+10]]
        self.POS_Y+=self.velocidad
        

    def draw(self, screen):
        for posF in self.pos_init:
            pygame.draw.rect(screen,GREEN_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

    def get_position(self):
        return self.pos_init

    def draw_next(self, screen):
        POS_X_N = 130
        POS_Y_N = 80
        pos_init_next = [[POS_X_N,POS_Y_N], 
                        [POS_X_N-10,POS_Y_N], 
                        [POS_X_N,POS_Y_N+10], #center
                        [POS_X_N,POS_Y_N+20]]
        for posF in pos_init_next:
            pygame.draw.rect(screen,GREEN_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

class Z():

    def __init__ (self):
        self.WIDTH = 10
        self.HEIGTH = 10
        self.POS_X = 40
        self.POS_Y = -10
        self.position_state = 0
        self.pos_init = [[self.POS_X,self.POS_Y], 
                        [self.POS_X+10,self.POS_Y], 
                        [self.POS_X,self.POS_Y+10], #center
                        [self.POS_X-10,self.POS_Y+10]]
        self.velocidad = 10


    def restart(self):
        self.POS_X=40
        self.POS_Y=-10

    def state(self, pulse):
        self.position_state += pulse
        
        if(self.position_state == 4):
            self.position_state=0    
        return self.position_state

    def update(self, pulse, pulse_R, pulse_L):
        position_state = self.state(pulse)
        
        if (pulse_R):
            self.POS_X+=10

        if (pulse_L):
            self.POS_X-=10
        
        if(position_state == 0):
            self.pos_init =  [[self.POS_X,self.POS_Y], 
                                [self.POS_X+10,self.POS_Y], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X-10,self.POS_Y+10]]
        elif(position_state == 1):
            self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X+10,self.POS_Y+10], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X+10,self.POS_Y+20]]
        elif(position_state == 2):
            self.pos_init =  [[self.POS_X+10,self.POS_Y+10], 
                                [self.POS_X,self.POS_Y+20], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X-10,self.POS_Y+20]]
        elif(position_state == 3):
            self.pos_init = [[self.POS_X-10,self.POS_Y], 
                                [self.POS_X-10,self.POS_Y+10], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X,self.POS_Y+20]]
        
        self.POS_Y+=self.velocidad

    def draw(self, screen):
        for posF in self.pos_init:
            pygame.draw.rect(screen,VIOLET_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

    def get_position(self):
        return self.pos_init

    def draw_next(self, screen):
        POS_X_N = 130 
        POS_Y_N = 80
        pos_init_next = [[POS_X_N,POS_Y_N], 
                        [POS_X_N+10,POS_Y_N], 
                        [POS_X_N,POS_Y_N+10], #center
                        [POS_X_N-10,POS_Y_N+10]]

        for posF in pos_init_next:
            pygame.draw.rect(screen,VIOLET_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)



class Z_inv():

    def __init__ (self):
        self.WIDTH = 10
        self.HEIGTH = 10
        self.POS_X = 40
        self.POS_Y = -10
        self.position_state = 0
        self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X-10,self.POS_Y], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X+10,self.POS_Y+10]]
        self.velocidad = 10

    def restart(self):
        self.POS_X=40
        self.POS_Y=-10

    def state(self, pulse):
        self.position_state += pulse
        
        if(self.position_state == 4):
            self.position_state=0    
        return self.position_state

    def update(self, pulse, pulse_R, pulse_L):
        position_state = self.state(pulse)
        
        if (pulse_R):
            self.POS_X+=10

        if (pulse_L):
            self.POS_X-=10

        if(position_state == 0):
            self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X-10,self.POS_Y], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X+10,self.POS_Y+10]]
        elif(position_state == 1):
            self.pos_init = [[self.POS_X+10,self.POS_Y+10], 
                                [self.POS_X+10,self.POS_Y], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X,self.POS_Y+20]]
        elif(position_state == 2):
            self.pos_init = [[self.POS_X-10,self.POS_Y+10], 
                                [self.POS_X,self.POS_Y+20], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X+10,self.POS_Y+20]]
        elif(position_state == 3):
            self.pos_init = [[self.POS_X,self.POS_Y], 
                                [self.POS_X-10,self.POS_Y+10], 
                                [self.POS_X,self.POS_Y+10], #center
                                [self.POS_X-10,self.POS_Y+20]]
        self.POS_Y+=self.velocidad

    def draw(self, screen):
        for posF in self.pos_init:
            pygame.draw.rect(screen,YELLOW_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)

    def get_position(self):
        return self.pos_init

    def draw_next(self, screen):
        POS_X_N = 130
        POS_Y_N = 80
        pos_init_next = [[POS_X_N,POS_Y_N], 
                        [POS_X_N-10,POS_Y_N], 
                        [POS_X_N,POS_Y_N+10], #center
                        [POS_X_N+10,POS_Y_N+10]]

        for posF in pos_init_next:
            pygame.draw.rect(screen,YELLOW_X,[posF[0],posF[1],self.WIDTH, self.HEIGTH], 2)