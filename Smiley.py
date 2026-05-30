import pygame

pygame.init()

WIDTH=1000
HEIGHT=700


screen=pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill("skyblue")

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


c1=circle(500,350,250,"gold",0)

c2=circle(410,248,31,"brown",0)
c3 = circle(592, 251, 29,"brown",0)


c4=circle(360,450,33,"white",0)
c5=circle(640,450, 33, "white", 0)
r1=rectangle(360,417,280,66,"white",0)



r2=rectangle(324,449,352,4,"black",0)

r3=rectangle(391,417,4,66,"black",0)
r4= rectangle(448,417,4,66,"black",0)
r5=rectangle(502,417,4,66,"black",0)
r6=rectangle(554,417,4,66,"black",0)

r7 = rectangle(609,417,4,66,"black",0)


c1.draw_circle()

c2.draw_circle()
c3.draw_circle()


r1.draw_rec()
c4.draw_circle()
c5.draw_circle()
r2.draw_rec()

r3.draw_rec()

r4.draw_rec()
r5.draw_rec()


r6.draw_rec()
r7.draw_rec()
        




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()




    pygame.display.update()