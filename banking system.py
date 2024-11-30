from icecream import ic

class Account:
    def __init__(self, bal, acc):
        self.balance = bal  
        self.account = acc  

    # Debit function
    def debit(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount  
        return self.balance

    # Credit function
    def credit(self, amount):
        self.balance += amount  
        return self.balance

res = Account(17000, 123456)
ic("Initial Balance:", res.balance)

ic("After Credit:", res.credit(6000))

ic("After Debit:", res.debit(500))
