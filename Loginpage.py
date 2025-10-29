import tkinter as tk
from tkinter import messagebox

# Hardcoded credentials for demo
USERNAME = "admin"
PASSWORD = "1234"

# Login App Class
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Login Page")
        self.root.geometry("400x300")

        tk.Label(root, text="Username", font=("Arial", 12)).pack(pady=10)
        self.username_entry = tk.Entry(root, font=("Arial", 12))
        self.username_entry.pack()

        tk.Label(root, text="Password", font=("Arial", 12)).pack(pady=10)
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 12))
        self.password_entry.pack()

        tk.Button(root, text="Login", command=self.check_login, font=("Arial", 12)).pack(pady=20)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == USERNAME and password == PASSWORD:
            messagebox.showinfo("Login Success", "Welcome!")
            self.root.destroy()  # Close login window
            # You can launch QuizWiz here if you want
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
