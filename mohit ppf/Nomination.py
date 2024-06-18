from tkinter import *
from tkinter import messagebox
import re
from tkcalendar import DateEntry
from PIL import Image,ImageTk
import sqlite3
from datetime import date

conn = sqlite3.connect('Nomination.db')
cursor = conn.cursor()
cursor.execute("create table if not exists Nominee_details(Account_holder_name text, nominee_name text, nominee_relationship text, account_no text, nominee_address text, DOB text)")

class Nomination:
    def __init__(self, root):
        self.root = root
        self.root.title("Nomination Form")
        self.root.geometry("1000x500")
        self.root.config(bg="#04D8B2")
        Label(self.root, text="Nomination Form", font=("times new roman", 20, "bold"),bg="#04D8B2", fg="black", anchor="w", padx=10).place(x=580, y=50, relwidth=1)

        self.account_holder_name = StringVar()
        self.nominee_name = StringVar()
        self.nominee_relationship = StringVar()
        self.account_no = StringVar()
        self.nominee_address = StringVar()
        self.DOB = StringVar()

        self.image_label = Label(root,bg="#04D8B2")
        self.image_label.place(x=20, y=80,width=450,height=350)
        self.image = Image.open("images\imagenomination.jpg")
        self.image = self.image.resize((400, 250))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)
  
        account_holder_name_label = Label(root, text="Account Holder Name:",font=("times new roman",12,"bold"),bg="#04D8B2")
        account_holder_name_label.place(x=480,y=130)
        self.account_holder_name_entry = Entry(root, textvariable=self.account_holder_name)
        self.account_holder_name_entry.place(x=700,y=130)

        nominee_name_label = Label(root, text="Nominee Name:",font=("times new roman",12,"bold"),bg="#04D8B2")
        nominee_name_label.place(x=480,y=190)
        self.nominee_name_entry = Entry(root, textvariable=self.nominee_name)
        self.nominee_name_entry.place(x=700,y=190)

        nominee_relationship_label = Label(root, text="Nominee Relationship:",font=("times new roman",12,"bold"),bg="#04D8B2")
        nominee_relationship_label.place(x=480,y=230)
        self.nominee_relationship_entry = Entry(root, textvariable=self.nominee_relationship)
        self.nominee_relationship_entry.place(x=700,y=230)

        account_no_label = Label(root, text="PPF Account No.:",font=("times new roman",12,"bold"),bg="#04D8B2")
        account_no_label.place(x=480,y=270)
        self.account_no_entry = Entry(root, textvariable=self.account_no)
        self.account_no_entry.place(x=700,y=270)

        nominee_address_label = Label(root, text="Nominee Address:",font=("times new roman",12,"bold"),bg="#04D8B2")
        nominee_address_label.place(x=480,y=310)
        self.nominee_address_entry = Entry(root, textvariable=self.nominee_address)
        self.nominee_address_entry.place(x=700,y=310)

        def calculate_age(event):
             dob = self.DOB_entry.get_date()
             today = date.today()
             age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
             if age < 18:
               messagebox.showerror("Error", "Age must be at least 18 years.")

        DOB_label = Label(root, text="Nominee DOB:", font=("times new roman", 12, "bold"), bg="#04D8B2")
        DOB_label.place(x=480, y=350)

        self.DOB_entry = DateEntry(root, font=("Helvetica", 11), date_pattern="mm/dd/yyyy")
        self.DOB_entry.place(x=700, y=350)
        self.DOB_entry.bind("<<DateEntrySelected>>", calculate_age)

        self.error_label = Label(self.root,bg="#04D8B2")
        self.error_label.place(x=480,y=430)

        submit_button = Button(root, text="Submit", command=self.validate_nomination,font=("times new roman",10,"bold"), cursor="hand2")
        submit_button.place(x=650,y=400)

        back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",font=("times new roman", 10, "bold"))
        back_to_menu_button.place(x=750,y=400)

    def back_to_menu(self):
        self.root.destroy()
        import Main_menu 
        root = Tk()
        email = ""
        Main_menu.Main_Menu(root, email)
        root.mainloop()

    def validate_nomination(self):
        account_holder_name = self.account_holder_name_entry.get()
        nominee_name = self.nominee_name_entry.get()
        nominee_relationship = self.nominee_relationship_entry.get()
        account_no = self.account_no_entry.get()
        nominee_address = self.nominee_address_entry.get()
        DOB = self.DOB_entry.get_date()

        if not account_holder_name:
            messagebox.showerror("Error", "account_holder_name is required!")
        elif not account_holder_name.replace(' ','').isalpha():
            messagebox.showerror("Error", "account_holder_name should contain only alphabets and spaces!")
        elif len(account_holder_name) > 50:
            messagebox.showerror("Error", "account_holder_name should be less than or equal to 50 characters!")

        elif not nominee_name:
            messagebox.showerror("Error", "nominee_name is required!")
        elif not nominee_name.replace(' ','').isalpha():
            messagebox.showerror("Error", "nominee_name should contain only alphabets and spaces!")
        elif len(nominee_name) > 50:
            messagebox.showerror("Error", "nominee_name should be less than or equal to 50 characters!")

        elif not nominee_relationship:
            messagebox.showerror("Error", "nominee_relationship is required!")
        elif not nominee_relationship.replace(' ','').isalpha():
            messagebox.showerror("Error", "nominee_relationship should contain only alphabets and spaces!")
        elif len(nominee_relationship) > 50:
            messagebox.showerror("Error", "nominee_relationship should be less than or equal to 50 characters!")
        elif not account_no:
            messagebox.showerror("Error", "account_no is required!")

        elif not nominee_address:
            messagebox.showerror("nominee_address is required!")
        elif not re.match(r'^[a-zA-Z0-9/ ]+$', nominee_address):
            messagebox.showerror("nominee_address should contain only letters, numbers, spaces, and '/'.")
        elif len(nominee_address) > 50:
            messagebox.showerror("nominee_address should be less than or equal to 50 characters!")
        elif DOB is None:
            messagebox.showerror("Error", "Please enter a valid date of birth!")
        else:
            conn = sqlite3.connect('New_Account.db')
            cursor = conn.cursor()      
            cursor.execute('SELECT Name, account_number FROM New_Account_details WHERE Name = ? and account_number = ?', (account_holder_name, account_no))
            Holder_name = cursor.fetchone()
            if Holder_name:
                conn_nomination = sqlite3.connect('Nomination.db')
                cursor_nomination = conn_nomination.cursor()
                cursor_nomination.execute("INSERT INTO Nominee_details(Account_holder_name, nominee_name, nominee_relationship, account_no, nominee_address, DOB) VALUES (?, ?, ?, ?, ?, ?)",
               (account_holder_name, nominee_name, nominee_relationship, account_no, nominee_address, DOB))
                conn_nomination.commit()
                messagebox.showinfo("Success", "Nominee added successfully!")
                self.back_to_menu()
            else:
                messagebox.showerror("Error", "Account holder name is not matching with account no.")
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Nomination(root)
    root.mainloop()






































































































































































