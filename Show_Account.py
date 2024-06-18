from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.Connection('New_Account.db')
cursor = conn.cursor()
cursor.execute("create table if not exists New_Account_details(account_number, Addhar_No, Name, Email, Mobile, Salary, Deposite, Gender)")

class ShowAccountDetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Show Account Details")
        self.root.geometry("600x600")
        self.root.config(bg="#04D8B2")
        
        self.account_number = StringVar()
        self.balance = StringVar()
        self.Addhar_No = StringVar()
        self.Name = StringVar() 
        self.Email = StringVar()
        self.Mobile = StringVar()
        self.Salary = StringVar()
        self.Gender = StringVar()
        self.nominee_name = StringVar()

        self.account_number_label = Label(root, text="Account Number:", font=("times new roman", 11, "bold"),bg="#04D8B2")
        self.account_number_label.place(x=50, y=50)
        self.account_number_entry = Entry(root, textvariable=self.account_number)
        self.account_number_entry.place(x=200, y=50)

        self.show_button = Button(root, text="Show Details", command=self.show_details, font=("times new roman", 10, "bold"),cursor="hand2")
        self.show_button.place(x=150, y=100)

        self.Addhar_No_label = Label(root, text="Addhar No:",font=("times new roman", 11, "bold"),bg="#04D8B2")
        self.Addhar_No_label.place(x=50, y=150)
        self.Addhar_No_entry = Entry(root, textvariable=self.Addhar_No, state='readonly')
        self.Addhar_No_entry.place(x=200, y=150)

        self.Name_label = Label(root, text="Name:", font=("times new roman", 11, "bold"),bg="#04D8B2")
        self.Name_label.place(x=50, y=200)
        self.Name_entry = Entry(root, textvariable=self.Name, state='readonly')
        self.Name_entry.place(x=200, y=200)

        self.Nomination_label = Label(root, text="Nominee:", font=("times new roman", 11, "bold"),bg="#04D8B2")
        self.Nomination_label.place(x=50, y=250)
        self.Nomination_entry = Entry(root, textvariable=self.nominee_name, state='readonly')
        self.Nomination_entry.place(x=200, y=250)


        self.Email_label = Label(root, text="Email:", font=("times new roman", 11, "bold"),bg="#04D8B2")
        self.Email_label.place(x=50, y=300)
        self.Email_entry = Entry(root, textvariable=self.Email, state='readonly')
        self.Email_entry.place(x=200, y=300)

        self.Mobile_label = Label(root, text="Mobile:",font=("times new roman", 11, "bold"),bg="#04D8B2")
        self.Mobile_label.place(x=50, y=350)
        self.Mobile_entry = Entry(root, textvariable=self.Mobile, state='readonly')
        self.Mobile_entry.place(x=200, y=350)

        self.Salary_label = Label(root, text="Salary:", font=("times new roman", 11, "bold"),bg="#04D8B2")
        self.Salary_label.place(x=50, y=400)
        self.Salary_entry = Entry(root, textvariable=self.Salary, state='readonly')
        self.Salary_entry.place(x=200, y=400)

        self.Gender_label = Label(root, text="Gender:", font=("times new roman", 11, "bold"),bg="#04D8B2")
        self.Gender_label.place(x=50, y=450)
        self.Gender_entry = Entry(root, textvariable=self.Gender, state='readonly')
        self.Gender_entry.place(x=200, y=450)

        self.balance_label = Label(root, text="Balance:",font=("times new roman", 11, "bold"),bg="#04D8B2")
        self.balance_label.place(x=50, y=500)
        self.balance_entry = Entry(root, textvariable=self.balance, state='readonly')
        self.balance_entry.place(x=200, y=500)

        self.back_button = Button(root, text="Back to Menu", command=self.back_to_menu, font=("times new roman", 10, "bold"),cursor="hand2")
        self.back_button.place(x=150, y=550)

    def show_details(self):
        account_number = self.account_number_entry.get()
        cursor.execute('Select * from New_Account_details where account_number=?', (account_number,))
        account = cursor.fetchone()
        if account:
            self.Addhar_No.set(account[1])
            self.Name.set(account[2])
            self.Email.set(account[3])
            self.Mobile.set(account[4])
            self.Salary.set(account[5])          
            self.balance.set(account[6])
            self.Gender.set(account[7])

            conn_nominee = sqlite3.Connection('Nomination.db')
            nominee_cursor = conn_nominee.cursor()
            nominee_cursor.execute('SELECT nominee_name FROM Nominee_details WHERE account_no=?', (account_number,))
            nominee_name = nominee_cursor.fetchone()
            if nominee_name:
                self.nominee_name.set(str(nominee_name[0]))
        else:
            messagebox.showinfo("Invalid","Account does not exist.")

    def back_to_menu(self):
        self.root.destroy()
        import Main_menu 
        root = Tk()
        email = ""
        Main_menu.Main_Menu(root, email)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = ShowAccountDetails(root)
    root.mainloop()


















































































































# from tkinter import *
# from tkinter import messagebox
# import sqlite3

# conn = sqlite3.connect('New_Account.db')
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS New_Account_details (account_number, Addhar_No, Name, Email, Mobile, Salary, Deposite, Gender)")

# class ShowAccountDetails:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Show Account Details")
#         self.root.geometry("600x600")
#         self.root.config(bg="#04D8B2")

