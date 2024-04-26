# Banking System Using OOPs

# Parent class: USer
# Holds Details about an user 
# Has a function to show user details 

# Child class:Bank 
# Stores details about the account Balance
# stores details about the amount 
# allows for deposits, withdraws, view_balance

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

class Bank:
    def __init__(self, name, age, gender):
        self.user = User(name, age, gender)  
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Account Balance has been updated:", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds. Your account Balance is:", self.balance)
        else:
            self.balance -= self.amount
            print("Account Balance has been updated:", self.balance)

    def view_balance(self):
        self.user.show_details()
        print("Your account Balance:", self.balance)


user1 = User('Subham Giri', 24, "Male")
bank_account = Bank('Subham Giri', 24, "Male")
bank_account.deposit(10000)
bank_account.withdraw(1000)
bank_account.view_balance()