# from tkinter import *
# from tkinter import messagebox
# import re
# from tkcalendar import DateEntry
# from PIL import Image,ImageTk
# import sqlite3
# from datetime import date

# conn = sqlite3.connect('Nomination.db')
# cursor = conn.cursor()
# cursor.execute("create table if not exists Nominee_details(Account_holder_name text, nominee_name text, nominee_relationship text, account_no text, nominee_address text, DOB text)")

# class Nomination:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Nomination Form")
#         self.root.geometry("1000x500")
#         self.root.config(bg="#04D8B2")
#         Label(self.root, text="Nomination Form", font=("times new roman", 20, "bold"),bg="#04D8B2", fg="black", anchor="w", padx=10).place(x=580, y=50, relwidth=1)

#         self.account_holder_name = StringVar()
#         self.nominee_name = StringVar()
#         self.nominee_relationship = StringVar()
#         self.account_no = StringVar()
#         self.nominee_address = StringVar()
#         self.DOB = StringVar()

#         self.image_label = Label(root,bg="#04D8B2")
#         self.image_label.place(x=20, y=80,width=450,height=350)
#         self.image = Image.open("images\imagenomination.jpg")
#         self.image = self.image.resize((400, 250))
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.image_label.config(image=self.photo)
  
#         account_holder_name_label = Label(root, text="Account Holder Name:",font=("times new roman",12,"bold"),bg="#04D8B2")
#         account_holder_name_label.place(x=480,y=130)
#         self.account_holder_name_entry = Entry(root, textvariable=self.account_holder_name)
#         self.account_holder_name_entry.place(x=700,y=130)
#         self.account_holder_name_entry.bind("<KeyRelease>", self.validate_account_holder_name)

