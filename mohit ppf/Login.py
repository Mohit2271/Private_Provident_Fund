from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import Menu

conn = sqlite3.Connection('users.db')
cursor = conn.cursor()
cursor.execute("create table if not exists users(username text  unique, password text, email text unique)")

def open_main_menu():
    root = Tk()
    obj = Menu.Menu(root)
    obj.create_widgets(root)
    root.mainloop()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.configure(bg="#04D8B2")
        Label(self.root, text="Log In", font=("times new roman", 30, "bold"),bg="#04D8B2", fg="black", anchor="w", padx=10).place(x=820, y=150, relwidth=1)

        self.email = StringVar()
        self.password = StringVar()

        self.image_label = Label(root,bg="#04D8B2")
        self.image_label.place(x=50, y=100, width=500, height=350)
        self.image = Image.open("images\login.jpg")
        self.image = self.image.resize((500, 500))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

        email_label = Label(root, text="Email",bg="#04D8B2", font=("times new roman", 12, "bold"))
        email_label.place(x=800, y=250)
        self.email_entry = Entry(root, textvariable=self.email)
        self.email_entry.place(x=900, y=250)

        password_label = Label(root, text="Password",bg="#04D8B2", font=("times new roman", 12, "bold"))
        password_label.place(x=800, y=300)
        self.password_entry = Entry(root, show="*", textvariable=self.password)
        self.password_entry.place(x=900, y=300)

        self.show_password_img = ImageTk.PhotoImage(Image.open("images/show.png").resize((15,14)))
        self.hide_password_img = ImageTk.PhotoImage(Image.open("images/hide.png").resize((15, 15)))

        self.show_password = False

        self.toggle_password_button = Button(self.root, image=self.show_password_img, relief="flat", bd=0, command=self.toggle_password,bg="white",activebackground="white")
        self.toggle_password_button.place(x=1005, y=302)

        forgot_password_label = Label(root, text="Forgot Password?", fg="blue", cursor="hand2",bg="#04D8B2")
        forgot_password_label.place(x=920, y=350)
        forgot_password_label.bind("<Button-1>", lambda event: self.forgot_password())

        submit_button = Button(root, text="Login", command=self.validate_login,font=("times new roman",10,"bold"), cursor="hand2")
        submit_button.place(x=850, y=400)

        back_button = Button(root, text="Back to Menu", command=self.back_to_menu,font=("times new roman",10,"bold"), cursor="hand2")
        back_button.place(x=950,y=400)

    def toggle_password(self):
        if self.show_password:
            self.password_entry.config(show="*")
            self.toggle_password_button.config(image=self.show_password_img)
        else:
            self.password_entry.config(show="")
            self.toggle_password_button.config(image=self.hide_password_img)

        self.show_password = not self.show_password

    def back_to_menu(self):
        self.root.destroy()
        import Menu 
        root = Tk()
        Menu=Menu.Menu(root)
        root.mainloop()

    def back_to_menu(self):
        self.root.destroy()
        open_main_menu()

    def validate_login(self):
        email = self.email.get()
        password = self.password.get()

        if not email or not password:
            messagebox.showerror("Error", "email and password are required!")
            return

        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()

        if user is None:
            messagebox.showerror("Error", "Invalid email or password")
        else:
            messagebox.showinfo("Success", "Login successful")
            self.root.destroy()
            self.open_main_menu(user[2])
            
    def open_main_menu(self,email):
        import Main_menu
        root = Tk()
        Main_menu.Main_Menu(root, email)
        root.mainloop()

    def forgot_password(self):
        self.root.destroy()
        import Forgot_Password
        root=Tk()
        Forgot_Password.ForgetPasswordForm(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()

