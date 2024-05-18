
"""
@classmethod
"""

# from datetime import datetime

# class Person:

#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
    

#     def display_data(self):
#         return f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}"
    
#     @classmethod
#     def create_person_with_year(cls, name1, surname1, year):
#         return cls(
#             name=name1,
#             surname=surname1,
#             age=datetime.now().year - year
#         )


# obj = Person(name="Fuad", surname="Huseynov", age=23)
# print(obj.display_data())


# obj2 = Person.create_person_with_year(
#     name1="Ferid", surname1="Eliyev", year=2004
# )
# print(obj2.display_data())



"""
@staticmethod  
"""
class CalculateNetProfit:

    def __init__(self, net_profit, tax, currency):
        self.net_profit = net_profit
        self.tax = tax
        self.currency = currency
    

    @staticmethod
    def convert_usd_to_azn(net_profit, currency,tax):
        if currency == "USD":
            return net_profit * 1.7 - tax
        return net_profit - tax

    def get_salary(self):
        return self.convert_usd_to_azn(
            net_profit=self.net_profit, currency=self.currency ,tax = self.tax) - self.tax


###classın içərisində normal qaydada istifadə edirik
obj=CalculateNetProfit(net_profit=400,tax=10,currency='USD')

print(obj.get_salary())


###### classdan kənarda isə static metodumuzun adı və dəyərləri
print(CalculateNetProfit.convert_usd_to_azn(100, "USD",10))
print(CalculateNetProfit.convert_usd_to_azn(39, "AZN",10))

