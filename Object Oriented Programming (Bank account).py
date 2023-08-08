# python Object Oriented Programming using class
# Bank account and bank withdraw and deposit function
# We have to decide on the account number, current balance, withdraw_limit, and transfer limit

class Bank:

    def __init__(self,account_number,balance,withdraw_limit,transfer_limit):
        self.account_number = account_number
        self.balance = balance
        self.withdraw_limit = withdraw_limit
        self.transfer_limit = transfer_limit

    def withraw(self,amount):
        if self.balance < amount:
            print('Insufficient Balance')
        elif amount < self.withdraw_limit:
            self.balance = self.balance - amount
            return self.balance
        else:
            print('The amount exceed withdraw limit')

    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance

    def transfer(self,other,amount):
        if self.balance < amount:
            print('Insufficient Balance')
        elif amount < self.transfer_limit:
            self.balance = self.balance - amount
            other.balance = other.balance + amount
            return self.balance, other.balance
        else:
            print('The amount exceed transfer limit')

    @classmethod
    def add_account(cls, acc_str):
        account_number, balance, withdraw_limit,transfer_limit = acc_str.split('-')
        return cls(account_number,balance, withdraw_limit, transfer_limit)



# to test the code above run the code below
# the account information is as below
acc_1 = Bank('B2023080801',5000,1000,1000)
acc_2 = Bank('B2023080802',8400,1000,500)
acc_3 = Bank('B2023080803',800,1000,1000)

# withdraw and deposit function
print(acc_1.balance)
acc_1.withraw(500)
print(acc_1.balance)
acc_1.deposit(500)
print(acc_1.balance)

#transfer sufficient balance
acc_1.transfer(acc_2,800)
print(acc_1.balance)
print(acc_2.balance)

# transfer insufficient balance
acc_3.transfer(acc_2,900)
print(acc_3.balance)
print(acc_2.balance)

# add new account
new_account = 'B2023080804-2500-1000-1000'
acc_4 = Bank.add_account(new_account)
print(acc_4.account_number + ' balance is ' + acc_4.balance)