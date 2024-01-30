from tkinter import *

def motion(event):
    target_x = event.x
    current_x = c.coords(ball)[0]

    if current_x < target_x:
        c.move(ball, 1, 0)
        root.after(10, motion, event)
    elif current_x > target_x:
        c.move(ball, -1, 0)
        root.after(10, motion, event)

root = Tk()
c = Canvas(root, width=300, height=200)
c.pack()
ball = c.create_oval(0, 100, 50, 150, fill='pink')

c.bind("<Button-1>", motion)

root.mainloop()