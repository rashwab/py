import sys
import math  

PI = math.pi

def circle_area(x):
    return PI * x**2

def circumfrence(x):
    return 2 * PI * x

def square_area(l, w):
    return l * w

def square_perimeter(l, w):
    return 2 * (l + w)

def cuboid_volume(l, w, h):
    return l * w * h

def cuboid_surface_area(l, w, h):
    return 2 * (l*w + l*h + w*h)

option = int(input("""
1 - Area of circle
2 - Circumference of circle
3 - Square area
4 - Square perimeter
5 - Cuboid volume
6 - Cuboid surface area
7 - Exit
Enter your choice: """))

if option == 1 or option == 2:
    radius = float(input("Enter your radius: "))
    if option == 1:
        print(circle_area(radius))
    elif option == 2:
        print(circumfrence(radius))

elif option == 3 or option == 4:
    length = float(input("Enter your length: "))
    width = float(input("Enter your width: "))
    if option == 3:
        print(square_area(length, width))
    elif option == 4:
        print(square_perimeter(length, width))

elif option == 5 or option == 6:
    cuboid_length = float(input("Enter the length: "))
    cuboid_width = float(input("Enter width: "))
    cuboid_height = float(input("Enter height: "))
    if option == 5:
        print(cuboid_volume(cuboid_length, cuboid_width, cuboid_height))
    elif option == 6:
        print(cuboid_surface_area(cuboid_length, cuboid_width, cuboid_height))

elif option == 7:
    exit()

else:
    print("Invalid option")
    exit()
