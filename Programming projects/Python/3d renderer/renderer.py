from turtle import *
import math

focal_length = 800 # Distance from screen to "camera"

# Setup for turtle, you can change this for your preference
def setup():
    global focal_length
    
    penup()
    pensize(3)
    speed(0)
    hideturtle()
    tracer(0)


def end(): # End all codes with end()
    hideturtle()
    input()

def point(x,y,z):
    x_projected = (focal_length*x)/(focal_length+z) # This handles the 3d stuff
    y_projected = (focal_length*y)/(focal_length+z)
    goto(x_projected,y_projected)
    dot()

    return(x_projected,y_projected)


def line(point1,point2):
    goto(point1[0],point1[1])
    pendown()
    goto(point2[0],point2[1])
    penup()

def connect(point_lst):
    penup()
    goto(point_lst[0])
    pendown()

    for point in point_lst:
        line(point, point_lst[-1])

def cuboid(x,y,z,w,l,a,draw):
    w_ = math.sqrt(w**2 + w**2)
    l_ = math.sqrt(l**2 + l**2)
    y_ = 400

    h_ = math.sqrt(w_**2 + l_**2) 
    print(math.degrees(math.asin(w_/h_)))
    point1 = [x+w_, y+y_, z+l_, h_, math.degrees(math.asin(w_/h_))]
    point2 = [x+w_, y-y_, z+l_, h_, math.degrees(math.asin(w_/h_))] 
    point3 = [x+w_, y+y_, z-l_, h_, math.degrees(math.asin(w_/h_))]
    point4 = [x+w_, y-y_, z-l_, h_, math.degrees(math.asin(w_/h_))]
    point5 = [x-w_, y+y_, z+l_, h_, math.degrees(math.asin(-w_/h_))]
    point6 = [x-w_, y-y_, z+l_, h_, math.degrees(math.asin(-w_/h_))]
    point7 = [x-w_, y+y_, z-l_, h_, math.degrees(math.asin(-w_/h_))]
    point8 = [x-w_, y-y_, z-l_, h_, math.degrees(math.asin(-w_/h_))]

    point1 = point(x+math.cos(math.radians(point1[4]+a))*w_, point1[1], z+math.sin(math.radians(point1[4]+a))*l_)
    point2 = point(x+math.cos(math.radians(point2[4]+a))*w_, point2[1], z+math.sin(math.radians(point2[4]+a))*l_)
    point3 = point(x-math.cos(math.radians(point3[4]+a))*w_, point3[1], z-math.sin(math.radians(point3[4]+a))*l_)
    point4 = point(x-math.cos(math.radians(point4[4]+a))*w_, point4[1], z-math.sin(math.radians(point4[4]+a))*l_)
    point5 = point(x+math.cos(math.radians(point5[4]+a))*w_, point5[1], z+math.sin(math.radians(point5[4]+a))*l_)
    point6 = point(x+math.cos(math.radians(point6[4]+a))*w_, point6[1], z+math.sin(math.radians(point6[4]+a))*l_)
    point7 = point(x-math.cos(math.radians(point7[4]+a))*w_, point7[1], z-math.sin(math.radians(point7[4]+a))*l_)
    point8 = point(x-math.cos(math.radians(point8[4]+a))*w_, point8[1], z-math.sin(math.radians(point8[4]+a))*l_)

    line(point1,point2)
    line(point3,point4)
    line(point5,point6)
    line(point7,point8)
    line(point1,point5)
    line(point1,point7)
    line(point3,point5)
    line(point3,point7)
    line(point2,point6)
    line(point2,point8)
    line(point4,point6)
    line(point4,point8)
