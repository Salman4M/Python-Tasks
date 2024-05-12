class BankAccount:
    def __init__(self, my_account_number:int, my_balance:int):
        self.account_number = my_account_number
        self.balance = my_balance

    def deposit(self, cash):
        if cash > 0:
            self.balance += cash

    def withdraw(self, howmuch):
        if howmuch > self.balance:
            return "You don't have enough money in your account"
        self.balance -= howmuch
        return f'Money you take from account is: {howmuch}'

    def get_account_number(self):
        return f'Your account number is: {self.account_number}'

    def get_balance(self):
        return self.balance


class CreditAccount(BankAccount):
    def __init__(self, my_account_number:int, my_balance:int,creditMoney:int):
        super().__init__(my_account_number, my_balance)
        self.creditMoney=creditMoney
        self.pay_money=(creditMoney/12)
        self.timer=0

    def give_credit(self):
        if self.balance >= self.creditMoney / 12:
            return f'You have taken this amount of money for credit: {self.creditMoney}'
        return "Sorry, we are not allowed to lend this amount of money. Your balance has to afford at least a month"

    def pay_credit(self):
            
            if self.timer==12:
                self.creditMoney=0
                return 'Congrats! You have completed your credit.'
            
            
            if self.creditMoney > 0 and self.balance >= self.pay_money:
                
                    self.balance -= self.pay_money
                    self.creditMoney -= self.pay_money
                    self.timer+=1  
                    return f'You have paid for {self.timer}th month:  The remaining credit amount of {self.creditMoney}---{self.pay_money}\n your balance {self.balance}'
            elif self.balance < self.pay_money:
                    return 'You have to increase your balance to pay off the credit.'




# Example usage:
obj = BankAccount(123, 0)
obj.deposit(1149)
print(obj.get_balance())

obj2 = CreditAccount(obj.account_number, obj.balance,1150)

print(obj2.give_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
print(obj2.pay_credit())
# print(obj2.pay_credit())


