import random
import re
import sqlite3
from tkinter import *
from tkinter import messagebox
from datetime import date, datetime

conn = sqlite3.Connection('New_Account.db')
cursor = conn.cursor()
cursor.execute("create table if not exists New_Account_details(account_number, Addhar_No unique, Name, Email, Mobile unique, Salary,Deposit, Gender, date text, time text)")

class CreateNewAccount:       
    def __init__(self, root):
        self.root = root
        self.root.title("Create New PPF Account")
        self.root.geometry("800x700")
        self.root.config(bg="#04D8B2")
        Label(self.root, text="Create New PPF Account", font=("times new roman", 20, "bold"),bg="#04D8B2", fg="black",anchor="w", padx=10).place(x=200, y=50, relwidth=1)
        
        self.adno = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.mobile = StringVar()
        self.salary = StringVar()
        self.deposit = StringVar()
        self.gender = StringVar()

        adno_label = Label(root, text="Aadhar No.:",font=("times new roman", 13, "bold"),bg="#04D8B2")
        adno_label.place(x=200,y=150)
        self.adno_entry = Entry(root, textvariable=self.adno)
        self.adno_entry.place(x=350,y=150)

        name_label = Label(root, text="Name:",font=("times new roman", 13, "bold"),bg="#04D8B2")
        name_label.place(x=200,y=200)
        self.name_entry = Entry(root, textvariable=self.name)
        self.name_entry.place(x=350,y=200)
        
        gender_label = Label(root, text="Gender",font=("times new roman", 13, "bold"),bg="#04D8B2")
        gender_label.place(x=200,y=250)

        male_rb = Radiobutton(root, text="Male", variable=self.gender, value="male",font=("times new roman", 13, "bold"),bg="#04D8B2",activebackground="#04D8B2")
        male_rb.place(x=350,y=250)

        female_rb = Radiobutton(root, text="Female", variable=self.gender, value="female",font=("times new roman", 13, "bold"),bg="#04D8B2",activebackground="#04D8B2")
        female_rb.place(x=420,y=250)

        other_rb = Radiobutton(root, text="Others", variable=self.gender, value="other",font=("times new roman", 13, "bold"),bg="#04D8B2",activebackground="#04D8B2")
        other_rb.place(x=500,y=250)
        male_rb.select()

        email_label = Label(root, text="Email:",font=("times new roman", 10, "bold"),bg="#04D8B2")
        email_label.place(x=200,y=300)
        self.email_entry = Entry(root)
        self.email_entry.place(x=350,y=300)

        mobile_label = Label(root, text="Mobile No.:",font=("times new roman", 10, "bold"),bg="#04D8B2")
        mobile_label.place(x=200,y=350)
        self.mobile_entry = Entry(root, textvariable=self.mobile)
        self.mobile_entry.place(x=350,y=350)

        salary_label = Label(root, text="Salary:",font=("times new roman", 10, "bold"),bg="#04D8B2")
        salary_label.place(x=200,y=400)
        self.salary_entry = Entry(root, textvariable=self.salary)
        self.salary_entry.place(x=350,y=400)

        deposit_label = Label(root, text="Deposit:",font=("times new roman", 13, "bold"),bg="#04D8B2")
        deposit_label.place(x=200,y=450)
        self.deposit_entry = Entry(root, textvariable=self.deposit)
        self.deposit_entry.place(x=350,y=450)

        self.error_label = Label(root,bg="#04D8B2")
        self.error_label.place()

        self.account_created_label = Label(root,bg="#04D8B2")
        self.account_created_label.place()

        create_account_button = Button(root, text="Create Account", command=self.create_account, font=("times new roman", 10, "bold"), cursor="hand2")
        create_account_button.place(x=290,y=550)

        back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",font=("times new roman", 10, "bold"))
        back_to_menu_button.place(x=400,y=550)

    def back_to_menu(self):
        email = self.email_entry.get()
        self.root.destroy()
        import Main_menu 
        root = Tk()
        Main_menu.Main_Menu(root,email)
        root.mainloop()
        
    def create_account(self):
        adno = self.adno_entry.get()
        name = self.name_entry.get()
        gender = self.gender.get()
        email = self.email_entry.get()
        mobile = self.mobile_entry.get()
        salary = self.salary_entry.get()
        deposit = self.deposit_entry.get()
        deposit_date = str(date.today())
        deposit_time = datetime.now().strftime("%H:%M:%S")

        cursor.execute("SELECT * FROM New_Account_details WHERE Addhar_No=?", (adno,))
        existing_account = cursor.fetchone()
        if existing_account:
            messagebox.showerror("Error", "Aadhar number already exists!")
            return
        
        cursor.execute("SELECT * FROM New_Account_details WHERE Mobile=?", (mobile,))
        existing_account = cursor.fetchone()
        if existing_account:
            messagebox.showerror("Error", "Mobile number already exists!")
            return

        account_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])

        conn_users = sqlite3.connect("users.db")
        c = conn_users.cursor()
        c.execute("SELECT email FROM users")
        all_emails = c.fetchall()
        email_list = [email[0] for email in all_emails]
        if email not in email_list:
            messagebox.showerror("Error", "Email does not match with the login email!")
            return

        if not adno:
            messagebox.showerror("Error", "Aadhar number is required!")
        elif not adno.isdigit() or len(adno) != 12:
            messagebox.showerror("Error", "Aadhar number should be a 12 digit number!")
        elif adno.startswith(('0', '1')):
            messagebox.showerror("Error", "Aadhar number should not start with 0 or 1!")
        elif any(adno[i] == adno[i+1] for i in range(len(adno)-1)):
            messagebox.showerror("Error", "Aadhar number should not have consecutive repeated digits!")

        elif not name:
            messagebox.showerror("Error", "Name is required!")
        elif len(name.strip()) < 4 or len(name.strip()) > 20:
            messagebox.showerror("Error", "Name should contain 4 to 20 characters")
            return
        elif not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Name should only contain alphabetic characters.")
            return    
           
        elif not gender:
            messagebox.showerror("Error", "Gender is required!")

        elif not mobile:
            messagebox.showerror("Error", "Mobile number is required!")
        elif not mobile.isdigit() or len(mobile) != 10 or not mobile.startswith(('7', '8', '9')):
            messagebox.showerror("Error", "Mobile number should be 10 digits long, should contain only digits, and should start with 7, 8, or 9!")

        elif not salary:
            messagebox.showerror("Error", "Salary is required!")
        elif not salary.isdigit():
            messagebox.showerror("Error", "Salary should be a numeric value!")
        elif len(salary) < 4:
            messagebox.showerror("Error", "Salary should have a minimum of four digits!")

        elif not deposit:
            messagebox.showerror("Error", "Deposit is required!")
        elif not deposit.isdigit() or len(deposit) < 2:
            messagebox.showerror("Error", "Deposit should be a numeric value with a minimum of 2 digits!")
        else:
            cursor.execute("INSERT INTO New_Account_details(account_number, Addhar_No, Name, Email, Mobile, Salary, Deposit, Gender, date, time) VALUES (?,?,?,?,?,?,?,?,?,?)", (account_number, adno, name, email, mobile, salary, deposit, gender, deposit_date, deposit_time))
            conn.commit()

            conn_deposit = sqlite3.connect('deposit.db')
            cursor_deposit = conn_deposit.cursor()
            cursor_deposit.execute("INSERT into deposit(Account_Number, Amount, date, time) VALUES (?,?,?,?)", (account_number, deposit,deposit_date,deposit_time))
            conn_deposit.commit()

            messagebox.showinfo("Success", "Account created successfully. Your account number is {}".format(account_number))
            self.back_to_menu()

