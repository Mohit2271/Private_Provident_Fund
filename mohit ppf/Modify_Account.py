import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('New_Account.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS New_Account_details (account_number, Addhar_No, Name, Email, Mobile, Salary, Deposit, Gender)")

class Modify_Account:
    def __init__(self, root):
        self.root = root
        self.root.title("Modify_Account")
        self.root.geometry("500x400")
        self.root.config(bg="#04D8B2")
        Label(self.root, text="Modify Account", font=("times new roman",23,"bold"),bg="#04D8B2",fg="black",anchor="w",padx=10).place(x=170,y=60,relwidth=1)

        self.account_number_label = Label(root, text="Account No.:",font=("times new roman",12,"bold"),bg="#04D8B2")
        self.account_number_label.place(x=160,y=130)
        self.account_number_entry = Entry(root)
        self.account_number_entry.place(x=290,y=130)

        self.name_label = Label(root, text="Name:",font=("times new roman",12,"bold"),bg="#04D8B2")
        self.name_label.place(x=160,y=170)
        self.name_entry = Entry(root)
        self.name_entry.place(x=290,y=170)

        self.email_label = Label(root, text="Email:",font=("times new roman",12,"bold"),bg="#04D8B2")
        self.email_label.place(x=160,y=210)
        self.email_entry = Entry(root)
        self.email_entry.place(x=290,y=210)

        self.mobile_number_label = Label(root, text="Mobile Number:",font=("times new roman",12,"bold"),bg="#04D8B2")
        self.mobile_number_label.place(x=160,y=250)
        self.mobile_number_entry = Entry(root)
        self.mobile_number_entry.place(x=290,y=250)

        self.button_modify = Button(root, text="Modify Data",font=("times new roman",10,"bold"), command=self.validate_data, cursor="hand2")
        self.button_modify.place(x=220,y=300)

        back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",font=("times new roman", 10, "bold"))
        back_to_menu_button.place(x=320,y=300)

    def back_to_menu(self):
        self.root.destroy()
        import Main_menu 
        root = Tk()
        email = ""
        Main_menu.Main_Menu(root, email)
        root.mainloop()

    def validate_data(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        mobile_number = self.mobile_number_entry.get()
        account_number = self.account_number_entry.get()

        if not account_number:
            messagebox.showerror("Error", "Account number does not exist!")
        if not name:
            messagebox.showerror("Error", "Name is required!")
        elif not name.replace(' ','').isalpha():
            messagebox.showerror("Error", "Name should contain only alphabets and spaces!")
        elif not email:
            messagebox.showerror("Error", "Email is required!")
        elif not "@" in email or not "." in email:
            messagebox.showerror("Error", "Invalid email address!")
        elif not mobile_number:
            messagebox.showerror("Error", "Mobile number is required!")
        elif not mobile_number.isdigit() or len(mobile_number) != 10:
            messagebox.showerror("Error", "Mobile number should be 10 digits long and should contain only digits!")
        else:
            cursor.execute("UPDATE New_Account_details SET Name=?, Email=?, Mobile=? WHERE account_number=?", (name, email, mobile_number,account_number))
            conn.commit()
            messagebox.showinfo("Success", "Data modified successfully!")
            self.back_to_menu()

if __name__ == "__main__":
    root = Tk()
    obj = Modify_Account(root)
    root.mainloop()






























































































































# import sqlite3
# from tkinter import *
# from tkinter import messagebox
# import re

# conn = sqlite3.connect('New_Account.db')
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS New_Account_details (account_number, Addhar_No, Name, Email, Mobile, Salary, Deposit, Gender)")

# class Modify_Account:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Modify_Account")
#         self.root.geometry("500x400")
#         self.root.config(bg="#04D8B2")
#         Label(self.root, text="Modify Account", font=("times new roman",23,"bold"),bg="#04D8B2",fg="black",anchor="w",padx=10).place(x=170,y=60,relwidth=1)

#         self.account_number_label = Label(root, text="Account No.:",font=("times new roman",12,"bold"),bg="#04D8B2")
#         self.account_number_label.place(x=160,y=130)
#         self.account_number_entry = Entry(root)
#         self.account_number_entry.place(x=290,y=130)
#         self.account_number_entry.bind("<KeyRelease>", self.validate_data)

#         self.name_label = Label(root, text="Name:",font=("times new roman",12,"bold"),bg="#04D8B2")
#         self.name_label.place(x=160,y=170)
#         self.name_entry = Entry(root)
#         self.name_entry.place(x=290,y=170)
#         self.name_entry.bind("<KeyRelease>", self.validate_data)

#         self.email_label = Label(root, text="Email:",font=("times new roman",12,"bold"),bg="#04D8B2")
#         self.email_label.place(x=160,y=210)
#         self.email_entry = Entry(root)
#         self.email_entry.place(x=290,y=210)
#         self.email_entry.bind("<KeyRelease>", self.validate_data)

#         self.mobile_number_label = Label(root, text="Mobile Number:",font=("times new roman",12,"bold"),bg="#04D8B2")
#         self.mobile_number_label.place(x=160,y=250)
#         self.mobile_number_entry = Entry(root)
#         self.mobile_number_entry.place(x=290,y=250)
#         self.mobile_number_entry.bind("<KeyRelease>", self.validate_data)

#         self.button_modify = Button(root, text="Modify Data",font=("times new roman",10,"bold"), command=self.modify_data, cursor="hand2")
#         self.button_modify.place(x=220,y=300)

#         back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",font=("times new roman", 10, "bold"))
#         back_to_menu_button.place(x=320,y=300)

#         self.account_number_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.account_number_error_label.place(x=160, y=150)

#         self.name_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.name_error_label.place(x=160, y=190)

#         self.email_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.email_error_label.place(x=160, y=230)

#         self.mobile_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.mobile_error_label.place(x=160, y=270)

#     def back_to_menu(self):
#         self.root.destroy()
#         import Main_menu 
#         root = Tk()
#         email = ""
#         Main_menu.Main_Menu(root, email)
#         root.mainloop()

#     def validate_data(self, event=None):
#         name = self.name_entry.get()
#         email = self.email_entry.get()
#         mobile_number = self.mobile_number_entry.get()
#         account_number = self.account_number_entry.get()

#         if not account_number:
#             self.account_number_error_label.config(text="Account number does not exist!")
#         else:
#             self.account_number_error_label.config(text="")
#         if not name:
#             self.name_error_label.config(text="Name is required!")
#         elif not name.replace(' ','').isalpha():
#             self.name_error_label.config(text="Name should contain only alphabets and spaces!")
#         else:
#             self.name_error_label.config(text="")
#         if not email:
#             self.email_error_label.config(text="Email is required!")
#         elif not re.match(r'^[\w\d]{4,}@[\w]{3,10}\.(com|co\.in|org)$', email):
#             self.email_error_label.config(text="Please enter a valid email address")
#         else:
#             self.email_error_label.config(text="")
#         if not mobile_number:
#             self.mobile_error_label.config(text="Mobile number is required!")
#         elif not mobile_number.isdigit() or len(mobile_number) != 10 or not mobile_number.startswith(('7', '8', '9')):
#             self.mobile_error_label.config(text="Mobile number should be 10 digits long, should contain only digits, and should start with 7, 8, or 9!")
#         else:
#             self.mobile_error_label.config(text="")

#     def modify_data(self):
#         account_number = self.account_number_entry.get()

#         if not account_number:
#             self.account_number_error_label.config(text="Account number is required!")
#             return

#         cursor.execute("SELECT * FROM New_Account_details WHERE account_number=?", (account_number,))
#         account = cursor.fetchone()

#         if not account:
#             self.account_number_error_label.config(text="Account number does not exist!")
#             return

#         name = self.name_entry.get()
#         email = self.email_entry.get()
#         mobile_number = self.mobile_number_entry.get()

#         if not name:
#             self.name_error_label.config(text="Name is required!")
#             return
#         elif not name.replace(' ', '').isalpha():
#             self.name_error_label.config(text="Name should contain only alphabets and spaces!")
#             return

#         if not email:
#             self.email_error_label.config(text="Email is required!")
#             return
#         elif not re.match(r'^[\w\d]{4,}@[\w]{3,10}\.(com|co\.in|org)$', email):
#             self.email_error_label.config(text="Please enter a valid email address")
#             return

#         if not mobile_number:
#             self.mobile_error_label.config(text="Mobile number is required!")
#             return
#         elif not mobile_number.isdigit() or len(mobile_number) != 10 or not mobile_number.startswith(('7', '8', '9')):
#             self.mobile_error_label.config(text="Mobile number should be 10 digits long, should contain only digits, and should start with 7, 8, or 9!")
#             return

#         cursor.execute("UPDATE New_Account_details SET Name=?, Email=?, Mobile=? WHERE account_number=?", (name, email, mobile_number, account_number))
#         conn.commit()
#         messagebox.showinfo("Success", "Data modified successfully!")
#         self.back_to_menu()


# if __name__ == "__main__":
#     root = Tk()
#     obj = Modify_Account(root)
#     root.mainloop()
