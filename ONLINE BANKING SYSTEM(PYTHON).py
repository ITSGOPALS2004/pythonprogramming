import tkinter as tk
from tkinter import messagebox

class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return self.balance

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.bank = Bank()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.balance_label = tk.Label(self, text="Balance: $0")
        self.balance_label.pack()

        self.deposit_entry = tk.Entry(self)
        self.deposit_entry.pack()

        self.deposit_button = tk.Button(self)
        self.deposit_button["text"] = "Deposit"
        self.deposit_button["command"] = self.deposit_money
        self.deposit_button.pack()

        self.withdraw_entry = tk.Entry(self)
        self.withdraw_entry.pack()

        self.withdraw_button = tk.Button(self)
        self.withdraw_button["text"] = "Withdraw"
        self.withdraw_button["command"] = self.withdraw_money
        self.withdraw_button.pack()

    def deposit_money(self):
        amount = float(self.deposit_entry.get())
        self.bank.deposit(amount)
        self.balance_label["text"] = "Balance: $" + str(self.bank.balance)
        messagebox.showinfo("Success", "Deposit successful")

    def withdraw_money(self):
        amount = float(self.withdraw_entry.get())
        result = self.bank.withdraw(amount)
        if isinstance(result, str):
            messagebox.showinfo("Error", result)
        else:
            self.balance_label["text"] = "Balance: $" + str(self.bank.balance)
            messagebox.showinfo("Success", "Withdrawal successful")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
