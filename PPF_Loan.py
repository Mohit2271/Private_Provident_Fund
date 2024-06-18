from tkinter import *
from tkinter import messagebox
import re
from tkinter import filedialog
from PIL import Image,ImageTk
import sqlite3

conn = sqlite3.Connection('loan.db')
cursor = conn.cursor()
cursor.execute("create table if not exists Loan_details(Account_no text unique, Amount_loan text, Interset text, PPF_Passbook)")

class PPF_Loan:
    def __init__(self, root):
        self.root = root
        self.root.title("PPF Loan")
        self.root.geometry("1000x500")
        self.root.config(bg="#04D8B2")
        Label(self.root, text="PPF Loan", font=("times new roman", 20, "bold"),bg="#04D8B2", fg="black", anchor="w", padx=10).place(x=580, y=80, relwidth=1)

        self.account_no = StringVar()
        self.amount_loan = StringVar()
        self.repaid_amount = StringVar()
        self.PPF_Passbook = StringVar()

        self.image_label = Label(root,bg="#04D8B2")
        self.image_label.place(x=20, y=80,width=450,height=350)
        self.image = Image.open("images\loan.jpg")
        self.image = self.image.resize((400, 250))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)
  
        account_no_label = Label(root, text="Account number:",font=("times new roman",12,"bold"),bg="#04D8B2")
        account_no_label.place(x=480,y=150)
        self.account_no_entry = Entry(root, textvariable=self.account_no)
        self.account_no_entry.place(x=700,y=150)

        amount_loan_label = Label(root, text="Amount of Loan:",font=("times new roman",12,"bold"),bg="#04D8B2")
        amount_loan_label.place(x=480,y=190)
        self.amount_loan_entry = Entry(root, textvariable=self.amount_loan)
        self.amount_loan_entry.place(x=700,y=190)

        repaid_amount_label = Label(root, text="Tenure(In year)",font=("times new roman",12,"bold"),bg="#04D8B2")
        repaid_amount_label.place(x=480,y=230)
        self.repaid_amount_entry = Entry(root, textvariable=self.repaid_amount)
        self.repaid_amount_entry.place(x=700,y=230)

        PPF_Passbook_label = Label(root, text="copy of your PPF Passbook:",font=("times new roman",12,"bold"),bg="#04D8B2")
        PPF_Passbook_label.place(x=480,y=300)
        self.PPF_Passbook_entry = Entry(root, textvariable=self.PPF_Passbook)
        self.PPF_Passbook_entry.place(x=700,y=300)

        browse_button = Button(root, text="Select Photo", command=self.browse_file, cursor="hand2")
        browse_button.place(x=850, y=300)

        self.error_label = Label(self.root,bg="#04D8B2")
        self.error_label.place(x=480,y=340)

        submit_button = Button(root, text="Apply", command=self.validate_ppf_loan,font=("times new roman",10,"bold"), cursor="hand2")
        submit_button.place(x=640,y=360)

        back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",font=("times new roman", 10, "bold"))
        back_to_menu_button.place(x=740,y=360)

    def back_to_menu(self):
        self.root.destroy()
        import Main_menu 
        root = Tk()
        email = ""
        Main_menu.Main_Menu(root, email)
        root.mainloop()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        self.PPF_Passbook.set(file_path)

    def validate_ppf_loan(self):
        account_no = self.account_no_entry.get()
        amount_loan = self.amount_loan_entry.get()
        repaid_amount = self.repaid_amount_entry.get()
        PPF_Passbook = self.PPF_Passbook_entry.get()
        
        if not re.match(r'^\d+$', account_no):
            messagebox.showerror("Error", "Account Number should be a number!")
            return
        if not re.match(r'^\d+(\.\d{1,2})?$', amount_loan):
            messagebox.showerror("Error", "Invalid loan amount!")
            return
        if not re.match(r'^\d+(\.\d{1,2})?$', repaid_amount):
            messagebox.showerror("Error", "Invalid Tenure(In year)!")
            return
        if not PPF_Passbook:
            messagebox.showerror("Error", "PPF Passbook required!")
            return
        else:
            with open(PPF_Passbook, 'rb') as f:
                ppf_passbook_bytes = f.read()
            cursor.execute("Insert into Loan_details(Account_no, Amount_loan, Interset, PPF_Passbook) values (?, ?, ?, ?)", (account_no, amount_loan, repaid_amount, ppf_passbook_bytes))
            conn.commit()
            messagebox.showinfo("Success", "Loan Applied successfully!")
            self.back_to_menu()

if __name__ == "__main__":
    root = Tk()
    obj = PPF_Loan(root)
    root.mainloop()






















































































































































































# from tkinter import *
# from tkinter import messagebox
# import re
# from tkinter import filedialog
# from PIL import Image, ImageTk
# import sqlite3
# import os

# conn = sqlite3.Connection('loan.db')
# cursor = conn.cursor()
# cursor.execute("create table if not exists Loan_details(Account_no text, Amount_loan text, Interset text, PPF_Passbook)")

# class PPF_Loan:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("PPF Loan")
#         self.root.geometry("1000x500")
#         self.root.config(bg="#04D8B2")
#         Label(self.root, text="PPF Loan", font=("times new roman", 20, "bold"), bg="#04D8B2", fg="black",
#               anchor="w", padx=10).place(x=580, y=80, relwidth=1)

#         self.account_no = StringVar()
#         self.amount_loan = StringVar()
#         self.repaid_amount = StringVar()
#         self.PPF_Passbook = StringVar()

