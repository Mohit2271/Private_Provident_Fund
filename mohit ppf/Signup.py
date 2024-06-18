import re
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import Menu

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("create table if not exists users(username text, password text, email text unique)")

def open_main_menu():
    root = Tk()
    obj = Menu.Menu(root)
    obj.create_widgets(root)
    root.mainloop()

class SignUpPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("1550x800+0+0")
        self.root.configure(bg="#04D8B2")
        Label(self.root, text="Sign Up", font=("times new roman", 30, "bold"), bg="#04D8B2", fg="black", anchor="w", padx=10).place(x=850, y=150, relwidth=1)

        self.name = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()

        self.image_label = Label(root)
        self.image_label.place(x=50, y=150, width=500, height=360)

        self.image = Image.open("images/sign-up1.jpg")
        self.image = self.image.resize((500, 500))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

        self.name_label = Label(root, text="Name:", font=("times new roman", 12, "bold"), bg="#04D8B2")
        self.name_label.place(x=800, y=250)
        self.name_entry = Entry(root, textvariable=self.name)
        self.name_entry.place(x=950, y=250)

        self.email_label = Label(root, text="Email:", font=("times new roman", 12, "bold"), bg="#04D8B2")
        self.email_label.place(x=800, y=300)
        self.email_entry = Entry(root, textvariable=self.email)
        self.email_entry.place(x=950, y=300)

        self.password_label = Label(root, text="Password:", font=("times new roman", 12, "bold"), bg="#04D8B2")
        self.password_label.place(x=800, y=350)
        self.password_entry = Entry(root, show="*", textvariable=self.password)
        self.password_entry.place(x=950, y=350)

        self.show_password_img = ImageTk.PhotoImage(Image.open("images/show.png").resize((15, 14)))
        self.hide_password_img = ImageTk.PhotoImage(Image.open("images/hide.png").resize((15, 15)))

        self.show_password = False

        self.toggle_password_button = Button(self.root, image=self.show_password_img, relief="flat", bd=0, command=self.toggle_password, bg="white", activebackground="white")
        self.toggle_password_button.place(x=1055, y=352)

        self.valid_label = Label(root, text="(Password must contain uppercase, lowercase, special character, and number)", bg="#04D8B2", font=("times new roman", 9))
        self.valid_label.place(x=1100, y=350)

        self.confirm_password_label = Label(root, text="Confirm Password:", font=("times new roman", 12, "bold"), bg="#04D8B2")
        self.confirm_password_label.place(x=800, y=400)
        self.confirm_password_entry = Entry(root, show="*", textvariable=self.confirm_password)
        self.confirm_password_entry.place(x=950, y=400)

        self.show_password1_img = ImageTk.PhotoImage(Image.open("images/show.png").resize((15, 14)))
        self.hide_password1_img = ImageTk.PhotoImage(Image.open("images/hide.png").resize((15, 15)))

        self.show_password1 = False

        self.toggle_confirm_password_button = Button(self.root, image=self.show_password1_img, relief="flat", bd=0, command=self.toggle_confirm_password, bg="white", activebackground="white")
        self.toggle_confirm_password_button.place(x=1055, y=402)

        self.signin_button = Button(root, text="Sign Up", command=self.submit_form, font=("times new roman", 12, "bold"), cursor="hand2")
        self.signin_button.place(x=800, y=450)

        back_button = Button(root, text="Back to Menu", command=self.back_to_menu, font=("times new roman", 10, "bold"), cursor="hand2")
        back_button.place(x=950, y=450)

    def toggle_password(self):
        if self.show_password:
            self.password_entry.config(show="*")
            self.toggle_password_button.config(image=self.show_password_img)
        else:
            self.password_entry.config(show="")
            self.toggle_password_button.config(image=self.hide_password_img)

        self.show_password = not self.show_password

    def toggle_confirm_password(self):
        if self.show_password1:
            self.confirm_password_entry.config(show="*")
            self.toggle_confirm_password_button.config(image=self.show_password1_img)
        else:
            self.confirm_password_entry.config(show="")
            self.toggle_confirm_password_button.config(image=self.hide_password1_img)

        self.show_password1 = not self.show_password1
    
    def back_to_menu(self):
        self.root.destroy()
        open_main_menu()

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not name or not email or not password or not confirm_password:
            messagebox.showinfo("Invalid", "All fields are required")
            return

        if len(name.strip()) < 4 or len(name.strip()) > 20:
            messagebox.showerror("Error", "Name should contain 4 to 20 characters")
            return
        elif not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Name should only contain alphabetic characters.")
            return
        elif password != confirm_password:
            messagebox.showinfo("Invalid", "Passwords must match.")
            return

        elif not re.match(r'^[\w\d]{4,}@[\w]{3,10}\.(com|co\.in|org)$', email):
            messagebox.showinfo("Invalid", "Please enter a valid email address.")
            return

        if not any(char.isupper() for char in password):
            messagebox.showinfo("Invalid", "Password must contain at least one uppercase letter.")
            return
        elif not any(char.islower() for char in password):
            messagebox.showinfo("Invalid", "Password must contain at least one lowercase letter.")
            return
        elif not any(char.isdigit() for char in password):
            messagebox.showinfo("Invalid", "Password must contain at least one digit.")
            return
        elif not any(char in '!@#$%^&*()_+-=[]{}|\\:;"<>,.?/' for char in password):
            messagebox.showinfo("Invalid", "Password must contain at least one special character.")
            return

        cursor.execute('SELECT email FROM users WHERE email = ?', (email,))
        if cursor.fetchone() is not None:
            messagebox.showinfo("Invalid", "Email already exists")
        else:
            cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (name, password, email))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful.")

        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.confirm_password_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = SignUpPage(root)
    root.mainloop()





























































































































































































