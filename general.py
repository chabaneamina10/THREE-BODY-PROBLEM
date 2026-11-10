import pygame
import math
from dataclasses import dataclass
#init

pygame.init()
height=700
width=1100
window=pygame.display.set_mode((width,height))
#title:
pygame.display.set_caption("probleme 3 corps")
#colors:
white=(255,255,255)
blue=(50,50,150)
green=(10,200,10)
yellow=(200,200,10)

clock=pygame.time.Clock()

@dataclass
class planet:

    m : float
    x : float
    y : float
    vx: float
    vy: float
        
p1= planet(m=10,x=-1,y=0,vx=0.005,vy=0.00001)
p2= planet(m=1,x=1,y=0,vx=0.0005,vy=0.0007)
p3= planet(m=20,x=3,y=1,vx=0.0002,vy=0.0005)

G=0.5
dt=0.01
running=True
points=[]
while(running):
    for event in pygame.event.get():
        if event.type==pygame.quit:
            running=False
    dx12=p2.x-p1.x
    dy12=p2.y-p1.y   
    dx23=p3.x-p2.x
    dy23=p3.y-p2.y
    dx13=p3.x-p1.x
    dy13=p3.y-p1.y     
    r12=math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
    r13=math.sqrt((p3.x-p1.x)**2+(p3.y-p1.y)**2)
    r23=math.sqrt((p3.x-p2.x)**2+(p3.y-p2.y)**2)
    if r12 > 0.01 and r13 > 0.01 and r23 > 0.01:
        a1x = G * ((p2.m * dx12 / r12**3)+(p3.m*dx13/r13**3))
        a1y = G * ((p2.m * dy12 / r12**3)+(p3.m*dy13/r13**3))

        a2x = G * ((p1.m * (-dx12) / r12**3) +(p3.m * dx23 / r23**3))
        a2y = G * ((p1.m * (-dy12) / r12**3) +(p3.m * dy23 / r23**3))

        a3x=G*((p1.m * dx13 / r13**3)+(p2.m * dx23 / r23**3))
        a3y=G*((p1.m * dy13 / r13**3)+(p2.m * dy23 / r23**3))

        p1.vx += a1x * dt
        p1.vy += a1y * dt

        p2.vx += a2x * dt
        p2.vy += a2y * dt

        p3.vx+=a3x*dt
        p3.vy+=a3y*dt

        p1.x=p1.x+p1.vx*dt
        p1.y=p1.y+p1.vy*dt

        p2.x=p2.x+p2.vx*dt  
        p2.y=p2.y+p2.vy*dt 

        p3.x+=p3.vx*dt
        p3.y+=p3.vy*dt

    window.fill(white) 
    x1=int(400+p1.x*100) 
    x2=int(400+p2.x*100)
    x3=int(400+p3.x*100) 
    y1=int(400+p1.y*100)
    y2=int(400+p2.y*100)
    y3=int(400+p3.y*100)
    points.append((x2, y2))
    if len(points) > 1:
        pygame.draw.lines(window, white, False, points, 1)
    pygame.draw.circle(window,blue,(x1,y1),15)
    pygame.draw.circle(window,green,(x2,y2),8)
    pygame.draw.circle(window,yellow,(x3,y3),10)
          
    pygame.display.flip()
    clock.tick(60)
pygame.quit()    

            
