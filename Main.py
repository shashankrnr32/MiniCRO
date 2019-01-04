'''
Python Mini CRO
Developer : Shashank Sharma
'''
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import csv
import tkinter as tk
from tkinter import font

pause = False
pos=[0]
with open('DATA.csv', 'r') as f:
    reader = csv.reader(f)
    ls = list(reader)
ls = [float(x[0]) for x in ls]

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(-2.5, 2.5))
line, = ax.plot([], [], lw=2)

def configRight():
    right = tk.Button(frame,text=u"\u25b6 \nMove Right",command=lambda : rightShift(pos,fig))
    right.pack()
    right.config(height=3,width=20)
    right.config(bg='#E53935',font=Font)
    return right
def configLeft():
    left = tk.Button(frame,text=u"\u25c0 \nMove Left",command=lambda :  leftShift(pos,fig))
    left.pack()
    left.config(height=3,width=20)
    left.config(bg='#E53935',font=Font)
    return left
def configStart():
    startBut = tk.Button(frame,text=u"\u23e9 \nStart",command=start)
    startBut.pack()
    startBut.config(height=3,width=20)
    startBut.config(bg='#E53935',font=Font)
    return startBut
def configPause():
    stop = tk.Button(frame,text=u"\u23f8 \nPause",command=pause)
    stop.pack()
    stop.config(height=3,width=20)
    stop.config(bg='#E53935',font=Font)
    return stop

def rightShift(i,fig):
    x = np.linspace(0,49,50)
    pos[0]+=10
    line.set_data(x,ls[pos[0]:pos[0]+50])
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    
def leftShift(i,fig):
    x = np.linspace(0,49,50)
    if pos[0]>10 : pos[0]-=10
    line.set_data(x,ls[pos[0]:pos[0]+50])
    fig.canvas.draw()
    fig.canvas.flush_events()
    
def start():
    global pause
    pause = False
    
    
def pause():
    global pause
    pause=True
    
    
def init():
    x = np.linspace(0,49,50)
    line.set_data(x,ls[pos[0]:pos[0]+50])
    return line,

def animate(i):
    x = np.linspace(0,49,50)
    if not pause:
        pos[0]+=1
        line.set_data(x,ls[pos[0]:pos[0]+50]) 
    return line,
    


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
Font = font.Font(family='Yu Gothic UI', size=15)

#configure Buttons
right = configRight()
left = configLeft()
startBut = configStart()
stopBut = configPause()
#configure primary plot
x = np.linspace(0,49,50)
line.set_data(x,ls[pos[0]:pos[0]+50])


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(ls), interval=100, blit=True,repeat=True)

root.mainloop()
plt.show()