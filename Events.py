import pygame

pygame.init()

WIDTH=1000
HEIGHT=700



screen=pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill("grey")

class circle():
    def __init__(self,x,y,r,c,t):
        self.x=x
        self.y=y
        self.r=r
        self.c=c
        self.t=t


    def circles(self):
        pygame.draw.circle(screen,self.c,(self.x,self.y),self.r,self.t)

    def expand_circ(self):
        self.r+=5
        pygame.draw.circle(screen,self.c,(self.x,self.y),self.r,self.t)

    def shrink_circ(self):
        self.r-=5
        pygame.draw.circle(screen,self.c,(self.x,self.y),self.r,self.t)

    def up_circ(self):
        self.y-=10
        pygame.draw.circle(screen,self.c,(self.x,self.y),self.r,self.t)

    def right_circ(self):
        self.x+=10
        pygame.draw.circle(screen,self.c,(self.x,self.y),self.r,self.t)

    def left_circ(self):
        self.x-=10
        pygame.draw.circle(screen,self.c,(self.x,self.y),self.r,self.t)

    def down_circ(self):
        self.y+=10
        pygame.draw.circle(screen,self.c,(self.x,self.y),self.r,self.t)

c1=circle(350,500,40,"red",10)  

  

c1.circles()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                screen.fill("grey")
                c1.expand_circ()

            if event.button==3:
                screen.fill("grey")
                c1.shrink_circ()

        
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                screen.fill("grey")
                c1.up_circ()

            if event.key==pygame.K_RIGHT:
                screen.fill("grey")
                c1.right_circ()

            if event.key==pygame.K_LEFT:
                screen.fill("grey")
                c1.left_circ()

            if event.key==pygame.K_DOWN:
                screen.fill("grey")
                c1.down_circ()

            if event.key==pygame.K_c:
                screen.fill("grey")

    pygame.display.update()





