import turtle as t
angle=90
def draw_side(width,height):
    t.forward(height)
    t.right(angle)
    t.forward(width)
    t.right(angle)
    t.forward(height)
    t.right(angle)
    t.forward(width)
    t.right(angle)


def draw_rectangle(x, y,width,height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    draw_side(width, height)
    t.end_fill()
    
    center_x= x + height*1/2
    center_y= y - width*1/2
    return center_x, center_y

def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y-radius) 
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_flagpole(x, y, height,color,radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    draw_side(height, 5)
    t.end_fill()

def draw_flag(x,y, scale_factor):
    height=150*scale_factor
    width=100*scale_factor
    radius=20*scale_factor
    
    center_X, center_Y= draw_rectangle(x, y, width, height, "red")
    draw_circle(center_X, center_Y,radius, 'white')
    draw_flagpole(x-10, y, height,'black',radius)
    draw_flag




def main():
    t.bgcolor('lightblue')
    draw_flag(-200, 50, 2)
    draw_flag(150, -80, 1)

    


    t.done

main()
