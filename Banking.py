class Bank:
    user = "Ibrahim"

    def __init__(self,balance):
        self.balance = balance
        self.max_withdrow = 10000
        self.min_withdrow = 500

    def get_balance(self):
        return self.balance

    def deposite(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdrow(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount < self.min_withdrow:
            print("At least withdrew ", self.min_withdrow, "Taka")
        else:
            self.balance = self.balance - amount,
            return self.balance


banking = Bank(20000)


new_balance = banking.withdrow(5000)
my_bal = banking.get_balance()
print(my_bal)
