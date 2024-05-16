# class BankAccount:
#     def __init__(self, account_number:int, balance:int):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, cash):
#         if cash > 0:
#             self.balance += cash

#     def withdraw(self, howmuch):
#         if howmuch > self.balance:
#             return "You don't have enough money in your account"
#         self.balance -= howmuch
#         return f'Money you take from account is: {howmuch}'

#     def get_account_number(self):
#         return f'Your account number is: {self.account_number}'

#     def get_balance(self):
#         return self.balance


# class CreditAccount(BankAccount):
#     def __init__(self, account_number, balance,creditMoney:int):
#         super().__init__(account_number, balance)
#         self.creditMoney=creditMoney
#         self.pay_money=(creditMoney/12)
#         self.timer=0

#     def give_credit(self):
#         if self.balance >= self.creditMoney / 12:
#             self.balance += self.creditMoney
#             return f'You have taken this amount of money for credit: {self.creditMoney}'
#         return "Sorry, we are not allowed to lend this amount of money. Your balance has to afford at least a month"

#     def pay_credit(self):
            
#             if self.timer==12 and self.creditMoney<0:
#                 self.balance+=abs(self.creditMoney)
#                 self.creditMoney=0
#                 return 'Congrats! You have completed your credit.'
            
            
#             if self.creditMoney > 0 and self.balance >= self.pay_money:
                
#                     self.balance -= self.pay_money
#                     self.creditMoney -= self.pay_money
#                     self.timer+=1  
#                     return f'You have paid for {self.timer}th month:  The remaining credit amount of {self.creditMoney}---{self.pay_money}\n your balance {self.balance}'
#             elif self.balance < self.pay_money:
#                     return 'You have to increase your balance to pay off the credit.'




# # Example usage:
# obj = BankAccount(123, 0)
# obj.deposit(1151)
# print(obj.get_balance())


# obj2 = CreditAccount(obj.account_number, obj.balance,1150)

# print(obj2.pay_money,obj2.balance)
# print(obj2.give_credit())

# for i in range(13):
#     print(obj2.pay_credit())




class Hesab:
    def _init_(self, hesab_nomresi: int, balans: float):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def balans_artir(self, mebleq):
        """Hesabın balansını artırmaq"""
        self.balans += mebleq
        print(f"{mebleq} AZN balansınıza əlavə edildi. Yeni balansınız: {self.balans} AZN")

    def pul_cixar(self, mebleq):
        """Hesabdan pul çıxarmaq"""
        if mebleq <= self.balans:
            self.balans -= mebleq
            print(f"{mebleq} AZN balansınızdan çıxarıldı. Yeni balansınız: {self.balans} AZN")
        else:
            print("Balansınızda kifayət qədər vəsait yoxdur.")

    def balans_goster(self):
        """Hesabın balansını göstərmək"""
        print(f"Hesabınızın balansı: {self.balans} AZN")


class Kredit(Hesab):
    def _init_(self, hesab_nomresi: int, balans: float, kredit_mebli: float):
        super()._init_(hesab_nomresi, balans)
        self.kredit_mebli = kredit_mebli

    def kredit_ver(self):
        """Kredit almaq"""
        self.balans += self.kredit_mebli
        print(f"{self.kredit_mebli} AZN kredit olaraq hesabınıza əlavə edildi.")

    def kredit_odenişi(self):
        """Kredit ödənişi etmək"""
        ayliq_odenis = self.kredit_mebli / 12
        if ayliq_odenis <= self.balans:
            self.balans -= ayliq_odenis
            print(f"Kredit ödənişi edildi. Yeni balansınız: {self.balans} AZN")
        else:
            print("Kredit ödənişini etmək üçün kifayət qədər balansınız yoxdur.")


# Bank Hesabı yaratmaq və əməliyyatlar etmək
hesab = Hesab(123456, 1000)
hesab.balans_goster()
hesab.balans_artir(500)
hesab.pul_cixar(200)

# Kredit alaraq ödəniş etmək
kredit = Kredit(789012, 2000, 12000)
kredit.balans_goster()
kredit.kredit_ver()
kredit.kredit_odenişi()
kredit.balans_goster()