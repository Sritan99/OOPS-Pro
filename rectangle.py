import pygame

pygame.init()

WIDTH=1000
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill("grey")

class rectangle():
    def __init__(self,x,y,w,h,c,t):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.c=c
        self.t=t
    def draw_rec(self):
        pygame.draw.rect(screen,self.c,(self.x,self.y,self.w,self.h),self.t)



class circle():
    def __init__(self,x,y,r,c,t):
        self.x=x
        self.y=y
        self.r=r
        self.c=c
        self.t=t

    def draw_circle(self):
        pygame.draw.circle(screen,self.c,(self.x,self.y),self.r,self.t)

c1=circle(70,70,70,"red",0)
c2=circle(500,500,100,"red",2)

c1.draw_circle()
c2.draw_circle()
        

r1=rectangle(350,285,300,70,"purple",1)

r2=rectangle(850,20,70,300,"purple",10)

r1.draw_rec()
r2.draw_rec()
        

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()


    pygame.display.update()