if __name__ == "__main__":
    root = Tk()
    email = Entry(root)
    obj = CreateNewAccount(root)
    root.mainloop()




































































































































# import random
# import re
# import sqlite3
# from tkinter import *
# from tkinter import messagebox
# from datetime import date, datetime

# conn = sqlite3.Connection('New_Account.db')
# cursor = conn.cursor()
# cursor.execute("create table if not exists New_Account_details(account_number, Addhar_No unique, Name, Email, Mobile unique, Salary,Deposit, Gender, date text, time text)")

# class CreateNewAccount:       
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Create New PPF Account")
#         self.root.geometry("800x700")
#         self.root.config(bg="#04D8B2")
#         Label(self.root, text="Create New PPF Account", font=("times new roman", 20, "bold"),bg="#04D8B2", fg="black",anchor="w", padx=10).place(x=200, y=50, relwidth=1)
        
#         self.adno = StringVar()
#         self.name = StringVar()
#         self.email = StringVar()
#         self.mobile = StringVar()
#         self.salary = StringVar()
#         self.deposit = StringVar()
#         self.gender = StringVar()

#         adno_label = Label(root, text="Aadhar No.:",font=("times new roman", 13, "bold"),bg="#04D8B2")
#         adno_label.place(x=200,y=150)
#         self.adno_entry = Entry(root, textvariable=self.adno)
#         self.adno_entry.place(x=350,y=150)
#         self.adno_entry.bind("<KeyRelease>", self.validate_adno)

