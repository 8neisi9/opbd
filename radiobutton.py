import tkinter as tk

def show_selected():
    selected_value = var.get()
    if selected_value == 1:
        label.config(text="89002222222")
    elif selected_value == 2:
        label.config(text="89001232323")
    elif selected_value == 3:
        label.config(text="89003443456)

root = tk.Tk()
root.title("Прога")

var = tk.IntVar()
var.set(1)

label = tk.Label(root, text="")
label.pack(side='right')

radio_button1 = tk.Radiobutton(root, text="петя", variable=var, value=1, indicatoron=0, command=show_selected)
radio_button1.pack()

radio_button2 = tk.Radiobutton(root, text="Вася", variable=var, value=2, indicatoron=0, command=show_selected)
radio_button2.pack()

radio_button3 = tk.Radiobutton(root, text="коля", variable=var, value=3, indicatoron=0, command=show_selected)
radio_button3.pack()



root.mainloop()