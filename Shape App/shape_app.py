# 1.  input the shape 
# enter attributes 
# pick multichoice answer for eg for circle area/circumference/sector
# output the results
import sys
import math  

PI = math.pi

def circle_area(x):
  return x * PI **2

def circumfrence(x):
   return 2 * PI **2

def square_area(l,w):
 return l**2 * w

def square_perimeter(l,w):
   return l+w

def cuboid_volume(l,w,h):
   return l*w*h

def cuboid_surface_area(l,w,h):
   return 2*w*l+2*h*w


option = int(input("""""
 1 - Area of circle
 2 - Circumfrence of circle
 3 - Square area
 4 - Square permimeter
 5 - cuboid volume
 6 - cuboid surface area 
 7 - exit"""))

if option == 1 or option == 2:
    radius = float(input("enter your raidus"))
    if option== 1: print (circle_area(radius))
    elif option ==2: print (circumfrence(radius))
 
elif option == 3 or option == 4:
    length= float(input("enter your length"))
    width= float (input("enter your width"))
if option==3: print(square_area(length,width))
elif option==4:print(square_perimeter(length,width))
    
elif option ==5 or option ==6:
 cuboid_length= float(input("enther the length"))
 cuboid_width= float(input("enter width"))
 cuboid_height= float (input("enter height"))

if option == 5: print(cuboid_volume(cuboid_length,cuboid_width,cuboid_height))
if option == 6: print(cuboid_surface_area(cuboid_length,cuboid_height,cuboid_width))
else:
 exit()
 
