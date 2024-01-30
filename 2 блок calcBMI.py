import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height/100) ** 2
    result_label.config(text=f"BMI: {bmi:.2f}")
window = tk.Tk()
window.title("Калькулятор BMI")
weight_label = tk.Label(window, text="Вес (кг):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()
height_label = tk.Label(window, text="Рост (см):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()


calculate_button = tk.Button(window, text="Рассчитать", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()