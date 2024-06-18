import sqlite3
from tkinter import *
from tkinter import ttk
from Main_menu import Main_Menu

class ShowTransactions:
    def __init__(self, root):
        self.root = root
        self.root.title("Show Transactions")
        self.root.geometry("1000x500")
        self.root.config(bg="#04D8B2")

        self.transactions = []

        Label(self.root, text="Show Transactions", font=("times new roman", 20, "bold"), bg="#04D8B2", fg="black", anchor="w", padx=10).place(x=400, y=50, relwidth=1)

        self.account_number = StringVar()
        self.account_number_label = Label(root, text="Account Number:", font=("times new roman", 11, "bold"), bg="#04D8B2")
        self.account_number_label.place(x=200, y=150)
        self.account_number_entry = Entry(root, textvariable=self.account_number)
        self.account_number_entry.place(x=350, y=150)

        self.show_button = Button(root, text="Show Details", command=self.show_details, font=("times new roman", 10, "bold"), cursor="hand2")
        self.show_button.place(x=300, y=200)

        self.transaction_treeview = ttk.Treeview(root, columns=( "amount", "date", "time", "type"))        
        self.transaction_treeview.heading("amount", text="Amount")
        self.transaction_treeview.heading("date", text="Date")
        self.transaction_treeview.heading("time", text="Time")
        self.transaction_treeview.heading("type", text="Transaction Type")
        self.transaction_treeview['show'] = 'headings'
        self.transaction_treeview.place(x=150, y=250)

        back_to_menu_button = Button(root, text="Back to menu", command=self.back_to_menu, cursor="hand2", font=("times new roman", 10, "bold"))
        back_to_menu_button.place(x=400, y=200)

    def back_to_menu(self):
        self.root.destroy()
        root = Tk()
        email = ""
        Main_Menu(root, email)
        root.mainloop()

    def show_details(self):
        account_number = self.account_number.get()
        self.fetch_transactions_from_database(account_number)
        self.fetch_withdrawals_from_database(account_number)
        self.display_transactions()

    def fetch_transactions_from_database(self, account_number):
        conn = sqlite3.connect("deposit.db")
        cursor = conn.cursor()
        cursor.execute("SELECT  amount, date, time FROM deposit WHERE account_number = ?", (account_number,))
        self.transactions = cursor.fetchall()
        cursor.close()
        conn.close()

    def fetch_withdrawals_from_database(self, account_number):
        conn = sqlite3.connect("withdrawal.db")
        cursor = conn.cursor()
        cursor.execute("SELECT -amount, date, time FROM withdrawal WHERE account_number = ?", (account_number,))
        withdrawal_transactions = cursor.fetchall()
        cursor.close()
        conn.close()

        self.transactions.extend(withdrawal_transactions)

    def display_transactions(self):
        self.clear_transaction_treeview()
        for transaction in self.transactions:
            amount,date, time = transaction
            transaction_type = "Credit" if amount > 0 else "Debit"
            amount = abs(amount)
            self.transaction_treeview.insert("", "end", values=(amount, date, time, transaction_type))

    def clear_transaction_treeview(self):
        self.transaction_treeview.delete(*self.transaction_treeview.get_children())

if __name__ == "__main__":
    root = Tk()
    show_transactions = ShowTransactions(root)
    root.mainloop()
