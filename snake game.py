# snake game

# imports modules
import turtle
import random
import time

# outputs a message
print("Snake Game\n")

# creates the background
background = turtle.Screen()
background.bgcolor("black")
background.title("snake game")
background.tracer(0)
background.setup(width=430,height=400)



# creates player head
head = turtle.Turtle()
head.penup()
head.color("red")
head.shape("square")
head.goto(0,0)
head.direction = "stop"
head.cant_move = ""

# set up food
food = turtle.Turtle()
food.penup()
food.color("yellow")
food.goto(0,100)
food.shape("circle")

# initialises variables
gameloop = True
sections = []
delay = 0.12
score = 0

# functions:
def go_up():
    if head.cant_move != "up":
        head.direction = "up"
    if len(sections) > 1:
        head.cant_move = "down"

def go_down():
    if head.cant_move != "down":
        head.direction = "down"
    if len(sections) > 1:
        head.cant_move = "up"

def go_left():
    if head.cant_move != "left":
        head.direction = "left"
    if len(sections) > 1:
        head.cant_move = "right"

def go_right():
    if head.cant_move != "right":
        head.direction = "right"
    if len(sections) > 1:
        head.cant_move = "left"

# moves the player forward
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)



# allows user input
background.listen()
background.onkeypress(go_up,"Up")
background.onkeypress(go_down,"Down")
background.onkeypress(go_left,"Left")
background.onkeypress(go_right,"Right")

# main gameloop
while gameloop:
    # updates the screen
    background.update()

    # stops program for a time
    time.sleep(delay)

    # checks collision of food
    if head.distance(food) < 20:
        # puts food in random location
        food.goto(random.randint(-180,180),random.randint(-180,180))

        # incraments the score
        score += 1

        # creates new body part
        new_section = turtle.Turtle()
        new_section.color("white")
        new_section.shape("square")
        new_section.penup()
        sections.append(new_section)

    # moves body allong
    for i in range(len(sections)-1,0,-1):
        sections[i].goto(sections[i-1].xcor(),sections[i-1].ycor())

    if len(sections) > 0:
        sections[0].goto(head.xcor(),head.ycor())

    if head.xcor() < -200 or head.xcor() > 200 or head.ycor() < -180 or head.ycor() > 180:
        gameloop = False


    for i in range(0,len(sections)-1):
        if head.distance(sections[i]) < 10 and i >= 1:
            gameloop = False

    
    # moves the head
    move()
    
print("Score: " + str(score))

background.mainloop()
