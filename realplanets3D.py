
import math
from vpython import *
from dataclasses import dataclass
#init





scale=1e-6
scene.width = 1100
scene.height = 700
scene.background = color.black
scene.title = "Probleme des trois corps"
scene.autoscale = False
scene.center = vector(20, 115, 3)
scene.range = 250
@dataclass
class planet:

    m : float
    x : float
    y : float
    z: float
    vx: float
    vy: float
    vz: float
#at 2026-Nov-10 00:00:00        
p1= planet(m=1988410e24,x=-1.504607374351569e5,y=-7.530129189757679e5,z=1.338692538323492e4,vx=1.024208825506264e-2,vy=4.931312178683457e-3,vz=-2.235574920994247e-4)
p2= planet(m=5.97219e24,x=1.004724634765653e8,y=1.080150191341946e8,z=6.485307280950248e3,vx=-2.234991849741000e1,vy=2.012892592638202e1,vz=-1.325385760976516e-3)
p3= planet(m=6.4171e23,x=-6.095085705258984e7,y=2.312534415814546e8,z=6.366211031335011e6,vx=-2.251041255102506e1,vy=-4.079146739244040,vz=4.663878296057569e-1)

G=6.67430e-20
dt=600

points=[]
sun=sphere(pos=vector(p1.x*scale,p1.y*scale,p1.z*scale),radius=12,color=color.yellow)
earth=sphere(pos=vector(p2.x*scale,p2.y*scale,p2.z*scale),radius=7,color=color.blue)
mars=sphere(pos=vector(p3.x*scale,p3.y*scale,p3.z*scale),radius=5,color=color.green)
while(True):
    rate(60)
    for _ in range(100):
        dx12=p2.x-p1.x
        dy12=p2.y-p1.y   
        dx23=p3.x-p2.x
        dy23=p3.y-p2.y
        dx13=p3.x-p1.x
        dy13=p3.y-p1.y   
        dz12=p2.z-p1.z
        dz23=p3.z-p2.z
        dz13=p3.z-p1.z  
        r12=math.sqrt(dx12**2+dy12**2+dz12**2)
        r13=math.sqrt(dx13**2+dy13**2+dz13**2)
        r23=math.sqrt(dx23**2+dy23**2+dz23**2)
        
        a1x = G * ((p2.m * dx12 / r12**3)+(p3.m*dx13/r13**3))
        a1y = G * ((p2.m * dy12 / r12**3)+(p3.m*dy13/r13**3))
        a1z  = G * ((p2.m * dz12 / r12**3)+(p3.m*dz13/r13**3))

        a2x = G * ((p1.m * (-dx12) / r12**3) +(p3.m * dx23 / r23**3))
        a2y = G * ((p1.m * (-dy12) / r12**3) +(p3.m * dy23 / r23**3))
        a2z = G * ((p1.m * (-dz12) / r12**3) +(p3.m * dz23 / r23**3))

        a3x=-G*((p1.m * dx13 / r13**3)+(p2.m * dx23 / r23**3))
        a3y=-G*((p1.m * dy13 / r13**3)+(p2.m * dy23 / r23**3))
        a3z=-G*((p1.m * dz13 / r13**3)+(p2.m * dz23 / r23**3))

        p1.vx += a1x * dt
        p1.vy += a1y * dt
        p1.vz += a1z * dt

        p2.vx += a2x * dt
        p2.vy += a2y * dt
        p2.vz += a2z * dt

        p3.vx+=a3x*dt
        p3.vy+=a3y*dt
        p3.vz+=a3z*dt

        p1.x=p1.x+p1.vx*dt
        p1.y=p1.y+p1.vy*dt
        p1.z=p1.z+p1.vz*dt

        p2.x=p2.x+p2.vx*dt  
        p2.y=p2.y+p2.vy*dt
        p2.z=p2.z+p2.vz*dt 

        p3.x+=p3.vx*dt
        p3.y+=p3.vy*dt
        p3.z+=p3.vz*dt


            

        sun.pos = vector(p1.x*scale, p1.y*scale, p1.z*scale)
        earth.pos = vector(p2.x*scale, p2.y*scale, p2.z*scale)
        mars.pos = vector(p3.x*scale, p3.y*scale, p3.z*scale)

            
