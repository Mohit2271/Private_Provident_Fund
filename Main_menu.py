from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import Menu

conn = sqlite3.Connection('New_Account.db')
conn2 = sqlite3.Connection('users.db')
cursor = conn.cursor()
cursor2 =conn2.cursor()

def open_main_menu():
    root = Tk()
    obj = Menu.Menu(root)  # Instantiate the Menu class from the imported module
    obj.create_widgets(root)  # Pass the root parameter to create_widgets
    root.mainloop()

class Main_Menu:
    def __init__(self, root, email):
        self.root = root
        self.root.title("Provident Fund Generating System")
        self.root.geometry("1550x1000+0+0")
        self.email = email
        
        self.image_label = Label(root)
        self.image_label.place(width=1550,height=200)
        self.image = Image.open("images\provident-fund.png")
        self.image = self.image.resize((1550, 200))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

        self.image1_label1 = Label(root)
        self.image1_label1.place(x=250,y=200,width=1300,height=600)
        self.image1 = Image.open("images\ppf2.jpg")
        self.image1 = self.image1.resize((1300,600))
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.image1_label1.config(image=self.photo1)

        self.new_account_button = Button(root, text="Create New PPF Account", command=self.new_account, cursor="hand2", bg="black", fg="white", height=3, width=34)
        self.new_account_button.place(y=200)

        self.deposited_amount_button = Button(root, text="Deposit Amount", command=self.deposited_amount, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.deposited_amount_button.place(y=250)

        self.withdrawal_button = Button(root, text="Withdrawal", command=self.withdrawal, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.withdrawal_button.place(y=300)

        self.check_ppf_button = Button(root, text="PPF Loan Check", command=self.check_ppf, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.check_ppf_button.place(y=350)

        self.calculate_button = Button(root, text="Calculate", command=self.calculate, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.calculate_button.place(y=400)

        self.ppf_loan_button = Button(root, text="PPF Loan", command=self.ppf_loan, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.ppf_loan_button.place(y=450)

        self.nomination_button = Button(root, text="Nomination Form", command=self.Nomination, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.nomination_button.place(y=500)

        self.Show_account_button = Button(root, text="Show Account", command=self.show_account, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.Show_account_button.place(y=550)

        self.modify_account_button = Button(root, text="Modify", command=self.modify_account, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.modify_account_button.place(y=600)

        self.show_transaction_button = Button(root, text="Show Transaction", command=self.show_transaction, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.show_transaction_button.place(y=650)

        self.logout_button = Button(root, text="Logout", command=self.back_to_menu, cursor="hand2",bg="black",fg="white",height=3,width=34)
        self.logout_button.place(y=700)

    # def logout(self):
    #     self.root.destroy()
    #     import Menu
    #     root = Tk()
    #     Menu.Menu(root)
    #     root.mainloop()

    def back_to_menu(self):
        self.root.destroy()
        open_main_menu()

    def show_transaction(self):
        self.root.destroy()
        import Show_transaction
        root = Tk()
        Show_transaction.ShowTransactions(root)
        root.mainloop()

    def modify_account(self):
        self.root.destroy()
        import Modify_Account
        root = Tk()
        Modify_Account.Modify_Account(root)
        root.mainloop()

    def show_account(self):
        self.root.destroy()
        import Show_Account
        root = Tk()
        Show_Account.ShowAccountDetails(root)
        root.mainloop()

    def user_has_account(self):
        email = self.email
        cursor.execute("SELECT Email FROM New_Account_details  WHERE Email=?", (str(email),))
        user = cursor.fetchone()

        if user is None:
            return False
        else:
            return True

    def new_account(self):
        if self.user_has_account():
            messagebox.showinfo("Account Exists", "You already have an account.")
        else:
            self.root.destroy()
            import Create_New_Account
            root = Tk()
            Create_New_Account.CreateNewAccount(root)
            root.mainloop()

    def deposited_amount(self):
        self.root.destroy() 
        import Deposit
        root = Tk()
        Deposit.Deposit(root)
        root.mainloop()

    def withdrawal(self):
        self.root.destroy()
        import Withdrawal
        root = Tk()
        Withdrawal.ProvidentFundWithdrawal(root)
        root.mainloop()

    def check_ppf(self):
        self.root.destroy()
        import PPF_Check
        root = Tk()
        PPF_Check.PPF_Check(root)
        root.mainloop()

    def ppf_loan(self):
        self.root.destroy()
        import PPF_Loan
        root = Tk()
        PPF_Loan.PPF_Loan(root)
        root.mainloop()

    def Nomination(self):
        self.root.destroy()
        import Nomination
        root = Tk()
        Nomination.Nomination(root)
        root.mainloop()

    def calculate(self):
        self.root.destroy()
        import Calculator
        root = Tk()
        Calculator.ProvidentFundCalculator(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    email_entry = Entry(root)
    obj = Main_Menu(root, email_entry)
    root.mainloop()