#         name_label = Label(root, text="Name:",font=("times new roman", 13, "bold"),bg="#04D8B2")
#         name_label.place(x=200,y=200)
#         self.name_entry = Entry(root, textvariable=self.name)
#         self.name_entry.place(x=350,y=200)
#         self.name_entry.bind("<KeyRelease>", self.validate_name)
        
#         gender_label = Label(root, text="Gender",font=("times new roman", 13, "bold"),bg="#04D8B2")
#         gender_label.place(x=200,y=250)

#         male_rb = Radiobutton(root, text="Male", variable=self.gender, value="male",font=("times new roman", 13, "bold"),bg="#04D8B2",activebackground="#04D8B2")
#         male_rb.place(x=350,y=250)

#         female_rb = Radiobutton(root, text="Female", variable=self.gender, value="female",font=("times new roman", 13, "bold"),bg="#04D8B2",activebackground="#04D8B2")
#         female_rb.place(x=420,y=250)

#         other_rb = Radiobutton(root, text="Others", variable=self.gender, value="other",font=("times new roman", 13, "bold"),bg="#04D8B2",activebackground="#04D8B2")
#         other_rb.place(x=500,y=250)
#         male_rb.select()

#         email_label = Label(root, text="Email:",font=("times new roman", 10, "bold"),bg="#04D8B2")
#         email_label.place(x=200,y=300)
#         self.email_entry = Entry(root)
#         self.email_entry.place(x=350,y=300)
#         self.email_entry.bind("<KeyRelease>", self.validate_email)

#         mobile_label = Label(root, text="Mobile No.:",font=("times new roman", 10, "bold"),bg="#04D8B2")
#         mobile_label.place(x=200,y=350)
#         self.mobile_entry = Entry(root, textvariable=self.mobile)
#         self.mobile_entry.place(x=350,y=350)
#         self.mobile_entry.bind("<KeyRelease>", self.validate_mobile)

#         salary_label = Label(root, text="Salary:",font=("times new roman", 10, "bold"),bg="#04D8B2")
#         salary_label.place(x=200,y=400)
#         self.salary_entry = Entry(root, textvariable=self.salary)
#         self.salary_entry.place(x=350,y=400)
#         self.salary_entry.bind("<KeyRelease>", self.validate_salary)

#         deposit_label = Label(root, text="Deposit:",font=("times new roman", 13, "bold"),bg="#04D8B2")
#         deposit_label.place(x=200,y=450)
#         self.deposit_entry = Entry(root, textvariable=self.deposit)
#         self.deposit_entry.place(x=350,y=450)

