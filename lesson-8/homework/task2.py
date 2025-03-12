import random
import json


accounts = {}

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance 

class Bank:
    def __init__(self):
        self.accounts = accounts  

    def create_account(self):
        while True:
            account_number = random.randint(100000, 999999)
            if account_number not in self.accounts:
                break  

        name = input("Enter your name as in your ID: ")
        deposit = float(input("Minimum deposit required: $10. Enter deposit amount: "))

        if deposit >= 10.00:
            self.accounts[account_number] = {
                "name": name,
                "balance": deposit
            }
            print(f"✅ Your account has been created successfully! Your Account Number: {account_number}")

            
            self.save_data()
        else:
            print("❌ Please deposit at least $10 to create an account.")
            self.create_account()

    def view_account(self):
        account_number = int(input("Enter your account number: "))
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"""
            __________________________________________
            Account Number: {account_number}
            Account Owner: {account['name']}
            Account Balance: ${account['balance']}
            __________________________________________
            """)
        else:
            print("❌ Account not found!")

    def add_money(self):
        account_number = int(input("Enter your account number: "))
        if account_number in self.accounts:
            amount = float(input("Enter the amount to deposit: "))
            self.accounts[account_number]['balance'] += amount
            print(f"✅ Successfully deposited ${amount}. New balance: ${self.accounts[account_number]['balance']}")
            self.save_data()
        else:
            print("❌ Account not found!")

    def withdraw_money(self):
        account_number = int(input("Enter your account number: "))
        if account_number in self.accounts:
            amount = float(input("Enter the amount to withdraw: "))
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"✅ Withdrawal successful! New balance: ${self.accounts[account_number]['balance']}")
                self.save_data()
            else:
                print("❌ Insufficient balance!")
        else:
            print("❌ Account not found!")

    def transfer_money(self):
        sender_acc = int(input("Enter your account number: "))
        receiver_acc = int(input("Enter the recipient's account number: "))

        if sender_acc in self.accounts and receiver_acc in self.accounts:
            transfer_amount = float(input("Enter the amount to transfer: "))

            if self.accounts[sender_acc]['balance'] >= transfer_amount:
                self.accounts[sender_acc]['balance'] -= transfer_amount
                self.accounts[receiver_acc]['balance'] += transfer_amount
                print(f"✅ Transfer successful! You sent ${transfer_amount} to {self.accounts[receiver_acc]['name']}.")
                self.save_data()
            else:
                print("❌ Insufficient funds for transfer.")
        else:
            print("❌ Invalid sender or recipient account number!")

    def save_data(self):
        with open("bank_info.json", "w") as f:
            json.dump(self.accounts, f, indent=4)

    def load_data(self):
        try:
            with open("bank_info.json", "r") as f:
                self.accounts = json.load(f)
        except FileNotFoundError:
            self.accounts = {}


bank = Bank()
bank.load_data()

while True: 
    choice = int(input("""\n💰 Welcome to the Banking System! 💰\n
    1️⃣ Create Account
    2️⃣ View Account Details
    3️⃣ Deposit Money
    4️⃣ Withdraw Money
    5️⃣ Transfer Money
    6️⃣ Exit
    Enter your choice: """))

    if choice == 1:
        bank.create_account()
    elif choice == 2:
        bank.view_account()
    elif choice == 3:
        bank.add_money()
    elif choice == 4:
        bank.withdraw_money()
    elif choice == 5:
        bank.transfer_money()
    elif choice == 6:
        print("👋 Exiting the banking system. Have a great day!")
        break
    else:
        print("❌ Invalid choice! Please enter a number between 1-6.")
        continue