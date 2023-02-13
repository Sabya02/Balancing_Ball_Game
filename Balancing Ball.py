import turtle
import random as r
import tkinter as tk
import time

from turtle import TurtleScreen,RawTurtle
from tkinter import messagebox as msg

win=tk.Tk()
win.geometry("900x690")
win.title("BALANCING BALL")
win.resizable(width="False",height="False")
win["bg"]="teal"
#win.tracer(40)

def start():
    canvas=tk.Canvas(win,width=850,height=600,bg="black")
    canvas.place(x=20,y=10)
    screen=TurtleScreen(canvas)
    #screen.addshape("H:\\Data\\football img.png")
    screen.width=800
    screen.height=600
    screen.bgcolor('#27d676')
    screen.tracer(40)

    #creating a paddle
    paddle = RawTurtle(screen)
    paddle.shape('square')
    paddle.shapesize(1,5)
    #paddle.shapesize(stretch_len=5,stretch_wid=1)
    paddle.color('orange')
    paddle.penup()
    paddle.goto(0,-270)

    #creating a ball:
    ball=RawTurtle(screen)
    ball.shape('circle')
    ball.shapesize(2)
    ball.color('red')
    ball.speed(0)
    ball.up()
    ball.dx=2
    ball.dy=-2

    #for pen
    pen=RawTurtle(screen)
    pen.color('black')
    pen.up()
    pen.ht()
    pen.goto(310,-220)
    pen.write('Score:0',align='center',font=('Agency FB',24,'normal'))
    c=['red','blue','green','cyan','purple','yellow','orange']
    score=0

    #key bindings:
    def paddle_right():
        if paddle.xcor()<350:
            paddle.setx(paddle.xcor()+80)
    def paddle_left():
        if paddle.xcor()>-350:
            paddle.setx(paddle.xcor()-80)

    def border_check():
        if ball.ycor()>280:
            ball.dy *= -1
        if ball.xcor()>380 or ball.xcor()<-380:
            ball.dx *= -1

    def paddle_check():
        if ball.ycor()-10<=paddle.ycor()+10 and ball.dy<0:
            if ball.xcor()-10<=paddle.xcor()+50 and ball.xcor()+10>=paddle.xcor()-50:
                ball.dy *= -1


    def falling_block():
        for i in block_list:
            if i.state=="falling":
                i.shape('circle')
                i.l=i.xcor()-10
                i.r=i.xcor()+10
                i.shapesize(1,1)
                i.goto(i.xcor(),i.ycor()+i.dy)


    screen.listen()
    screen.onkeypress(paddle_right,"Right")
    screen.onkeypress(paddle_left,"Left")

    x_list=[-340,-230,-120,-10,100,210,320]
    y_list=[280,255,230,205,180]
    block_list=[]
    for i in y_list:
        for j in x_list:
            block=RawTurtle(screen)
            block.shape('circle')
            r.shuffle(c)
            block.color(c[0])
            block.up()
            block.goto(j,i)
            block.state='ready'
            block.l=block.xcor()-50
            block.r=block.xcor()+50
            block_list.append(block)
    block_count=len(block_list)

    x=0.015
    while block_count>0:
        if score<=10:
            x=0.015
        else:
            x=0.011
        time.sleep(x)

        screen.update()
        ball.goto(ball.xcor()+ball.dx,ball.ycor()+ball.dy)
        border_check()
        paddle_check()
        falling_block()


        #Autopiolot:
        #if ball.xcor()>-350 and ball.xcor()<350:
            #paddle.setx(ball.xcor())

        if ball.ycor()<=-300:
            ball.goto(0,0)
            if score>0:
                score -=1
            pen.clear()
            pen.write(f'Score: {score}',align='center',font=('Agency FB',24,'normal'))


        #Block_collision:
        for i in  block_list:
            if(i.l<=ball.xcor()<=i.r) and (i.ycor()-10<=ball.ycor()<=i.ycor()+10)and i.state=='ready':
                ball.dy *=-1
                i.state='falling'
                i.dy=-2
                score+=1
                pen.clear()
                #paddle.color(i,c)
                pen.clear()
                pen.write(f'Score: {score}',align='center',font=('Agency FB',24,'normal'))

            if(paddle.xcor()-50<i.xcor()<paddle.xcor()+50)and(paddle.ycor()-10<i.ycor()<=paddle.ycor()-10) and i.dy<0:
                i.dy *=-1
            if i.ycor()<-320 or i.ycor()>320:
                block_list.remove(i)
                block_count=len(block_list)

    #Game Over:
    pen.clear()
    pen.goto(0,0)
    pen.write(f"GAME OVER\nScore:(score)",align='center',font=('Agency FB',24,'normsl'))





#start()

start_Button=tk.Button(win,text="START",font=("Agency FB",20),width=20,height=1,
                       bg="tomato",fg="white",bd=4,activebackground="yellow",command=start)
start_Button.place(x=350,y=620)

win.mainloop()
