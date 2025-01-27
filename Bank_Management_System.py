import random
import getpass

class Bank_account:
    def __init__(self, account_name, account_number, account_type, name, age, gender, phone_number, password, ifsc_code, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.account_type = account_type
        self.name = name
        self.gender = gender
        self.age = age
        self.phone_number = phone_number
        self.password = password
        self.ifsc_code = ifsc_code
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited: {amount}.New balance{self.balance}")
            
        else:
            print("Invalid Input, Please Enter Money in the form of digits only")
            
    def withdraw(self, amount):
        if 0<amount<=self.balance:
            self.balance -= amount
            print(f"Amount withdrawn: {amount},New balance{self.balance}")
            
    def check_balance(self):
        return self.balance
    
    def account_details_tuples(self):
        return (self.account_name, self.account_number, self.account_type, self.name, self.age, self.gender, self.phone_number, self.password, self.ifsc_code, self.balance)
    
    def create_account(accounts):
        account_name = random.choice(["SBI", "HDFC", "ICICI", "AXIS", "KOTAK", "CANARA",])
        account_number = random.randint(10**11, 10**12-1)
        account_type = random.choice(["Savings", "Current"])
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your Gender: ")
        phone_number = random.randint(10**9, 10**10-1)
        password = getpass.getpass("Enter your password: ") # getpass.getpass() is used to hide the password while security purpose.
        ifsc_code = random.randint(1000000000, 9999999999)
        initial_balance = float(int(input("Enter the initial balance: ")))
        
        new_account = Bank_account(account_name, account_number, account_type, name, age, gender, phone_number, password, ifsc_code, initial_balance)
        accounts.append(new_account)
        print(f"Account Created Successfully. Your Account Number is {account_number}")
        
    def enter_existing_account(accounts):
        account_number = int(input("Enter your account number: "))
        password = getpass.getpass("Enter your password: ") # getpass.getpass() is used to hide the password while security purpose.
        
        for account in accounts:
            if account.account_number == account_number and account.password == password:
                return account
            print("Invalid account number or password")
            return None
        
    def display_all_accounts(accounts):
        print("\nAll accounts:")
        for account in accounts:
            print(f"Account name: {account.account_name}, Account number: {account.account_number}, Account type: {account.account_type}, Name: {account.name}, Gender: {account.gender}, Phone number: {account.phone_number}, IFSC code: {account.ifsc_code}, Balance: {account.check_balance()}")
    
    def edit_account(accounts):
        account_number = int(input("Enter your account number: "))
        password = getpass.getpass("Enter your password: ")
        
        for account in accounts:
            if account.account_number == account_number and account.password == password:
                print("1. Change account name")
                print("2 change account number")
                print("3. Change account type")
                print("4. Change name")
                print("5. change age")
                print("6. change gender")
                print("7. Change phone number")
                print("8. Change password")
                print("9. Change IFSC code")
                print("10. Change balance")
                
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    account.account_name = input("Enter the new account name: ")
                    
                elif choice == 2:
                    account.account_number = int(input("Enter the new account number: "))
                    
                elif choice == 3:
                    account.account_type = input("Enter the new account type: ")
                    
                elif choice == 4:
                    account.name = input("Enter the new name: ")
                    
                elif choice == 5:
                    account.age = int(input("Enter the new age: "))
                    
                elif choice == 6:
                    account.gender = input("Enter the new gender: ")
                    
                elif choice == 7:
                    account.phone_number = input("Enter the new phone number: ")
                    
                elif choice == 8:
                    account.password = getpass.getpass("Enter the new password: ")
                    
                elif choice == 9:
                    account.ifsc_code = int(input("Enter the new IFSC code: "))
                    
                elif choice == 10:
                    account.balance = float(int(input("Enter the new balance: ")))
                    
                print("Account edited successfully")
                return
            
            else:
                print("Invalid account number or password")
                
accounts = []

while True:
    print("\nBANK MANAGEMENT SYSTEM")
    print("1. Create account")
    print("2. Enter existing account")
    print("3. Display all accounts")
    print("4. Edit account")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        Bank_account.create_account(accounts)
        
    elif choice == 2:
        existing_account = Bank_account.enter_existing_account(accounts)
        
        if existing_account:
            while True:
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check balance")
                print("4. Display account details")
                print("5. Exit")
                
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    amount = float(input("Enter the amount to be deposited: "))
                    existing_account.deposit(amount)
                    
                elif choice == 2:
                    amount = float(input("Enter the amount to be withdrawn: "))
                    existing_account.withdraw(amount)
                    
                elif choice == 3:
                    print(f"Balance: {existing_account.check_balance()}")
                    
                elif choice == 4:
                    print(f"Account details: {existing_account.account_details_tuples()}")
                    
                elif choice == 5:
                    break
                
    elif choice == 3:
        Bank_account.display_all_accounts(accounts)
        
    elif choice == 4:
        Bank_account.edit_account(accounts)
        
    elif choice == 5:
        break
    
    else:
        print("Invalid choice")
    
            
                
                                            
                            
                
            