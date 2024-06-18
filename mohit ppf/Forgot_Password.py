from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(username TEXT UNIQUE, password TEXT, email TEXT UNIQUE)")

class ForgetPasswordForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("1000x500")
        self.root.config(bg="#04D8B2")
        Label(self.root, text="Forgot Your Password?", font=("times new roman", 20, "bold"), bg="#04D8B2", fg="black",
              anchor="w", padx=10).place(x=650, y=80, relwidth=1)

        self.create_login_page()

    def create_login_page(self):
        self.image_label = Label(self.root, bg="#04D8B2")
        self.image_label.place(x=30, y=100, width=550, height=300)
        self.image = Image.open("images/password.jpg")
        self.image = self.image.resize((500, 500))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

        self.email_label = Label(self.root, text="Email:", font=("times new roman", 12, "bold"), bg="#04D8B2")
        self.email_label.place(x=700, y=200)
        self.email_entry = Entry(self.root)
        self.email_entry.place(x=800, y=200)

        self.next_button = Button(self.root, text="Next", command=self.check_email_and_show_new_password_page,font=("times new roman",10,"bold"))
        self.next_button.place(x=770, y=250)

    def check_email_and_show_new_password_page(self):
        email = self.email_entry.get()

        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()

        if user:
            self.show_new_password_page()
        else:
            messagebox.showerror("Error", "Email not found.")

    def create_new_password_page(self):
        self.email_label.place_forget()
        self.email_entry.place_forget()
        self.next_button.place_forget()

        self.new_password_label = Label(self.root, text="New Password:", font=("times new roman", 12, "bold"), bg="#04D8B2")
        self.new_password_label.place(x=650, y=200)
        self.new_password_entry = Entry(self.root, show="*")
        self.new_password_entry.place(x=800, y=200)

        self.show_password_img = ImageTk.PhotoImage(Image.open("images/show.png").resize((15,14)))
        self.hide_password_img = ImageTk.PhotoImage(Image.open("images/hide.png").resize((15, 15)))

        self.show_password = False

        self.toggle_password_button = Button(self.root, image=self.show_password_img, relief="flat", bd=0, command=self.toggle_password,bg="white",activebackground="white")
        self.toggle_password_button.place(x=900, y=202)

        self.confirm_password_label = Label(self.root, text="Confirm Password:", font=("times new roman", 12, "bold"), bg="#04D8B2")
        self.confirm_password_label.place(x=650, y=250)
        self.confirm_password_entry = Entry(self.root, show="*")
        self.confirm_password_entry.place(x=800, y=250)

        self.show_password1_img = ImageTk.PhotoImage(Image.open("images/show.png").resize((15,14)))
        self.hide_password1_img = ImageTk.PhotoImage(Image.open("images/hide.png").resize((15, 15)))

        self.show_password1 = False

        self.toggle_confirm_password_button = Button(self.root, image=self.show_password1_img, relief="flat", bd=0, command=self.toggle_confirm_password,bg="white",activebackground="white")
        self.toggle_confirm_password_button.place(x=900, y=252)

        self.submit_button = Button(self.root, text="Submit", command=self.submit_new_password,font=("times new roman",10,"bold"))
        self.submit_button.place(x=770, y=300)

        back_button = Button(self.root, text="Back to Menu", command=self.back_to_menu,font=("times new roman",10,"bold"), cursor="hand2")
        back_button.place(x=830,y=300)

    def toggle_password(self):
        if self.show_password:
            self.new_password_entry.config(show="*")
            self.toggle_password_button.config(image=self.show_password_img)
        else:
            self.new_password_entry.config(show="")
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
        import Login 
        root = Tk()
        Login.Login(root)
        root.mainloop()

    def show_new_password_page(self):
        self.create_new_password_page()

    def submit_new_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password == confirm_password:
            email = self.email_entry.get()

            if not any(char.isupper() for char in new_password):
                messagebox.showinfo("Invalid", "Password must contain at least one uppercase letter.")
                return
            if not any(char.islower() for char in new_password):
                messagebox.showinfo("Invalid", "Password must contain at least one lowercase letter.")
                return
            if not any(char.isdigit() for char in new_password):
                messagebox.showinfo("Invalid", "Password must contain at least one digit.")
                return
            if not any(char in '!@#$%^&*()_+-=[]{}|\\:;"<>,.?/' for char in new_password):
                messagebox.showinfo("Invalid", "Password must contain at least one special character.")
                return

            cursor.execute("SELECT * FROM users WHERE email=?", (email,))
            user = cursor.fetchone()

            if user:
                cursor.execute("UPDATE users SET password=? WHERE email=?", (new_password, email))
                conn.commit()
                messagebox.showinfo("Success", "Password updated successfully!")
                self.back_to_menu()
            else:
                messagebox.showerror("Error", "Email not found.")
        else:
            messagebox.showerror("Error", "Passwords do not match.")

if __name__ == "__main__":
    root = Tk()
    forget_password_form = ForgetPasswordForm(root)
    root.mainloop()