#         self.error_label = Label(root,bg="#04D8B2")
#         self.error_label.place()

#         self.account_created_label = Label(root,bg="#04D8B2")
#         self.account_created_label.place()

#         create_account_button = Button(root, text="Create Account", command=self.create_account, font=("times new roman", 10, "bold"), cursor="hand2")
#         create_account_button.place(x=290,y=550)

#         back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",font=("times new roman", 10, "bold"))
#         back_to_menu_button.place(x=400,y=550)

#         self.adno_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.adno_error_label.place(x=200, y=180)

#         self.name_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.name_error_label.place(x=200, y=230)

#         self.mobile_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.mobile_error_label.place(x=200, y=380)

#         self.email_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.email_error_label.place(x=200, y=330)

#         self.salary_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.salary_error_label.place(x=200, y=430)

#     def back_to_menu(self):
#         email = self.email_entry.get()
#         self.root.destroy()
#         import Main_menu 
#         root = Tk()
#         Main_menu.Main_Menu(root,email)
#         root.mainloop()

#     def validate_adno(self,event):
#         adno = self.adno_entry.get()
        
#         if not adno:
#             self.adno_error_label.config(text="Aadhar number is required!")
#         elif not adno.isdigit() or len(adno) != 12:
#             self.adno_error_label.config(text="Aadhar number should be a 12 digit number!")
#         elif adno.startswith(('0', '1')):
#             self.adno_error_label.config(text="Aadhar number should not start with 0 or 1!")
#         elif any(adno[i] == adno[i+1] for i in range(len(adno)-1)):
#             self.adno_error_label.config(text="Aadhar number should not have consecutive repeated digits!")
#         else:
#             self.adno_error_label.config(text="")

#     def validate_name(self, event):
#         name = self.name_entry.get()

#         if len(name.strip()) < 4 or len(name.strip()) > 20:
#             self.name_error_label.config(text="Name should contain 4 to 20 characters")
#         elif not name.replace(" ", "").isalpha():
#             self.name_error_label.config(text="Name should only contain alphabetic characters.")
#         else:
#             self.name_error_label.config(text="")

#     def validate_mobile(self,event):
#         mobile = self.mobile_entry.get()

#         if not mobile:
#             self.mobile_error_label.config(text="Mobile number is required!")
#         elif not mobile.isdigit() or len(mobile) != 10 or not mobile.startswith(('7', '8', '9')):
#             self.mobile_error_label.config(text="Mobile number should be 10 digits long, should contain only digits, and should start with 7, 8, or 9!")
#         else:
#             self.mobile_error_label.config(text="")

#     def validate_email(self,event):
#         email = self.email_entry.get()

#         conn_users = sqlite3.connect("users.db")
#         c = conn_users.cursor()
#         c.execute("SELECT email FROM users")
#         all_emails = c.fetchall()
#         email_list = [email[0] for email in all_emails]
#         if email not in email_list:
#             self.email_error_label.config(text="Email does not match with the login email!")
#             return
#         else:
#             self.email_error_label.config(text="")

#     def validate_salary(self,event):
#         salary = self.salary_entry.get()

#         if not salary:
#             self.salary_error_label.config(text="Salary is required!")
#         elif not salary.isdigit():
#             self.salary_error_label.config(text="Salary should be a numeric value!")
#         elif len(salary) < 4:
#            self.salary_error_label.config(text="Salary should have a minimum of four digits!")
#         else:
#             self.salary_error_label.config(text="")

#     def create_account(self):
#         adno = self.adno_entry.get()
#         name = self.name_entry.get()
#         gender = self.gender.get()
#         email = self.email_entry.get()
#         mobile = self.mobile_entry.get()
#         salary = self.salary_entry.get()
#         deposit = self.deposit_entry.get()
#         deposit_date = str(date.today())
#         deposit_time = datetime.now().strftime("%H:%M:%S")

