

# class Cat:
#     name = "Mestan"
#     color = "white"



# cat1 = Cat()

# print(cat1)
# print(cat1.name)
# print(cat1.color)


# cat2 = Cat()

# print(cat2)
# print(cat2.name)
# print(cat2.color)


# print(cat1 == cat2)



# class Cat:
#     # gender = "female" # --> class attribute

#     def __init__(self, name, color):
#         self.name = name # --> instance attribute
#         self.color = color # --> instance attribute
#         self.gender = "female"



# cat1 = Cat(name="Mestan", color="ag")

# print(cat1)
# print(cat1.name)
# print(cat1.color)
# print(cat1.gender)



class Cat:

    def __init__(self, name, color):
        self.name = name # --> instance attribute
        self.color = color # --> instance attribute
    

    def displayName(self):
        return self.name.upper()
    

    def displayColor(x):
        return x.color.upper()

    def displayData(self, age):
        return f"Name: {self.displayName()}\nColor: {self.displayColor()}\nAge: {age}"



cat1 = Cat(name="Mestan", color="ag")
print(cat1.displayData(age=5))





"""
TASK 1:

1) Bir Dog classi yaradin
    Attribute --> name, color, gender
    Methodlari --> displayData (butun datalari qaytaracaq alt alta), 
                   makeSound (Sadece "Hav hav" qaytaracaq)

    Daha sonra obyekt yaradin ve attribute, methodlari cap edin

"""


class Dog:

    def __init__(self, name, color, gender):
        self.name = name
        self.color = color
        self.gender = gender

    def displayData(self):
        return f"Name: {self.name}\nColor: {self.color}\nGender: {self.gender}"
    
    def makeSound(self):
        return "Hav hav"

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
dog1 = Dog(name="Toplan", color="qara", gender="kisi")
print(dog1.name, dog1.color, dog1.gender)
print(dog1.displayData())
print(dog1.makeSound())



"""
Task 2:
1) Calculator classi yaratmaq lazimdi
    Attributes: --> x, y
    Methods: --> toplama, cixma, vurma, bolme
"""

class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def toplama(self):
        return f"{self.x} + {self.y} = {self.x + self.y}"
    
    def cixma(self):
        return f"{self.x} - {self.y} = {self.x - self.y}"

    def vurma(self):
        return f"{self.x} * {self.y} = {self.x * self.y}"
    
    def bolme(self):
        return f"{self.x} / {self.y} = {self.x / self.y}"


op1 = Calculator(x=20, y=10)

print(op1.toplama())
print(op1.cixma())
print(op1.vurma())
print(op1.bolme())


"""
Task3: 

1) CheckWord classi yaradin
    Attributelari: --> word, word_list
    Methodlari --> check_word

    Ex.1: word="applepieapple", word_list=["apple", "pie"]
            check_word --> True
    
    Ex.2: word = "catsandog", word_list = ["cats", "sand", "dog", "cat", "dogs"]
            check_word --> False
"""


class CheckWord:

    def __init__(self, word, word_list):
        self.word = word
        self.word_list = word_list


    # def update_word_list(self):
    #     self.word_list.sort()
    #     self.word_list = sorted(self.word_list, key=lambda x: len(x))
    #     print(self.word_list)
    
    def check_word(self):
        # self.update_word_list()
        copy_word = self.word

        for i in range(len(self.word_list)):
            for elem in self.word_list[i:]:
                if elem in copy_word:
                    copy_word = copy_word.replace(elem, "")
            
            if copy_word == "":
                return True
            else:
                copy_word = self.word

        return False


# obj1 = CheckWord(word="applepieapple", word_list=["apple", "pie"])
obj1 = CheckWord(word="catsandog", word_list=["cats", "sand", "dog", "cat", "dogs"])
print(obj1.check_word())