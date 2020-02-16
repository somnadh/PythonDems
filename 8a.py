import math
def ball_collide(x1,y1,r1,x2,y2,r2):
 dist=math.sqrt((x2-x1)**2+(y2-y1)**2);
 print("Distance b/w two balls:",dist)
 center=dist/2;
 print("Collision point",center);
 r=r1+r2;
 print("Sum of radious",r)
 if(center<=r):
    print("They are Colliding")
    return True;
 else:
    print("Not Colliding")
    return False;

c=ball_collide(4,7,7,4,8,1)
print(c)
c=ball_collide(300,400,20,30,40,20)
print(c)