#         nominee_name_label = Label(root, text="Nominee Name:",font=("times new roman",12,"bold"),bg="#04D8B2")
#         nominee_name_label.place(x=480,y=190)
#         self.nominee_name_entry = Entry(root, textvariable=self.nominee_name)
#         self.nominee_name_entry.place(x=700,y=190)
#         self.nominee_name_entry.bind("<KeyRelease>", self.validate_nominee_name)

#         nominee_relationship_label = Label(root, text="Nominee Relationship:",font=("times new roman",12,"bold"),bg="#04D8B2")
#         nominee_relationship_label.place(x=480,y=230)
#         self.nominee_relationship_entry = Entry(root, textvariable=self.nominee_relationship)
#         self.nominee_relationship_entry.place(x=700,y=230)
#         self.nominee_relationship_entry.bind("<KeyRelease>", self.validate_nominee_relationship)

#         account_no_label = Label(root, text="PPF Account No.:",font=("times new roman",12,"bold"),bg="#04D8B2")
#         account_no_label.place(x=480,y=270)
#         self.account_no_entry = Entry(root, textvariable=self.account_no)
#         self.account_no_entry.place(x=700,y=270)

#         nominee_address_label = Label(root, text="Nominee Address:",font=("times new roman",12,"bold"),bg="#04D8B2")
#         nominee_address_label.place(x=480,y=310)
#         self.nominee_address_entry = Entry(root, textvariable=self.nominee_address)
#         self.nominee_address_entry.place(x=700,y=310)
#         self.nominee_address_entry.bind("<KeyRelease>", self.validate_nominee_address)

#         def calculate_age(event):
#             dob = self.DOB_entry.get_date()
#             today = date.today()
#             age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
#             if age < 18:
#                self.dob_error_label.config(text="Age must be at least 18 years")
#             else :
#                 self.dob_error_label.config(text="")

#         DOB_label = Label(root, text="Nominee DOB:", font=("times new roman", 12, "bold"), bg="#04D8B2")
#         DOB_label.place(x=480, y=350)

#         self.DOB_entry = DateEntry(root, font=("Helvetica", 11), date_pattern="mm/dd/yyyy")
#         self.DOB_entry.place(x=700, y=350)
#         self.DOB_entry.bind("<<DateEntrySelected>>", calculate_age)

#         self.dob_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.dob_error_label.place(x=480,y=370)

#         submit_button = Button(root, text="Submit", command=self.validate_nomination,font=("times new roman",10,"bold"), cursor="hand2")
#         submit_button.place(x=650,y=400)

#         back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2",font=("times new roman", 10, "bold"))
#         back_to_menu_button.place(x=750,y=400)

#         self.account_holder_name_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.account_holder_name_error_label.place(x=480, y=160)

#         self.nominee_name_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.nominee_name_error_label.place(x=480, y=210)

#         self.nominee_relationship_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.nominee_relationship_error_label.place(x=480, y=250)

#         self.nominee_address_error_label = Label(root, text="", font=("times new roman", 9), fg="red", bg="#04D8B2")
#         self.nominee_address_error_label.place(x=480, y=330)

