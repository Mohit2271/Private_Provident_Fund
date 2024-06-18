import sqlite3
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date, datetime

conn = sqlite3.connect('deposit.db')
cursor = conn.cursor()
cursor.execute("create table if not exists deposit(account_number text, Amount integer, date text, time text)")

class Deposit:
    def __init__(self,root):
        self.root = root
        self.root.title("Deposit")
        self.root.geometry("900x600")
        self.root.config(bg="#04D8B2") 
        Label(self.root, text="Add Amount to PPF", font=("times new roman",20,"bold"),bg="#04D8B2",fg="black",anchor="w",padx=10).place(x=560,y=50,relwidth=1)

        self.account_no = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.mobile = StringVar()
        self.amount_deposited = StringVar()

        self.image_label = Label(root)
        self.image_label.place(x=50, y=130,width=400,height=330)
        self.image = Image.open("images\deposit.jpg")
        self.image = self.image.resize((400, 400))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

        account_no_label = Label(root, text="Account number:",font=("times new roman",10,"bold"),bg="#04D8B2")
        account_no_label.place(x=500,y=150)
        self.account_no_entry = Entry(root, textvariable=self.account_no)
        self.account_no_entry.place(x=730,y=150)

        name_label = Label(root, text="Name:",font=("times new roman",10,"bold"),bg="#04D8B2")
        name_label.place(x=500,y=190)
        self.name_entry = Entry(root, textvariable=self.name, state="readonly")
        self.name_entry.place(x=730,y=190)

        email_label = Label(root, text="Email:",font=("times new roman",10,"bold"),bg="#04D8B2")
        email_label.place(x=500,y=230)
        self.email_entry = Entry(root, textvariable=self.email, state="readonly")
        self.email_entry.place(x=730,y=230)

        mobile_label = Label(root, text="Mobile:",font=("times new roman",10,"bold"),bg="#04D8B2")
        mobile_label.place(x=500,y=270)
        self.mobile_entry = Entry(root, textvariable=self.mobile, state="readonly")
        self.mobile_entry.place(x=730,y=270)

        search_button = Button(root, text="Search", command=self.show_details,font=("times new roman",10,"bold"), cursor="hand2")
        search_button.place(x=650,y=310)

        amount_deposited_label = Label(root, text="Amount to be Deposited:",font=("times new roman",10,"bold"),bg="#04D8B2")
        amount_deposited_label.place(x=500,y=350)
        self.amount_deposited_entry = Entry(root, textvariable=self.amount_deposited)
        self.amount_deposited_entry.place(x=730,y=350)

        submit_button = Button(root, text="Submit", command=self.deposit_amount,font=("times new roman",10,"bold"), cursor="hand2")
        submit_button.place(x=650,y=400)

        back_button = Button(root, text="Back to Menu", command=self.back_to_menu,font=("times new roman",10,"bold"), cursor="hand2")
        back_button.place(x=750,y=400)

    def back_to_menu(self):
        self.root.destroy()
        import Main_menu 
        root = Tk()
        email = ""
        Main_menu.Main_Menu(root, email)
        root.mainloop()

    def show_details(self):
        account_number = self.account_no_entry.get()

        conn = sqlite3.connect('New_Account.db')
        cursor = conn.cursor()
        cursor.execute('Select * from New_Account_details where account_number=?', (account_number,))
        account = cursor.fetchone()
        if account:
            self.name.set(account[2])
            self.email.set(account[3])
            self.mobile.set(account[4])
        else:
            messagebox.showinfo("Invalid","Account does not exist.")

    def deposit_amount(self):
        account_number = self.account_no_entry.get()
        amount = int(self.amount_deposited_entry.get())
        deposit_date = str(date.today())
        deposit_time = datetime.now().strftime("%H:%M:%S")

        conn = sqlite3.connect('New_Account.db')
        cursor = conn.cursor()
        cursor.execute("SELECT deposit FROM New_Account_details WHERE account_number = ?", (account_number,))
        account = cursor.fetchone()

        if account:
            current_balance = int(account[0])
            new_balance = current_balance + amount
            cursor.execute("UPDATE New_Account_details SET deposit = ? WHERE account_number = ?", (new_balance, account_number))
            conn.commit()
            messagebox.showinfo("Success", "Amount deposited successfully. New balance is {}".format(new_balance))

            conn_deposit = sqlite3.connect('deposit.db')
            cursor_deposit = conn_deposit.cursor()
            cursor_deposit.execute("INSERT INTO deposit(account_number, amount, date, time) VALUES (?, ?, ?, ?)", (account_number, amount, deposit_date, deposit_time))
            conn_deposit.commit()
            self.back_to_menu()
        else:
            messagebox.showerror("Error", "Account not found.")

if __name__ == "__main__":
    root = Tk()
    obj = Deposit(root)
    root.mainloop()























































































































# import sqlite3
# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from datetime import date, datetime

# conn = sqlite3.connect('deposit.db')
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS deposit(account_number TEXT, amount INTEGER, date TEXT, time TEXT)")