#         self.image_label = Label(root, bg="#04D8B2")
#         self.image_label.place(x=20, y=80, width=450, height=350)
#         self.image = Image.open("images/loan.jpg")
#         self.image = self.image.resize((400, 250))
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.image_label.config(image=self.photo)

#         account_no_label = Label(root, text="Account number:", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         account_no_label.place(x=480, y=150)
#         self.account_no_entry = Entry(root, textvariable=self.account_no)
#         self.account_no_entry.place(x=700, y=150)
#         self.account_no_entry.bind("<KeyRelease>", self.validate_ppf_loan)

#         amount_loan_label = Label(root, text="Amount of Loan:", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         amount_loan_label.place(x=480, y=190)
#         self.amount_loan_entry = Entry(root, textvariable=self.amount_loan)
#         self.amount_loan_entry.place(x=700, y=190)
#         self.amount_loan_entry.bind("<KeyRelease>", self.validate_ppf_loan)

#         repaid_amount_label = Label(root, text="Tenure(In year)", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         repaid_amount_label.place(x=480, y=230)
#         self.repaid_amount_entry = Entry(root, textvariable=self.repaid_amount)
#         self.repaid_amount_entry.place(x=700, y=230)
#         self.repaid_amount_entry.bind("<KeyRelease>", self.validate_ppf_loan)

#         PPF_Passbook_label = Label(root, text="Copy of your PPF Passbook:", font=("times new roman", 12, "bold"),
#                                    bg="#04D8B2")
#         PPF_Passbook_label.place(x=480, y=300)
#         self.PPF_Passbook_entry = Entry(root, textvariable=self.PPF_Passbook)
#         self.PPF_Passbook_entry.place(x=700, y=300)
#         self.PPF_Passbook_entry.bind("<KeyRelease>", self.validate_ppf_loan)

#         browse_button = Button(root, text="Select Photo", command=self.browse_file, cursor="hand2")
#         browse_button.place(x=850, y=300)

#         self.error_label = Label(self.root, bg="#04D8B2")
#         self.error_label.place(x=480, y=340)

#         submit_button = Button(root, text="Apply", command=self.validate_ppf_loan, font=("times new roman", 10, "bold"),
#                                cursor="hand2")
#         submit_button.place(x=640, y=360)

#         back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",
#                                      font=("times new roman", 10, "bold"))
#         back_to_menu_button.place(x=740, y=360)

#         self.account_no_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.account_no_error_label.place(x=480, y=170)

#         self.amount_loan_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.amount_loan_error_label.place(x=480, y=210)

#         self.tenure_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.tenure_error_label.place(x=480, y=250)

#         self.PPF_Passbook_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.PPF_Passbook_error_label.place(x=480, y=320)

#     def back_to_menu(self):
#         self.root.destroy()
#         import Main_menu
#         root = Tk()
#         email = ""
#         Main_menu.Main_Menu(root, email)
#         root.mainloop()

#     def browse_file(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
#         self.PPF_Passbook.set(file_path)

#     def validate_ppf_loan(self, event=None):
#         account_no = self.account_no_entry.get()
#         amount_loan = self.amount_loan_entry.get()
#         repaid_amount = self.repaid_amount_entry.get()
#         PPF_Passbook = self.PPF_Passbook_entry.get()

#         if not re.match(r'^\d+$', account_no):
#             self.account_no_error_label.config(text="Account Number should be a number!")
#         else:
#             self.account_no_error_label.config(text="")

#             conn_account = sqlite3.Connection('New_Account.db')
#             cursor_account = conn_account.cursor()

#             cursor_account.execute("SELECT account_number FROM New_Account_details WHERE account_number = ?", (account_no,))

#             result = cursor_account.fetchone()
#             if result is None:
#                 self.account_no_error_label.config(text="Account Number does not exist!")
#             else:
#                 self.account_no_error_label.config(text="")

#         if not re.match(r'^\d+(\.\d{1,2})?$', amount_loan):
#             self.amount_loan_error_label.config(text="Invalid loan amount!")
#         else:
#             self.amount_loan_error_label.config(text="")
#         if not re.match(r'^\d+(\.\d{1,2})?$', repaid_amount):
#             self.tenure_error_label.config(text="Invalid Tenure(In year)!")
#         else:
#             self.tenure_error_label.config(text="")

#         if not PPF_Passbook:
#             self.PPF_Passbook_error_label.config(text="PPF Passbook required!")
#         else:
#             self.PPF_Passbook_error_label.config(text="")
#         if not PPF_Passbook:
#             self.PPF_Passbook_error_label.config(text="PPF Passbook path is empty!")
#         elif not os.path.exists(PPF_Passbook):
#             self.PPF_Passbook_error_label.config(text="PPF Passbook path is incorrect!")
#         else:
#             self.PPF_Passbook_error_label.config(text="")

#         if re.match(r'^\d+$', account_no) and re.match(r'^\d+(\.\d{1,2})?$', amount_loan) and \
#             re.match(r'^\d+(\.\d{1,2})?$', repaid_amount) and PPF_Passbook and \
#             os.path.exists(PPF_Passbook) and result:
#             with open(PPF_Passbook, 'rb') as f:
#                 ppf_passbook_bytes = f.read()
#             cursor.execute(
#                 "INSERT INTO Loan_details(Account_no, Amount_loan, Interset, PPF_Passbook) VALUES (?, ?, ?, ?)",
#                 (account_no, amount_loan, repaid_amount, ppf_passbook_bytes))
#             conn.commit()
#             messagebox.showinfo("Success", "Loan Applied successfully!")
#             self.back_to_menu()

# if __name__ == "__main__":
#     root = Tk()
#     obj = PPF_Loan(root)
#     root.mainloop()