# import re
# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import sqlite3
# import Menu

# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()
# cursor.execute("create table if not exists users(username text, password text, email text unique)")

# def open_main_menu():
#     root = Tk()
#     obj = Menu.Menu(root)
#     obj.create_widgets(root)
#     root.mainloop()

# class SignUpPage:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sign Up")
#         self.root.geometry("1550x800+0+0")
#         self.root.configure(bg="#04D8B2")
#         Label(self.root, text="Sign Up", font=("times new roman", 30, "bold"), bg="#04D8B2", fg="black", anchor="w", padx=10).place(x=850, y=150, relwidth=1)

#         self.name = StringVar()
#         self.email = StringVar()
#         self.password = StringVar()
#         self.confirm_password = StringVar()

#         self.image_label = Label(root)
#         self.image_label.place(x=50, y=150, width=500, height=360)

#         self.image = Image.open("images/sign-up1.jpg")
#         self.image = self.image.resize((500, 500))
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.image_label.config(image=self.photo)

#         self.name_label = Label(root, text="Name:", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         self.name_label.place(x=800, y=250)
#         self.name_entry = Entry(root, textvariable=self.name)
#         self.name_entry.place(x=950, y=250)
#         self.name_entry.bind("<KeyRelease>", self.validate_name)

#         self.email_label = Label(root, text="Email:", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         self.email_label.place(x=800, y=300)
#         self.email_entry = Entry(root, textvariable=self.email)
#         self.email_entry.place(x=950, y=300)
#         self.email_entry.bind("<KeyRelease>", self.validate_email)

#         self.password_label = Label(root, text="Password:", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         self.password_label.place(x=800, y=350)
#         self.password_entry = Entry(root, show="*", textvariable=self.password)
#         self.password_entry.place(x=950, y=350)
#         self.password_entry.bind("<KeyRelease>", self.validate_password)

#         self.show_password_img = ImageTk.PhotoImage(Image.open("images/show.png").resize((15, 14)))
#         self.hide_password_img = ImageTk.PhotoImage(Image.open("images/hide.png").resize((15, 15)))

#         self.show_password = False

#         self.toggle_password_button = Button(self.root, image=self.show_password_img, relief="flat", bd=0, command=self.toggle_password, bg="white", activebackground="white")
#         self.toggle_password_button.place(x=1055, y=352)

#         self.valid_label = Label(root, text="(Password must contain uppercase, lowercase, special character, and number)", bg="#04D8B2", font=("times new roman", 9))
#         self.valid_label.place(x=1100, y=350)

#         self.confirm_password_label = Label(root, text="Confirm Password:", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         self.confirm_password_label.place(x=800, y=400)
#         self.confirm_password_entry = Entry(root, show="*", textvariable=self.confirm_password)
#         self.confirm_password_entry.place(x=950, y=400)
#         self.confirm_password_entry.bind("<KeyRelease>", self.validate_confirm_password)

#         self.show_password1_img = ImageTk.PhotoImage(Image.open("images/show.png").resize((15, 14)))
#         self.hide_password1_img = ImageTk.PhotoImage(Image.open("images/hide.png").resize((15, 15)))