#         cursor.execute("SELECT * FROM New_Account_details WHERE Addhar_No=?", (adno,))
#         existing_account = cursor.fetchone()
#         if existing_account:
#             messagebox.showerror("Error", "Aadhar number already exists!")
#             return
        
#         cursor.execute("SELECT * FROM New_Account_details WHERE Mobile=?", (mobile,))
#         existing_account = cursor.fetchone()
#         if existing_account:
#             messagebox.showerror("Error", "Mobile number already exists!")
#             return

#         account_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])

#         # conn_users = sqlite3.connect("users.db")
#         # c = conn_users.cursor()
#         # c.execute("SELECT email FROM users")
#         # all_emails = c.fetchall()
#         # email_list = [email[0] for email in all_emails]
#         # if email not in email_list:
#         #     messagebox.showerror("Error", "Email does not match with the login email!")
#         #     return

#         # if not adno:
#         #     messagebox.showerror("Error", "Aadhar number is required!")
#         # elif not adno.isdigit() or len(adno) != 12:
#         #     messagebox.showerror("Error", "Aadhar number should be a 12 digit number!")
#         # elif adno.startswith(('0', '1')):
#         #     messagebox.showerror("Error", "Aadhar number should not start with 0 or 1!")
#         # elif any(adno[i] == adno[i+1] for i in range(len(adno)-1)):
#         #     messagebox.showerror("Error", "Aadhar number should not have consecutive repeated digits!")

#         # elif not name:
#         #     messagebox.showerror("Error", "Name is required!")
#         # elif len(name.strip()) < 4 or len(name.strip()) > 20:
#         #     messagebox.showerror("Error", "Name should contain 4 to 20 characters")
#         #     return
#         # elif not name.replace(" ", "").isalpha():
#         #     messagebox.showerror("Error", "Name should only contain alphabetic characters.")
#         #     return    
           
#         if not gender:
#             messagebox.showerror("Error", "Gender is required!")

#         # elif not mobile:
#         #     messagebox.showerror("Error", "Mobile number is required!")
#         # elif not mobile.isdigit() or len(mobile) != 10 or not mobile.startswith(('7', '8', '9')):
#         #     messagebox.showerror("Error", "Mobile number should be 10 digits long, should contain only digits, and should start with 7, 8, or 9!")

#         # elif not salary:
#         #     messagebox.showerror("Error", "Salary is required!")
#         # elif not salary.isdigit():
#         #     messagebox.showerror("Error", "Salary should be a numeric value!")
#         # elif len(salary) < 4:
#         #     messagebox.showerror("Error", "Salary should have a minimum of four digits!")

#         elif not deposit:
#             messagebox.showerror("Error", "Deposit is required!")
#         elif not deposit.isdigit() or len(deposit) < 2:
#             messagebox.showerror("Error", "Deposit should be a numeric value with a minimum of 2 digits!")
#         else:
#             cursor.execute("INSERT INTO New_Account_details(account_number, Addhar_No, Name, Email, Mobile, Salary, Deposit, Gender, date, time) VALUES (?,?,?,?,?,?,?,?,?,?)", (account_number, adno, name, email, mobile, salary, deposit, gender, deposit_date, deposit_time))
#             conn.commit()

#             conn_deposit = sqlite3.connect('deposit.db')
#             cursor_deposit = conn_deposit.cursor()
#             cursor_deposit.execute("INSERT into deposit(Account_Number, Amount, date, time) VALUES (?,?,?,?)", (account_number, deposit,deposit_date,deposit_time))
#             conn_deposit.commit()

#             messagebox.showinfo("Success", "Account created successfully. Your account number is {}".format(account_number))
#             self.back_to_menu()

# if __name__ == "__main__":
#     root = Tk()
#     email = Entry(root)
#     obj = CreateNewAccount(root)
#     root.mainloop()
