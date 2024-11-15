import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

#setup screen

win = turtle.Screen()
win.title("Snack game")
win.bgcolor("Green")
win.setup(width=600 , height=600)
win.tracer(0) #turns off the screen updates

#snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction  = "stop"

#snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score :0 High Score :0", align="center",font=("Courier",24,"normal"))

#functons

def go_up():
    if head.direction !="down":
        head.direction ="up"

def go_down():
    if head.direction !="up":
       head.direction = "down"

def go_left(): 
    if head.direction !="right":
       head.direction = "left"

def go_right(): 
    if head.direction !="left":
       head.direction = "right"

def move(): 
    if head.direction =="up":
       y = head.ycor()
       head.sety(y+20)

    if head.direction =="down":
       y = head.ycor()
       head.sety(y-20)   

    if head.direction =="left":
       x = head.xcor()
       head.setx(x-20)   
                     
    if head.direction =="right":
       x = head.xcor()
       head.setx(x+20)   
               
 # keyboard button set / binding

win.listen()
win.onkeypress(go_up,"8")
win.onkeypress(go_down,"2")
win.onkeypress(go_left,"4")
win.onkeypress(go_right,"6")

#main game loop

while True:
    win.update()

    #check collision with border

    if  head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #middle segments

        for segment in segments:
            segment.goto(1000,1000)

        #clear the segment list

        segments.clear()
        # reset the score

        score = 0
        #reset the delay 
        delay = 0.1    
        pen.clear()
        pen.write("Score: {} High Score: {} ". format(score, high_score),align="center",font=("courier", 24, "normal"))

        #check for collision with food
    if head.distance(food)<20:
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)

            #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

            #shorten delay
        delay -=0.001
            #increase score
        score +=10
        if score > high_score:
            high_score= score

        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("courierss", 24, "normal"))                     
       
            #move end segment in reverse order

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
                # move segment 0 at where  head is

    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
            # check for head collision with the body segments
            
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

                    #hide the premade segments/tail

            for segments in segments:
                        segments.goto(1000,1000)

                    #clear segment list

            segments.clear()

                    #reset the score

            score = 0

                    #reset the delay
            delay =0.1

                    #updte te score display

            pen.clear()
            pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("courierss", 24, "normal"))
    time.sleep(delay)
win.mainloop()
            

                         

            

