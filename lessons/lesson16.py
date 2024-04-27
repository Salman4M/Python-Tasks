class Dunder:
    def __init__(self,name,surname,age,university,password):
        self.name = name #--> public member
        self.surname = surname  #--> public member
        self.age = age  #--> public member

        self._university = university  #--> protected member

        self.__password = password  #--> private member
        
    def _displayUniversity(self):

        return self._university
    
    def displayPassword(self):

        return self.__password



myobj = Dunder(name = "Salman", surname="Mammadli", age = 22, university="UNEC",password="bakugozelseher")


# myobj.name = "Celal"
# print(myobj.name)
# myobj._university = "ADNSU"
# print(myobj._university)
# print(myobj._displayUniversity())

############## we can't call private member outside of class
print(myobj.__password)

#######only inside of class
# print(myobj.displayPassword())



# # #name mangling

# print(vars(myobj))


###### also we can call like this
# print(myobj._Dunder__password)


# class Person:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password

#     def get_password(self):
#         return self.__password
    
#     def set_password(self,new_password):
#         self.__password = new_password
    
#     def del_password(self):
#         del self.__password
    
#     password = property(
#         fget= get_password,
#         fset= set_password,
#         # fdel=None
#         fdel = del_password
#     )

# player1  = Person(username = 'salman4m', password = 'italy123')

# print(player1.get_password())

# player1.set_password("swiss123")

# print(player1.get_password())

# print(player1.password)
# player1.password="koln123"
# print(player1.password)
# print(player1.del_password())
# # player1.set_password("swiss123")
# player1.password="koln134"
# print(player1.password)





class Person:
    def __init__(self,username,password):
        self.username = username
        self.__password = password

### you have to use @property before using @name.setter or  @name.deleter otherwise they are not gonna work out. 
#Also you can access the password outside of class by this method
    @property
    def password(self):
        return self.__password
    
    # password = property(
    #     fget=get_password
    # )
    @password.setter
    def password(self,x):
        self.__password = x

player1  = Person(username = 'salman4m', password = 'italy123')

player1.password="venice123"
print(player1.password)

