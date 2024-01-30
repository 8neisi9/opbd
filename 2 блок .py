import tkinter as tk

def count_words():
    sentence = entry.get()
    words = sentence.split()
    word_count = len(words)
    result_label.config(text=f"Количество слов: {word_count}")


window = tk.Tk()
window.title("Подсчет слов")
window.geometry("300x200")


entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=20)

button = tk.Button(window, text="Подсчитать", command=count_words)
button.pack()

result_label = tk.Label(window, text="Количество слов: 0", font=("Arial", 14))
result_label.pack(pady=20)

window.mainloop()