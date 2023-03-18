from tkinter import *
from random import randint
from mouse import *
from keyboard import *

root=Tk()
root.config(bg="black")
root.attributes("-fullscreen",True)
height=root.winfo_screenheight()
width=root.winfo_screenwidth()
cam=Canvas(root,height=1920,width=1080*2,bg='black')
cam.pack()
c="000000"
f=10000
speed=1
x=[-20,20,20,-20,-20,-20]
y=[-20,-20,30,30,-20,30]
z=[-660,-700,-700,-660,-750,-750]
connections=[[0,1,2,3,randint(230,254)],[3,0,4,5,randint(230,254)]]
v=len(x)
t=[0,0]
g=[get_position()[0],get_position()[1]]
print (g,type(g))
def getrot():
     global g
     if is_pressed('²'):
          t[0]=(get_position()[0]-g[0])/1.1
          t[1]=(get_position()[1]-g[1])/1.1
          if g[0]==width-1:
               for i in range(v):
                    h=[float(point_projected(x[i],y[i],z[i])[0]-400-t[0]),float(point_projected(x[i],y[i],z[i])[1]-400-t[1])]
                    y[i]=h[1]*(z[i]+f)/f
               move(1,g[1])
          elif g[0]==0:
               for i in range(v):
                    h=[float(point_projected(x[i],y[i],z[i])[0]-400-t[0]),float(point_projected(x[i],y[i],z[i])[1]-400-t[1])]
                    x[i]=h[0]*(z[i]+f)/f
               move(width,g[1])
          if g[1]==height-1:
               for i in range(v):
                    h=[float(point_projected(x[i],y[i],z[i])[0]-400-t[0]),float(point_projected(x[i],y[i],z[i])[1]-400-t[1])]
                    x[i]=h[0]*(z[i]+f)/f
               move(g[0],1)
          elif g[1]==0:
               for i in range(v):
                    h=[float(point_projected(x[i],y[i],z[i])[0]-400-t[0]),float(point_projected(x[i],y[i],z[i])[1]-400-t[1])]
                    x[i]=h[0]*(z[i]+f)/f
               move(g[0],height)
          else:
               for i in range(v):
                    h=[float(point_projected(x[i],y[i],z[i])[0]-400-t[0]),float(point_projected(x[i],y[i],z[i])[1]-400-t[1])]
                    y[i]=h[1]*(z[i]+f)/f
                    x[i]=h[0]*(z[i]+f)/f
          g=[get_position()[0],get_position()[1]]
def right():
     if is_pressed("z"):
          for i in range(v):
               z[i]=z[i]-speed
     if is_pressed("s"):
          for i in range(v):
               z[i]=z[i]+speed
     if is_pressed("q"):
          for i in range(v):
               x[i]=x[i]+speed/2
     if is_pressed("d"):
          for i in range(v):
               x[i]=x[i]-speed/2
     if is_pressed("space"):
          for i in range(v):
               y[i]=y[i]+speed
     if is_pressed("e"):
          for i in range(v):
               y[i]=y[i]-speed
def point_projected(x1,y1,z1):
     if z1!=-f:
          if z1!=0 :
               x_projected=(x1*f/(z1+f))+400
               y_projected=(y1*f/(z1+f))+400
          else:
               x_projected=x1+400
               y_projected=y1+400
     else:
          x_projected=(x1*50/(z1+f+0.1))+400
          y_projected=(y1*50/(z1+f+0.1))+400
     return x_projected,y_projected
def shader(z,p):
     u="#"
     for i in range(0,len(c),2):
          m=str(hex(p[4]))[3:]
          u=u+m
     return u.upper()
def line_drawer(x,y,z,connections):
    for i in connections:
          if z[i[0]]>=-f and z[i[1]]>=-f and z[i[2]]>=-f:
               p0=point_projected(x[i[0]],y[i[0]],z[i[0]])
               p1=point_projected(x[i[1]],y[i[1]],z[i[1]])
               p2=point_projected(x[i[2]],y[i[2]],z[i[2]])
               p3=point_projected(x[i[3]],y[i[3]],z[i[3]])
               cam.create_polygon(p0,p1,p2,p3,fill=shader(z,i),outline="dark gray" )
          elif z[i[0]]<=-f and z[i[1]]<=-f and z[i[2]]>=-f:
               p0=-1*point_projected(x[i[0]],y[i[0]],z[i[0]])
               p1=-1*point_projected(x[i[1]],y[i[1]],z[i[1]])
               p2=point_projected(x[i[2]],y[i[2]],z[i[2]])
               cam.create_polygon(p0,p1,p2,fill=shader(z,i) )
          elif z[i[0]]<=-f and z[i[1]]>=-f and z[i[2]]<=-f:
               p0=-1*point_projected(x[i[0]],y[i[0]],z[i[0]])
               p1=point_projected(x[i[1]],y[i[1]],z[i[1]])
               p2=-1*point_projected(x[i[2]],y[i[2]],z[i[2]])
               cam.create_polygon(p0,p1,p2,fill=shader(z,i) )
          elif z[i[0]]>=-f and z[i[1]]<=-f and z[i[2]]<=-f:
               p0=point_projected(x[i[0]],y[i[0]],z[i[0]])
               p1=-1*point_projected(x[i[1]],y[i[1]],z[i[1]])
               p2=-1*point_projected(x[i[2]],y[i[2]],z[i[2]])
               cam.create_polygon(p0,p1,p2,fill=shader(z,i) )
          elif z[i[0]]<=-f and z[i[1]]>=-f and z[i[2]]>=-f:
               p0=-1*point_projected(x[i[0]],y[i[0]],z[i[0]])
               p1=point_projected(x[i[1]],y[i[1]],z[i[1]])
               p2=point_projected(x[i[2]],y[i[2]],z[i[2]])
               cam.create_polygon(p0,p1,p2,fill=shader(z,i) )
          elif z[i[0]]>=-f and z[i[1]]<=-f and z[i[2]]>=-f:
               p0=point_projected(x[i[0]],y[i[0]],z[i[0]])
               p1=-1*point_projected(x[i[1]],y[i[1]],z[i[1]])
               p2=point_projected(x[i[2]],y[i[2]],z[i[2]])
               cam.create_polygon(p0,p1,p2,fill=shader(z,i) )
          elif z[i[0]]>=-f and z[i[1]]>=-f and z[i[2]]<=-f:
               p0=point_projected(x[i[0]],y[i[0]],z[i[0]])
               p1=point_projected(x[i[1]],y[i[1]],z[i[1]])
               p2=-1*point_projected(x[i[2]],y[i[2]],z[i[2]])
               cam.create_polygon(p0,p1,p2,fill=shader(z,i) )
while True:
     line_drawer(x,y,z,connections)
     right()
     getrot()
     root.update()
     cam.delete('all')
root.mainloop()
