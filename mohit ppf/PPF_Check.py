from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

conn = sqlite3.Connection('loan.db')
cursor = conn.cursor()
cursor.execute("create table if not exists Loan_details(Account_no text unique, Amount_loan text, Interset text, PPF_Passbook)")

class PPF_Check:
    def __init__(self,root):
        self.root = root
        self.root.title("PPF Loan Check")
        self.root.geometry("1100x600")
        self.root.config(bg="#04D8B2")
        Label(self.root, text="PPF Loan Check", font=("times new roman",23,"bold"),bg="#04D8B2",fg="black",anchor="w",padx=10).place(x=750,y=100,relwidth=1)

        self.Account_no = StringVar()
        self.amount_loan = StringVar()
        self.tenure = StringVar()
        
        self.image_label = Label(root,bg="#04D8B2")
        self.image_label.place(x=50, y=120,width=550,height=300)
        self.image = Image.open("images\loan_check.jpg")
        self.image = self.image.resize((500, 300))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

        Account_no_label = Label(root, text="Account No.",font=("times new roman",12,"bold"),bg="#04D8B2")
        Account_no_label.place(x=650,y=200)
        self.Account_no_entry = Entry(root, textvariable=self.Account_no)
        self.Account_no_entry.place(x=850,y=200)

        amount_loan_label = Label(root, text="Loan Amount",font=("times new roman",12,"bold"),bg="#04D8B2")
        amount_loan_label.place(x=650,y=240)
        self.amount_loan_entry = Entry(root, textvariable=self.amount_loan, state='readonly')
        self.amount_loan_entry.place(x=850,y=240)

        tenure_label = Label(root, text="Tenure (In year)",font=("times new roman",12,"bold"),bg="#04D8B2")
        tenure_label.place(x=650,y=280)
        self.tenure_entry = Entry(root, textvariable=self.tenure,state='readonly')
        self.tenure_entry.place(x=850,y=280)

        check_button = Button(root, text="Check", command=self.show_details,font=("times new roman",10,"bold"))
        check_button.place(x=750,y=340)

        back_button = Button(root, text="Back to Menu", command=self.back_to_menu,font=("times new roman",10,"bold"))
        back_button.place(x=850,y=340)

    def back_to_menu(self):
        self.root.destroy()
        import Main_menu 
        root = Tk()
        email = ""
        Main_menu.Main_Menu(root, email)
        root.mainloop()

    def show_details(self):
        Account_no = self.Account_no_entry.get()
        cursor.execute('Select * from Loan_details where Account_no=?', (Account_no,))
        account = cursor.fetchone()
        if account:
            self.amount_loan.set(account[1])
            self.tenure.set(account[2])
        else:
            messagebox.showinfo("Invalid","Loan does not exist.")
        
if __name__ == "__main__":
    root = Tk()
    obj=PPF_Check(root)
    root.mainloop()
























































































































# from tkinter import *
# from PIL import Image, ImageTk
# import sqlite3

# conn = sqlite3.connect('loan.db')
# cursor = conn.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS Loan_details(Account_no TEXT UNIQUE, Amount_loan TEXT, Interest TEXT, PPF_Passbook)")

# class PPF_Check:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("PPF Loan Check")
#         self.root.geometry("1100x600")
#         self.root.config(bg="#04D8B2")
#         Label(self.root, text="PPF Loan Check", font=("times new roman", 23, "bold"), bg="#04D8B2", fg="black", anchor="w", padx=10).place(x=750, y=100, relwidth=1)

#         self.Account_no = StringVar()
#         self.amount_loan = StringVar()
#         self.tenure = StringVar()

#         self.image_label = Label(root, bg="#04D8B2")
#         self.image_label.place(x=50, y=120, width=550, height=300)
#         self.image = Image.open("images/loan_check.jpg")
#         self.image = self.image.resize((500, 300))
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.image_label.config(image=self.photo)

#         Account_no_label = Label(root, text="Account No.", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         Account_no_label.place(x=650, y=200)
#         self.Account_no_entry = Entry(root, textvariable=self.Account_no)
#         self.Account_no_entry.place(x=850, y=200)
#         self.Account_no_entry.bind("<KeyRelease>", self.show_details)

#         amount_loan_label = Label(root, text="Loan Amount", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         amount_loan_label.place(x=650, y=240)
#         self.amount_loan_entry = Entry(root, textvariable=self.amount_loan, state='readonly')
#         self.amount_loan_entry.place(x=850, y=240)

#         tenure_label = Label(root, text="Tenure (In year)", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         tenure_label.place(x=650, y=280)
#         self.tenure_entry = Entry(root, textvariable=self.tenure, state='readonly')
#         self.tenure_entry.place(x=850, y=280)

#         check_button = Button(root, text="Check", command=self.show_details, font=("times new roman", 10, "bold"))
#         check_button.place(x=750, y=340)

#         back_button = Button(root, text="Back to Menu", command=self.back_to_menu, font=("times new roman", 10, "bold"))
#         back_button.place(x=850, y=340)

#         self.account_number_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.account_number_error_label.place(x=650, y=220)

#     def back_to_menu(self):
#         self.root.destroy()
#         import Main_menu
#         root = Tk()
#         email = ""
#         Main_menu.Main_Menu(root, email)
#         root.mainloop()

#     def show_details(self, event=None):
#         Account_no = self.Account_no_entry.get()
#         cursor.execute('SELECT * FROM Loan_details WHERE Account_no=?', (Account_no,))
#         account = cursor.fetchone()
#         if account:
#             self.amount_loan.set(account[1])
#             self.tenure.set(account[2])
#             self.account_number_error_label.config(text="")
#         else:
#             self.amount_loan.set("")
#             self.tenure.set("")
#             self.account_number_error_label.config(text="Loan does not exist")

# if __name__ == "__main__":
#     root = Tk()
#     obj = PPF_Check(root)
#     root.mainloop()
