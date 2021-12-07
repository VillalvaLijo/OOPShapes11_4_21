#graphicstest2.py

#12/7/21

#Lord Alya Vijana

#simple graphics animation to test out tkinter

from tkinter import *
import random
import time

tk=Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Bouncing Ball")
canvas.pack()

ball = canvas.create_oval(10, 10, 60, 60, fill = "blue")
xspeed = 2
yspeed = 3

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] >= 400 or pos[1] <= 0:
        yspeed = -yspeed
    if pos[2] >= 500 or pos[0] <= 0:
        xspeed = -xspeed
    tk.update()
  

tk.mainloop()
