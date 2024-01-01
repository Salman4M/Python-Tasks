

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



# class Cat:

#     def __init__(self, name, color):
#         self.name = name # --> instance attribute
#         self.color = color # --> instance attribute
    

#     def displayName(self):
#         return self.name.upper()
    

#     def displayColor(x):
#         return x.color.upper()

#     def displayData(self, age):
#         return f"Name: {self.displayName()}\nColor: {self.displayColor()}\nAge: {age}"



# cat1 = Cat(name="Mestan", color="ag")
# print(cat1.displayData(5))





# """
# TASK 1:

# 1) Bir Dog classi yaradin
#     Attribute --> name, color, gender
#     Methodlari --> displayData (butun datalari qaytaracaq alt alta), 
#                    makeSound (Sadece "Hav hav" qaytaracaq)

#     Daha sonra obyekt yaradin ve attribute, methodlari cap edin

# """

# class dog:

#     def __init__(self, name,color,gender):
#         self.name = name
#         self.color = color
#         self.gender = gender
    
#     def displayData(self):
#         return self.name, self.color, self.gender
    
#     def makeSound(self):
#         return "HavHav"
    
# dogs = dog(name = "Toplan",color =  "brown" , gender = "its")

# print(dogs.displayData())
# print(dogs.makeSound())


# class Dog:

#     def __init__(self, name, color, gender):
#         self.name = name
#         self.color = color
#         self.gender = gender

#     def displayData(self):
#         return f"Name: {self.name}\nColor: {self.color}\nGender: {self.gender}"
    
#     def makeSound(self):
#         return "Hav hav"

# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# dog1 = Dog(name="Toplan", color="qara", gender="kisi")
# print(dog1.name, dog1.color, dog1.gender)
# print(dog1.displayData())
# print(dog1.makeSound())



# """
# Task 2:
# 1) Calculator classi yaratmaq lazimdi
#     Attributes: --> x, y
#     Methods: --> toplama, cixma, vurma, bolme
# """

# class Calculator:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def toplama(self):
#         return f"{self.x} + {self.y} = {self.x + self.y}"
    
#     def cixma(self):
#         return f"{self.x} - {self.y} = {self.x - self.y}"

#     def vurma(self):
#         return f"{self.x} * {self.y} = {self.x * self.y}"
    
#     def bolme(self):
#         return f"{self.x} / {self.y} = {self.x / self.y}"


# op1 = Calculator(x=20, y=10)

# print(op1.toplama())
# print(op1.cixma())
# print(op1.vurma())
# print(op1.bolme())


# """
# Task3: 

# 1) CheckWord classi yaradin
#     Attributelari: --> word, word_list
#     Methodlari --> check_word

#     Ex.1: word="applepieapple", word_list=["apple", "pie"]
#             check_word --> True
    
#     Ex.2: word = "catsandog", word_list = ["cats", "sand", "dog", "cat", "dogs"]
#             check_word --> False
# """


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


obj1 = CheckWord(word="applepieapple", word_list=["apple", "pie"])
# obj1 = CheckWord(word="catsandog", word_list=["cats", "sand", "dog", "cat", "dogs"])
print(obj1.check_word())



# """
# Task 1:

# Bir dene findList classi yaradacayiq. Bu class iki dene parametr (start, end) qebul edecek.
# Method: --> find_arrange_list ( + elave parametr --> even)
# if even=True, start ve end arasindaki cut ededleri liste qaytaracaq
# else start ve end arasindaki tek ededleri liste qaytaracaq
# """

# # class FindList:

# #     def __init__(self, start, end):
# #         self.start = start
# #         self.end = end
    
# #     # def find_arrange_list(self, even):
# #     #     result = []
# #     #     if even:
# #     #         for i in range(self.start,self.end+1):
# #     #             if i % 2 == 0:
# #     #                 result.append(i)
# #     #     else:
# #     #         for i in range(self.start, self.end+1):
# #     #             if i % 2 == 1:
# #     #                 result.append(i)
        
# #     #     return result

# #     def find_arrange_list(self, even):
# #         return [i for i in range(self.start, self.end+1) if i%2==0] if even else [i for i in range(self.start, self.end+1) if i%2==1]


# # obj1 = FindList(start=10, end=30)
# # print(obj1.find_arrange_list(even=False))



# # """

# # Task 2:

# # Bir dene calculateSideLength classi yaradiriq. Bu class iki parametr qebul edecek a ve b.
# # Burda mesele duzbucaqli ucbucagin hipotenizi hesablamaqdi. Pifaqor teorimi
# # c-nin kvadrati = a-nin kvadrati + b-nin kvadrati
# # Method: -> find_length
# # find_length methodu c-nin qiymetini qaytaracaq
# # """

# # class CalculateSideLength:

# #     def __init__(self, a, b):
# #         self.a = a
# #         self.b = b
    
# #     def find_length(self):
# #         c = self.a ** 2 + self.b ** 2
# #         return c**(0.5)


# # obj1 = CalculateSideLength(a=3, b=4)
# # print(obj1.find_length())

# # """
# # Task 3:

# # Bir dene Todo classi yaradin.
# # Attributelar --> Yoxdur
# # Methods --> todo_list, add_todo, remove_todo, complete_todo, uncomplete_todo