# class Deposit:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Deposit")
#         self.root.geometry("900x600")
#         self.root.config(bg="#04D8B2")
#         Label(self.root, text="Add Amount to PPF", font=("times new roman", 20, "bold"), bg="#04D8B2", fg="black",
#               anchor="w", padx=10).place(x=560, y=50, relwidth=1)

#         self.account_no = StringVar()
#         self.name = StringVar()
#         self.email = StringVar()
#         self.mobile = StringVar()
#         self.amount_deposited = StringVar()

#         self.image_label = Label(root)
#         self.image_label.place(x=50, y=130, width=400, height=330)
#         self.image = Image.open("images/deposit.jpg")
#         self.image = self.image.resize((400, 400))
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.image_label.config(image=self.photo)

#         account_no_label = Label(root, text="Account number:", font=("times new roman", 10, "bold"), bg="#04D8B2")
#         account_no_label.place(x=500, y=150)
#         self.account_no_entry = Entry(root, textvariable=self.account_no)
#         self.account_no_entry.place(x=730, y=150)
#         self.account_no_entry.bind("<KeyRelease>", self.show_details)

#         name_label = Label(root, text="Name:", font=("times new roman", 10, "bold"), bg="#04D8B2")
#         name_label.place(x=500, y=190)
#         self.name_entry = Entry(root, textvariable=self.name, state="readonly")
#         self.name_entry.place(x=730, y=190)

#         email_label = Label(root, text="Email:", font=("times new roman", 10, "bold"), bg="#04D8B2")
#         email_label.place(x=500, y=230)
#         self.email_entry = Entry(root, textvariable=self.email, state="readonly")
#         self.email_entry.place(x=730, y=230)

#         mobile_label = Label(root, text="Mobile:", font=("times new roman", 10, "bold"), bg="#04D8B2")
#         mobile_label.place(x=500, y=270)
#         self.mobile_entry = Entry(root, textvariable=self.mobile, state="readonly")
#         self.mobile_entry.place(x=730, y=270)

#         search_button = Button(root, text="Search", command=self.show_details, font=("times new roman", 10, "bold"),
#                                cursor="hand2")
#         search_button.place(x=650, y=310)

#         amount_deposited_label = Label(root, text="Amount to be Deposited:",
#                                        font=("times new roman", 10, "bold"), bg="#04D8B2")
#         amount_deposited_label.place(x=500, y=350)
#         self.amount_deposited_entry = Entry(root, textvariable=self.amount_deposited)
#         self.amount_deposited_entry.place(x=730, y=350)

#         submit_button = Button(root, text="Submit", command=self.deposit_amount, font=("times new roman", 10, "bold"),
#                                cursor="hand2")
#         submit_button.place(x=650, y=400)

#         back_button = Button(root, text="Back to Menu", command=self.back_to_menu, font=("times new roman", 10, "bold"),
#                              cursor="hand2")
#         back_button.place(x=750, y=400)

#         self.account_number_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.account_number_error_label.place(x=500, y=170)

#     def back_to_menu(self):
#         self.root.destroy()
#         import Main_menu
#         root = Tk()
#         email = ""
#         Main_menu.Main_Menu(root, email)
#         root.mainloop()

#     def show_details(self, event=None):
#         account_number = self.account_no_entry.get()

#         conn = sqlite3.connect('New_Account.db')
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM New_Account_details WHERE account_number=?', (account_number,))
#         account = cursor.fetchone()
#         if account:
#             self.name.set(account[2])
#             self.email.set(account[3])
#             self.mobile.set(account[4])
#             self.account_number_error_label.config(text="")
#         else:
#             self.name.set("")
#             self.email.set("")
#             self.mobile.set("")
#             self.account_number_error_label.config(text="Account does not exist")

#     def deposit_amount(self):
#         account_number = self.account_no_entry.get()
#         amount = int(self.amount_deposited_entry.get())
#         deposit_date = str(date.today())
#         deposit_time = datetime.now().strftime("%H:%M:%S")

#         conn = sqlite3.connect('New_Account.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT deposit FROM New_Account_details WHERE account_number = ?", (account_number,))
#         account = cursor.fetchone()

#         if account:
#             current_balance = int(account[0])
#             new_balance = current_balance + amount
#             cursor.execute("UPDATE New_Account_details SET deposit = ? WHERE account_number = ?",
#                            (new_balance, account_number))
#             conn.commit()
#             messagebox.showinfo("Success", "Amount deposited successfully. New balance is {}".format(new_balance))

#             conn_deposit = sqlite3.connect('deposit.db')
#             cursor_deposit = conn_deposit.cursor()
#             cursor_deposit.execute("INSERT INTO deposit(account_number, amount, date, time) VALUES (?, ?, ?, ?)", (account_number, amount, deposit_date, deposit_time))
#             conn_deposit.commit()
#             self.back_to_menu()
#         else:
#             messagebox.showerror("Error", "Account not found.")

# if __name__ == "__main__":
#     root = Tk()
#     obj = Deposit(root)
#     root.mainloop()
