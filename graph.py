import pygame
import math
import matplotlib.pyplot as plt
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
        
p1= planet(m=5,x=-1,y=0,vx=0.5,vy=1)
p2= planet(m=10,x=1,y=0,vx=5,vy=7)
p3= planet(m=7,x=3,y=1,vx=0.2,vy=5)

G=0.5
dt=0.01

points=[]
planete1x=[p1.x]
planete2x=[p1.y]
planete3x=[p2.x]
planete1y=[p2.y]
planete2y=[p3.x]
planete3y=[p3.y]


for i in range(1000000):
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
        planete1x.append(p1.x)
        p1.y=p1.y+p1.vy*dt
        planete1y.append(p1.y)

        p2.x=p2.x+p2.vx*dt  
        planete2x.append(p2.x)
        p2.y=p2.y+p2.vy*dt 
        planete2y.append(p2.y)

        p3.x+=p3.vx*dt
        planete3x.append(p3.x)
        p3.y+=p3.vy*dt
        planete3y.append(p3.y)


plt.plot(planete1x,planete1y,color="blue",label="planete1")
plt.plot(planete2x,planete2y,color="green",label="planete2")
plt.plot(planete3x,planete3y,color="yellow",label="planete3")
plt.xlabel("position x")
plt.ylabel("position y")
plt.title("comparaison des trajectoires")
plt.legend()
plt.grid(color="gray",alpha=0.4)
plt.axis("equal")
plt.show()




    
   
          
    
            