# #     * todo_list --> bu method butun todolarin siyahisini qaytaracaq
# #     * add_todo --> elave olaraq bir dene todo adinda parametr qebul edecek ve hemin todonu siyahiya elave edecek
# #     * remove_todo --> elave olaraq todonun nomresin goturecek ve hemin nomreye uygun todonu siyahidan silecek
# #     * complete_todo --> elave olaraq todonun nomresin goturecek ve hemin nomreye uygun todonu tamamlanmis edecek
# #     * uncomplete_todo --> elave olaraq todonun nomresin goturecek ve hemin nomreye uygun todonu tamamlanmamis
# #                             edecek

# # HINTS:

# #     todo_siyahi = {
# #         1: {
# #             "name": "Python Practice",
# #             "status": True,
# #         },
# #         2: {
# #             "name": "Python Homework",
# #             "status": False,
# #         },
# #         3: {
# #             "name": "Python Class",
# #             "status": False
# #         },
# #         4: {
# #             "name": "Python function",
# #             "status": False
# #         }
# #     }

# #     1. Python Practice --> True
# #     2. Python Homework --> False
# # """


# # class ToDo:

# #     todo_list = {}


# #     def add_todo(self, name):
# #         keys = list(self.todo_list.keys())
# #         keys.sort()
# #         number = keys[-1] + 1 if keys else 1

# #         self.todo_list[number] = {
# #             "name": name
# #             "status": False
# #         }
    

# #     def show_list(self):
# #         result = ''
# #         for key, data in self.todo_list.items():
# #             result += f"{key}. {data.get('name')} --> {data.get('status')}\n"
# #         return result
    
# #     def remove_todo(self, number):
# #         if number in self.todo_list.keys():
# #             del self.todo_list[number]
# #         else:
# #             return "Wrong number"
    
# #     def complete_todo(self, number):
# #         if number in self.todo_list.keys():
# #             self.todo_list[number]["status"] = True
# #         else:
# #             return "Wrong number"
    
# #     def uncomplete_todo(self, number):
# #         if number in self.todo_list.keys():
# #             self.todo_list[number]["status"] = False
# #         else:
# #             return "Wrong number"



# # obj1 = ToDo()

# print(obj1.todo_list)

# obj1.add_todo(name="Python Practice")

# obj1.add_todo(name="Python Lesson")

# print(obj1.show_list())

# obj1.remove_todo(2)

# print(obj1.show_list())


# obj1.complete_todo(1)

# print(obj1.show_list())

# obj1.uncomplete_todo(1)

# print(obj1.show_list())





"""
Task 3:

Bir dene Todo classi yaradin.
Attributelar --> Yoxdur
Methods --> todo_list, add_todo, remove_todo, complete_todo, uncomplete_todo

    * todo_list --> bu method butun todolarin siyahisini qaytaracaq
    * add_todo --> elave olaraq bir dene todo adinda parametr qebul edecek ve hemin todonu siyahiya elave edecek
    * remove_todo --> elave olaraq todonun nomresin goturecek ve hemin nomreye uygun todonu siyahidan silecek
    * complete_todo --> elave olaraq todonun nomresin goturecek ve hemin nomreye uygun todonu tamamlanmis edecek
    * uncomplete_todo --> elave olaraq todonun nomresin goturecek ve hemin nomreye uygun todonu tamamlanmamis
                            edecek

HINTS:

    todo_siyahi = {
        1: {
            "name": "Python Practice",
            "status": True,
        },
        2: {
            "name": "Python Homework",
            "status": False,
        },
        3: {
            "name": "Python Class",
            "status": False
        },
        4: {
            "name": "Python function",
            "status": False
        }
    }

    1. Python Practice --> True
    2. Python Homework --> False
"""



# class Todo:

#     todo_siyahi = {
#         1: {
#             "name": "Python Practice",
#             "status": True,
#         },
#         2: {
#             "name": "Python Homework",
#             "status": False,
#         },
#         3: {
#             "name": "Python Class",
#             "status": False
#         },
#         4: {
#             "name": "Python function",
#             "status": False
#         }
#     }


#     def todo_list(self):
#         result = ""
#         for key, data in self.todo_siyahi.items():
#             result += f"{key}. {data.get('name')} --> {data.get('status')}\n"
#         return result

#     def add_todo(self, name):
#         keys = list(self.todo_siyahi.keys())
#         keys.sort()
#         number = keys[-1] + 1 if keys else 1
        
#         self.todo_siyahi[number] = {
#             "name": name,
#             "status": False
#         }
    

#     def remove_todo(self, number):
#         if number in self.todo_siyahi.keys():
#             del self.todo_siyahi[number]
#         else:
#             return "Olmayan bir reqem yazmisiniz"

#     def complete_todo(self, number):
#         if number in self.todo_siyahi.keys():
#             self.todo_siyahi[number]["status"] = True
#         else:
#             return "Olmayan bir reqem yazmisiniz"
    
#     def uncomplete_todo(self, number):
#         if number in self.todo_siyahi.keys():
#             self.todo_siyahi[number]["status"] = False
#         else:
#             return "Olmayan bir reqem yazmisiniz"




# obj1 = Todo()

# print(obj1.todo_list())

# obj1.add_todo(name='Django Hello World')

# print(obj1.todo_list())