#         self.account_number = StringVar()
#         self.balance = StringVar()
#         self.Addhar_No = StringVar()
#         self.Name = StringVar() 
#         self.Email = StringVar()
#         self.Mobile = StringVar()
#         self.Salary = StringVar()
#         self.Gender = StringVar()
#         self.nominee_name = StringVar()

#         self.account_number_label = Label(root, text="Account Number:", font=("times new roman", 11, "bold"), bg="#04D8B2")
#         self.account_number_label.place(x=50, y=50)
#         self.account_number_entry = Entry(root, textvariable=self.account_number)
#         self.account_number_entry.place(x=200, y=50)
#         self.account_number_entry.bind("<KeyRelease>", self.show_details)

#         self.show_button = Button(root, text="Show Details", command=self.show_details, font=("times new roman", 10, "bold"), cursor="hand2")
#         self.show_button.place(x=150, y=100)

#         self.Addhar_No_label = Label(root, text="Addhar No:", font=("times new roman", 11, "bold"), bg="#04D8B2")
#         self.Addhar_No_label.place(x=50, y=150)
#         self.Addhar_No_entry = Entry(root, textvariable=self.Addhar_No, state='readonly')
#         self.Addhar_No_entry.place(x=200, y=150)

#         self.Name_label = Label(root, text="Name:", font=("times new roman", 11, "bold"), bg="#04D8B2")
#         self.Name_label.place(x=50, y=200)
#         self.Name_entry = Entry(root, textvariable=self.Name, state='readonly')
#         self.Name_entry.place(x=200, y=200)

#         self.Nomination_label = Label(root, text="Nominee:", font=("times new roman", 11, "bold"), bg="#04D8B2")
#         self.Nomination_label.place(x=50, y=250)
#         self.Nomination_entry = Entry(root, textvariable=self.nominee_name, state='readonly')
#         self.Nomination_entry.place(x=200, y=250)

#         self.Email_label = Label(root, text="Email:", font=("times new roman", 11, "bold"), bg="#04D8B2")
#         self.Email_label.place(x=50, y=300)
#         self.Email_entry = Entry(root, textvariable=self.Email, state='readonly')
#         self.Email_entry.place(x=200, y=300)

#         self.Mobile_label = Label(root, text="Mobile:", font=("times new roman", 11, "bold"), bg="#04D8B2")
#         self.Mobile_label.place(x=50, y=350)
#         self.Mobile_entry = Entry(root, textvariable=self.Mobile, state='readonly')
#         self.Mobile_entry.place(x=200, y=350)

#         self.Salary_label = Label(root, text="Salary:", font=("times new roman", 11, "bold"), bg="#04D8B2")
#         self.Salary_label.place(x=50, y=400)
#         self.Salary_entry = Entry(root, textvariable=self.Salary, state='readonly')
#         self.Salary_entry.place(x=200, y=400)

#         self.Gender_label = Label(root, text="Gender:", font=("times new roman", 11, "bold"), bg="#04D8B2")
#         self.Gender_label.place(x=50, y=450)
#         self.Gender_entry = Entry(root, textvariable=self.Gender, state='readonly')
#         self.Gender_entry.place(x=200, y=450)

#         self.balance_label = Label(root, text="Balance:", font=("times new roman", 11, "bold"), bg="#04D8B2")
#         self.balance_label.place(x=50, y=500)
#         self.balance_entry = Entry(root, textvariable=self.balance, state='readonly')
#         self.balance_entry.place(x=200, y=500)

#         self.back_button = Button(root, text="Back to Menu", command=self.back_to_menu, font=("times new roman", 10, "bold"), cursor="hand2")
#         self.back_button.place(x=150, y=550)

#         self.account_number_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.account_number_error_label.place(x=50, y=70)

#     def show_details(self, event=None):
#         account_number = self.account_number_entry.get()
#         cursor.execute('SELECT * FROM New_Account_details WHERE account_number=?', (account_number,))
#         account = cursor.fetchone()
#         if account:
#             self.Addhar_No.set(account[1])
#             self.Name.set(account[2])
#             self.Email.set(account[3])
#             self.Mobile.set(account[4])
#             self.Salary.set(account[5])
#             self.balance.set(account[6])
#             self.Gender.set(account[7])

#             conn_nominee = sqlite3.connect('Nomination.db')
#             nominee_cursor = conn_nominee.cursor()
#             nominee_cursor.execute('SELECT nominee_name FROM Nominee_details WHERE account_no=?', (account_number,))
#             nominee_name = nominee_cursor.fetchone()
#             if nominee_name:
#                 self.nominee_name.set(str(nominee_name[0]))
#             else:
#                 self.nominee_name.set("")
#             self.account_number_error_label.config(text="")
#         else:
#             self.Addhar_No.set("")
#             self.Name.set("")
#             self.Email.set("")
#             self.Mobile.set("")
#             self.Salary.set("")
#             self.balance.set("")
#             self.Gender.set("")
#             self.nominee_name.set("")
#             self.account_number_error_label.config(text="Account does not exist.")

#     def back_to_menu(self):
#         self.root.destroy()
#         import Main_menu
#         root = Tk()
#         email = ""
#         Main_menu.Main_Menu(root, email)
#         root.mainloop()

# if __name__ == "__main__":
#     root = Tk()
#     obj = ShowAccountDetails(root)
#     root.mainloop()