#         self.show_password1 = False

#         self.toggle_confirm_password_button = Button(self.root, image=self.show_password1_img, relief="flat", bd=0, command=self.toggle_confirm_password, bg="white", activebackground="white")
#         self.toggle_confirm_password_button.place(x=1055, y=402)

#         self.signin_button = Button(root, text="Sign Up", command=self.submit_form, font=("times new roman", 12, "bold"), cursor="hand2")
#         self.signin_button.place(x=800, y=450)

#         back_button = Button(root, text="Back to Menu", command=self.back_to_menu, font=("times new roman", 10, "bold"), cursor="hand2")
#         back_button.place(x=950, y=450)

#         self.name_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.name_error_label.place(x=950, y=280)

#         self.email_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.email_error_label.place(x=950, y=330)

#         self.password_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.password_error_label.place(x=950, y=380)

#         self.confirm_password_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.confirm_password_error_label.place(x=950, y=380)

#     def toggle_password(self):
#         if self.show_password:
#             self.password_entry.config(show="*")
#             self.toggle_password_button.config(image=self.show_password_img)
#         else:
#             self.password_entry.config(show="")
#             self.toggle_password_button.config(image=self.hide_password_img)

#         self.show_password = not self.show_password

#     def toggle_confirm_password(self):
#         if self.show_password1:
#             self.confirm_password_entry.config(show="*")
#             self.toggle_confirm_password_button.config(image=self.show_password1_img)
#         else:
#             self.confirm_password_entry.config(show="")
#             self.toggle_confirm_password_button.config(image=self.hide_password1_img)

#         self.show_password1 = not self.show_password1
    
#     def back_to_menu(self):
#         self.root.destroy()
#         open_main_menu()

#     def validate_name(self, event):
#         name = self.name_entry.get()

#         if len(name.strip()) < 4 or len(name.strip()) > 20:
#             self.name_error_label.config(text="Name should contain 4 to 20 characters")
#         elif not name.replace(" ", "").isalpha():
#             self.name_error_label.config(text="Name should only contain alphabetic characters.")
#         else:
#             self.name_error_label.config(text="")

#     def validate_email(self, event):
#         email = self.email_entry.get()

#         if not re.match(r'^[\w\d]{4,}@[\w]{3,10}\.(com|co\.in|org)$', email):
#            self.email_error_label.config(text="Please enter a valid email address.")
#         else:
#             self.email_error_label.config(text="")

#     def validate_password(self,event):
#         password = self.password_entry.get()

#         if not any(char.isupper() for char in password):
#             self.password_error_label.config(text="Password must contain at least one uppercase letter")
#             return
#         elif not any(char.islower() for char in password):
#             self.password_error_label.config(text="Password must contain at least one lowercase letter")
#             return
#         elif not any(char.isdigit() for char in password):
#             self.password_error_label.config(text="Password must contain at least one digit")
#             return
#         elif not any(char in '!@#$%^&*()_+-=[]{}|\\:;"<>,.?/' for char in password):
#             self.password_error_label.config(text="Password must contain at least one special character")
#             return
#         else:
#             self.password_error_label.config(text="")

#     def validate_confirm_password(self,event):
#         confirm_password = self.confirm_password_entry.get()
#         password = self.password_entry.get()

#         if password != confirm_password:
#             self.confirm_password_error_label.config(text="Passwords must match")
#             return
#         else:
#             self.confirm_password_error_label.config(text="")

#     def submit_form(self):
#         name = self.name_entry.get()
#         email = self.email_entry.get()
#         password = self.password_entry.get()
#         confirm_password = self.confirm_password_entry.get()

#         if not name or not email or not password or not confirm_password:
#             messagebox.showinfo("Invalid", "All fields are required")
#             return

#         cursor.execute('SELECT email FROM users WHERE email = ?', (email,))
#         if cursor.fetchone() is not None:
#             messagebox.showinfo("Invalid", "Email already exists")
#         else:
#             cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (name, password, email))
#             conn.commit()
#             messagebox.showinfo("Success", "Registration successful.")

#         self.name_entry.delete(0, END)
#         self.email_entry.delete(0, END)
#         self.password_entry.delete(0, END)
#         self.confirm_password_entry.delete(0, END)

# if __name__ == "__main__":
#     root = Tk()
#     obj = SignUpPage(root)
#     root.mainloop()
