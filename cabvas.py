import tkinter as tk

def draw_scene(canvas):
    canvas.delete('all')

    canvas.create_rectangle(50, 150, 150, 250, fill='brown')
    canvas.create_polygon(50, 150, 150, 150, 100, 100, fill='pink')

    canvas.create_oval(200, 50, 250, 100, fill='yellow')

    for i in range(0, 400, 10):
        canvas.create_arc(i, 230, i+7, 280, start=0, extent=100, fill='green')
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
draw_scene(canvas)
root.mainloop()