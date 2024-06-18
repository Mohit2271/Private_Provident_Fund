import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date, datetime

conn = sqlite3.connect('withdrawal.db')
cursor = conn.cursor()
cursor.execute("create table if not exists withdrawal(account_number text, Amount integer, date text, time text)")

class ProvidentFundWithdrawal:
    def __init__(self, root):
        self.root = root
        root.title("Private Provident Fund Withdrawal")
        self.root.geometry("900x500")
        self.root.config(bg="#04D8B2")
        Label(self.root, text="Withdrawal", font=("times new roman", 23, "bold"),bg="#04D8B2",fg="black",anchor="w", padx=10).place(x=600, y=80, relwidth=1)
        
        self.Account_Number = StringVar()

        self.image_label = Label(root,bg="#04D8B2")
        self.image_label.place(x=5, y=80,width=500,height=360)
        self.image = Image.open("images\withdrawal.jpg")
        self.image = self.image.resize((400, 300))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

        Account_Number_label = Label(root, text="Account_No:",font=("times new roman", 12, "bold"),bg="#04D8B2")
        Account_Number_label.place(x=500,y=140)
        self.Account_Number_entry = Entry(root, textvariable=self.Account_Number)
        self.Account_Number_entry.place(x=700,y=140)

        search_button = Button(root, text="Search", command=self.search_account, font=("times new roman", 10, "bold"),cursor="hand2")
        search_button.place(x=650, y= 180)

        self.Deposit = StringVar()
        Deposit_label = Label(root, text="Available Balance:", font=("times new roman", 12, "bold"),bg="#04D8B2")
        Deposit_label.place(x=500, y=220)
        Deposit_entry = Entry(root, textvariable=self.Deposit, state='readonly')
        Deposit_entry.place(x=700, y=220)

        amount_label = Label(root, text="Withdrawal amount:",font=("times new roman", 12, "bold"),bg="#04D8B2")
        amount_label.place(x=500,y=280)
        self.amount_entry = Entry(root)
        self.amount_entry.place(x=700,y=280)

        withdraw_button = Button(root, text="Withdraw", command=self.withdraw_amount, font=("times new roman", 10, "bold"),cursor="hand2")
        withdraw_button.place(x=650, y=320)

        back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",font=("times new roman", 10, "bold"))
        back_to_menu_button.place(x=750,y=320)

    def back_to_menu(self):
        self.root.destroy()
        import Main_menu 
        root = Tk()
        email = ""
        Main_menu.Main_Menu(root, email)
        root.mainloop()

    def search_account(self):
        account_number = self.Account_Number.get()

        conn = sqlite3.connect('New_Account.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Deposit FROM New_Account_details WHERE account_number = ?", (account_number,))
        account = cursor.fetchone()

        if account:
            self.Deposit.set(account[0])
        else:
            messagebox.showerror("Error", "Account not found.")
        conn.close()

    def withdraw_amount(self):
        account_number = self.Account_Number.get()
        amount = int(self.amount_entry.get())
        deposit_date = str(date.today())
        deposit_time = datetime.now().strftime("%H:%M:%S")

        conn = sqlite3.connect('New_Account.db')
        cursor = conn.cursor()
        cursor.execute("SELECT deposit FROM New_Account_details WHERE account_number = ?", (account_number,))
        account = cursor.fetchone()

        if account:
            current_balance = int(account[0])
            if current_balance >= amount:
                new_balance = current_balance - amount
                cursor.execute("UPDATE New_Account_details SET deposit = ? WHERE account_number = ?",(new_balance, account_number))
                conn.commit()
                messagebox.showinfo("Success", "Amount withdrawn successfully. New balance is {}".format(new_balance))

                conn = sqlite3.connect('withdrawal.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO withdrawal(account_number, Amount, date, time) VALUES (?, ?, ?, ?)",(account_number, amount, deposit_date, deposit_time))
                conn.commit()

                self.back_to_menu()
            else:
                messagebox.showerror("Error", "Insufficient balance in the account.")
        else:
            messagebox.showerror("Error", "Account not found.")

if __name__ == "__main__":
    root = Tk()
    obj = ProvidentFundWithdrawal(root)
    root.mainloop()

























































































































# import sqlite3
# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from datetime import date, datetime

# conn = sqlite3.connect('withdrawal.db')
# cursor = conn.cursor()
# cursor.execute("create table if not exists withdrawal(account_number text, Amount integer, date text, time text)")

# class ProvidentFundWithdrawal:
#     def __init__(self, root):
#         self.root = root
#         root.title("Private Provident Fund Withdrawal")
#         self.root.geometry("900x500")
#         self.root.config(bg="#04D8B2")
#         Label(self.root, text="Withdrawal", font=("times new roman", 23, "bold"),bg="#04D8B2",fg="black",anchor="w", padx=10).place(x=600, y=80, relwidth=1)
        
#         self.Account_Number = StringVar()

#         self.image_label = Label(root,bg="#04D8B2")
#         self.image_label.place(x=5, y=80,width=500,height=360)
#         self.image = Image.open("images/withdrawal.jpg")
#         self.image = self.image.resize((400, 300))
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.image_label.config(image=self.photo)

#         Account_Number_label = Label(root, text="Account_No:",font=("times new roman", 12, "bold"),bg="#04D8B2")
#         Account_Number_label.place(x=500,y=140)
#         self.Account_Number_entry = Entry(root, textvariable=self.Account_Number)
#         self.Account_Number_entry.place(x=700,y=140)
#         self.Account_Number_entry.bind("<KeyRelease>", self.search_account)

#         search_button = Button(root, text="Search", command=self.search_account, font=("times new roman", 10, "bold"),cursor="hand2")
#         search_button.place(x=650, y= 180)

#         self.Deposit = StringVar()
#         Deposit_label = Label(root, text="Available Balance:", font=("times new roman", 12, "bold"),bg="#04D8B2")
#         Deposit_label.place(x=500, y=220)
#         Deposit_entry = Entry(root, textvariable=self.Deposit, state='readonly')
#         Deposit_entry.place(x=700, y=220)

#         amount_label = Label(root, text="Withdrawal amount:",font=("times new roman", 12, "bold"),bg="#04D8B2")
#         amount_label.place(x=500,y=280)
#         self.amount_entry = Entry(root)
#         self.amount_entry.place(x=700,y=280)

#         withdraw_button = Button(root, text="Withdraw", command=self.withdraw_amount, font=("times new roman", 10, "bold"),cursor="hand2")
#         withdraw_button.place(x=650, y=320)

#         back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",font=("times new roman", 10, "bold"))
#         back_to_menu_button.place(x=750,y=320)

#         self.account_number_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.account_number_error_label.place(x=500, y=160)

#     def back_to_menu(self):
#         self.root.destroy()
#         import Main_menu 
#         root = Tk()
#         email = ""
#         Main_menu.Main_Menu(root, email)
#         root.mainloop()

#     def search_account(self, event=None):
#         account_number = self.Account_Number.get()

#         conn = sqlite3.connect('New_Account.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT Deposit FROM New_Account_details WHERE account_number = ?", (account_number,))
#         account = cursor.fetchone()

#         if account:
#             self.Deposit.set(account[0])
#         else:
#             self.account_number_error_label.config(text="Account not found")
#         conn.close()

#     def withdraw_amount(self):
#         account_number = self.Account_Number.get()
#         amount_str = self.amount_entry.get()

#         try:
#             amount = int(amount_str)
#         except ValueError:
#             messagebox.showerror("Error", "Invalid withdrawal amount. Please enter a valid integer.")
#             return

#         conn = sqlite3.connect('New_Account.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT deposit FROM New_Account_details WHERE account_number = ?", (account_number,))
#         account = cursor.fetchone()

#         if account:
#             current_balance = int(account[0])
#             if amount <= 0:
#                 messagebox.showerror("Error", "Invalid withdrawal amount. Amount must be greater than zero.")
#             elif amount > current_balance:
#                 messagebox.showerror("Error", "Insufficient balance in the account.")
#             else:
#                 new_balance = current_balance - amount
#                 cursor.execute("UPDATE New_Account_details SET deposit = ? WHERE account_number = ?",(new_balance, account_number))
#                 conn.commit()
#                 messagebox.showinfo("Success", "Amount withdrawn successfully. New balance is {}".format(new_balance))

#                 deposit_date = str(date.today())
#                 deposit_time = datetime.now().strftime("%H:%M:%S")
#                 conn = sqlite3.connect('withdrawal.db')
#                 cursor = conn.cursor()
#                 cursor.execute("INSERT INTO withdrawal(account_number, Amount, date, time) VALUES (?, ?, ?, ?)",(account_number, amount, deposit_date, deposit_time))
#                 conn.commit()

#                 self.back_to_menu()
#         else:
#             messagebox.showerror("Error", "Account not found.")

# if __name__ == "__main__":
#     root = Tk()
#     obj = ProvidentFundWithdrawal(root)
#     root.mainloop()
