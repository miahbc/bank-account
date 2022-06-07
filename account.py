class Account(Bank):
    def __init__(self,name, id, balance,bank_name):
        super().__init__(self,bank_name)
        self.account = name
        self.id = id
        if balance < 0:
            raise Exception("We apologize, an account cannot be set up with a negative balance.")
        else:
            self.balance = balance

    def withdraw(self, withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount            
        if withdrawal_amount > self.balance:
            raise Exception("We apologize, you don't have enough funds to complete this transaction.")
        else:
            self.balance -= withdrawal_amount
        return self.balance

    def deposit(self,deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance += deposit_amount
        return self.balance
