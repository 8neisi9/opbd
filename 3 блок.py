import customtkinter as ctk
from tkinter import messagebox
from CTkListbox import *

class LoginWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Login")
        self.geometry("300x300")

        self.username_label = ctk.CTkLabel(self, text="Логин:")
        self.username_label.pack()
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack()

        self.password_label = ctk.CTkLabel(self, text="Пароль:")
        self.password_label.pack()
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack()

        self.login_button = ctk.CTkButton(self, text="Login", command=self.on_login)
        self.login_button.pack()

    def on_login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin1":
            self.master.show_main_window()
            self.destroy()
        else:
            messagebox.showerror("ошибка", "Неправильный логин или пароль")

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.login_window = LoginWindow(self)
        self.login_window.lift()

        self.task_list = []
        self.main_window = None

    def show_main_window(self):
        self.main_window = MainWindow(self)
        self.deiconify()

class MainWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("zxc")
        self.geometry("400x500")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()