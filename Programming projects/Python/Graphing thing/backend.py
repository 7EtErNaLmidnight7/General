from turtle import *

# All the random numbers look a bit complicated, and they are :)
# It makes sure the graph is centred with the screen because turtle is wierd with co-ordinates

def setup(): # Sets up co-ordinate stuff
    title("Graph")
    speed(0)
    penup()
    goto(-540, 0)
    pendown()

def draw(point_lst):
    # These bits make sure that the graph looks relatively clean
    Xmultiplier = 1080 / len(point_lst)
    Ymultiplier = 200 / max(point_lst)
    i = 1

    for point in point_lst:
        goto(i*Xmultiplier-540, point*Ymultiplier)
        i += 1

    end(point_lst)   

def end(point_lst):
    exitonclick() # You can use this to find the value of any point
    
    while True:
        try:
            point = int(input())
            print("\n",point_lst[point])
        except:
            print("Invalid index")
    
    