#     def back_to_menu(self):
#         self.root.destroy()
#         import Main_menu 
#         root = Tk()
#         email = ""
#         Main_menu.Main_Menu(root, email)
#         root.mainloop()

#     def validate_account_holder_name(self,event):
#         account_holder_name = self.account_holder_name_entry.get()

#         if not account_holder_name:
#             self.account_holder_name_error_label.config(text="account_holder_name is required!")
#         elif not account_holder_name.replace(' ','').isalpha():
#             self.account_holder_name_error_label.config(text="account_holder_name should contain only alphabets and spaces!")
#         elif len(account_holder_name) > 50:
#             self.account_holder_name_error_label.config(text="account_holder_name should be less than or equal to 50 characters!")
#         else:
#             self.account_holder_name_error_label.config(text="")

#     def validate_nominee_name(self,event):
#         nominee_name = self.nominee_name_entry.get()

#         if not nominee_name:
#             self.nominee_name_error_label.config(text="nominee_name is required!")
#         elif not nominee_name.replace(' ','').isalpha():
#             self.nominee_name_error_label.config(text="nominee_name should contain only alphabets and spaces!")
#         elif len(nominee_name) > 50:
#             self.nominee_name_error_label.config(text="nominee_name should be less than or equal to 50 characters!")
#         else:
#             self.nominee_name_error_label.config(text="")

#     def validate_nominee_relationship(self,event):
#         nominee_relationship = self.nominee_relationship_entry.get()

#         if not nominee_relationship:
#             self.nominee_relationship_error_label.config(text="nominee_relationship is required!")
#         elif not nominee_relationship.replace(' ','').isalpha():
#             self.nominee_relationship_error_label.config(text="nominee_relationship should contain only alphabets and spaces!")
#         elif len(nominee_relationship) > 50:
#             self.nominee_relationship_error_label.config(text="nominee_relationship should be less than or equal to 50 characters!")
#         else:
#             self.nominee_relationship_error_label.config(text="")

#     def validate_nominee_address(self,event):
#         nominee_address = self.nominee_address_entry.get()

#         if not nominee_address:
#             self.nominee_address_error_label.config(text="nominee_address is required!")
#         elif not re.match(r'^[a-zA-Z0-9/ ]+$', nominee_address):
#             self.nominee_address_error_label.config(text="nominee_address should contain only letters, numbers, spaces, and '/'")
#         elif len(nominee_address) > 50:
#             self.nominee_address_error_label.config(text="nominee_address should be less than or equal to 50 characters!")
#         else:
#             self.nominee_address_error_label.config(text="")


#     def validate_nomination(self):
#         account_holder_name = self.account_holder_name_entry.get()
#         nominee_name = self.nominee_name_entry.get()
#         nominee_relationship = self.nominee_relationship_entry.get()
#         account_no = self.account_no_entry.get()
#         nominee_address = self.nominee_address_entry.get()
#         DOB = self.DOB_entry.get_date()

#         conn = sqlite3.connect('New_Account.db')
#         cursor = conn.cursor()      
#         cursor.execute('SELECT Name, account_number FROM New_Account_details WHERE Name = ? and account_number = ?', (account_holder_name, account_no))
#         Holder_name = cursor.fetchone()
#         if Holder_name:
#             conn_nomination = sqlite3.connect('Nomination.db')
#             cursor_nomination = conn_nomination.cursor()
#             cursor_nomination.execute("INSERT INTO Nominee_details(Account_holder_name, nominee_name, nominee_relationship, account_no, nominee_address, DOB) VALUES (?, ?, ?, ?, ?, ?)",
#            (account_holder_name, nominee_name, nominee_relationship, account_no, nominee_address, DOB))
#             conn_nomination.commit()
#             messagebox.showinfo("Success", "Nominee added successfully!")
#             self.back_to_menu()
#         else:
#             messagebox.showerror("Error", "Account holder name is not matching with account no.")
#     conn.close()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Nomination(root)
#     root.mainloop()
    
    