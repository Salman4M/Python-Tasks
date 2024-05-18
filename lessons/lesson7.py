# for i in range(6):
#     for j in range(i):
#         print("*", end=" ")
    
#     print("")


# # for i in range(11):
# #     for j in range(i):
# #         print("*", end=" ")
    
# #     print("")



# # def prepare_star_figure():
# #     for i in range(6):
# #         for j in range(i):
# #             print("*", end=" ")
        
# #         print("")



# # print(prepare_star_figure())




# # def say_hello(name, surname, age):
# #     print(f"Hello {name} {surname} {age}")


# # func1 = say_hello('Fuad', 'Huseynov', 20)  #---> arguments
# # func1 = say_hello(name='Fuad', surname='Huseynov', age=20) #--> keyword arguments

# # print(func1)




# # def say_hello(name, surname, age):
# #     return f"Hello {name} {surname} {age}"



# # func1 = say_hello(name='Fuad', surname='Huseynov', age=20)
# # print(func1)




# # def calculate_perimetr(a, b):
# #     return a*b


# # func1 = calculate_perimetr(10, 20)
# # print(func1)



# # def example_func(*args, **kwargs):
# #     print(args)
# #     print(kwargs)



# # obj1 = example_func(name="hello", s="canavar",  course="coders")

# # print(obj1)




# *a, b, c = 10, 20, 30, 40, 50

# print(a)
# print(b)
# print(c)



def lower_text(text):
    return text.lower().strip()


def check_lower_word(text1, text2):
    return lower_text(text1) == lower_text(text2)


word1 = "Coders"
word2 = "coDeRs "

print(check_lower_word(word1, word2))





# """
# Tasks

# 1) s = "Coders Azerbaijan: Say 'Hello World!' "
# Output: codersazerbaijansayhelloworld

# Yuxaridaki neticeni almaq ucun funksiya yazin

# """
# def myfunct(word):
#     return word.lower().replace(" ","")

# def myword(mytext):
#     b=''
#     for i in myfunct(mytext):
#         if i.isalpha() == True:
#             b+=i
#     return b
     
# funct = myword("Coders Azerbaijan: Say 'Hello World!'")

# print(funct)



# '''2) Userden iki input (start, end) isteyin ve asagidaki sertleri qarsilayan bir funksiya yazin

#     * end startdan kicikdise funksiya -1 qaytarmalidir
#     * start ve end arasindaki ededlerin ededi ortasini qaytarmalidir

# '''
startnum = int(input("my start num: "))
endnum =int(input("my end num: "))

mylist=[]


def minus(startnum,endnum):
    if startnum >= endnum:
        return -1
    for i in range(startnum,endnum):
        mylist.append(i)
    
    
func=minus(startnum,endnum)
print(func)
def average(first,last):
    return sum(minus(first,last))/len(minus(first,last))

            
fucnt1 = average(startnum,endnum)
print(fucnt1)


       

 
# '''3) mydict = {"name": "Fuad", "surname": "Huseynov", "age": 23}
# Qeyd: Funksiya 3 parametr qebul etmelidir
# Output: Welcome to Coders Azerbaijan, Mr. Fuad Huseynov
#         Your age is 23

# Yuxaridaki neticeni almaq ucun funksiya yazin



# 4) mydb = [{'username': 'huseynovfuad', 'password': 'admin123'}, {'username': 'salman11', 'password': 'salman123'}]
# Userden iki input isteyin (username, password) ve asagidaki sertleri qarsilayan bir funksiya yazin (login)

#     * eger userin daxil etdiyi username ve password listde varsa onda "Sisteme xos geldiniz, {username}" cixarmalidir
#     * eger yoxdusa ekrana "Username ve ya password yalnisdir" cixarmalidir

    
# 5) Register
#     * password uzunlugu minimum 6 olmalidir
#     * password boyuk herfle baslamalidir
#     * icinde en azi bir reqem olmalidir
#     * username uzunlugu minimum 5 olmalidir
#     * username ancaq reqem ve herflerden ibaret olmalidir
# """''''''


# # Task1

# # s = "Coders Azerbaijan: Say 'Hello World!' "

# # def get_short_word(word):
# #     # result = ""
# #     # for i in word.lower():
# #     #     if i.isalnum():
# #     #         result += i
    
# #     # return result
# #     return "".join(i for i in word.lower() if i.isalnum())

# # print(get_short_word(s))



# # # Task2

# # start = 5
# # end = 10

# # def calculate_average(start, end):

# #     if start > end:
# #         return -1
# #     else:
# #         lst = [i for i in range(start, end+1)]
# #         print(lst)
# #         return sum(lst)/len(lst)


# # print(calculate_average(start, end))


# # # Task3
# # """
# # Output: Welcome to Coders Azerbaijan, Mr. Fuad Huseynov
# #         Your age is 23
# # """

# # mydict = {"name": "Fuad", "surname": "Huseynov", "age": 23}

# # def show_text(name, surname, age):
# #     return f"Welcome to Coders Azerbaijan, Mr. {name} {surname}\nYour age is {age}"


# # print(
# #     show_text(
# #         **mydict
# #     )
# # )



# # # Task 4

# # mydb = [{'username': 'huseynovfuad', 'password': 'admin123'}, {'username': 'salman11', 'password': 'salman123'}]

# # username = 'huseynovfuad'
# # password = 'admin123'

# # def login_func(username, password):
# #     for data in mydb:
# #         if data.get("username") == username and data.get("password") == password:
# #             return f"Sisteme xos geldiniz, {username}"
    
# #     return "Username ve ya password yalnisdir"


# # print(login_func(username, password))


# # # Task 5
# # """
# # 5) Register
# #     * password uzunlugu minimum 6 olmalidir
# #     * password boyuk herfle baslamalidir
# #     * icinde en azi bir reqem olmalidir
# #     * username uzunlugu minimum 5 olmalidir
# #     * username ancaq reqem ve herflerden ibaret olmalidir
# # """


# # username = "fhuseyn"
# # password = "Admin123"


# # def check_password(password):
# #     if len(password) < 6:
# #         return "password minimum uzunlugu 6 olmalidir"
    
# #     if not password[0].isupper():
# #         return "password boyuk herfle baslamalidir"
    
# #     check = [i for i in password if i.isdigit()]
# #     if len(check) == 0:
# #         return "Icinde en azi bir reqem olmalidir"
    
# #     return True

# # def check_username(username):
# #     if len(username) < 5:
# #         return "Minimum uzunlug 5 olmalidir"
    
# #     if not username.isalnum():
# #         return "Ancaq herf ve ya reqemlerden ibaret olsun"

# #     return True

# # def register_func(username, password):

# #     password_check = check_password(password)
# #     username_check = check_username(username)

# #     if password_check == True and username_check == True:
# #         mydb.append(
# #             {"username": username, "password": password}
# #         )
# #     else:
# #         return password_check, username_check 
    
# #     return "Sag salamat", "Celal bele istedi"


# # password_error, username_error = register_func(username, password)

# # print(password_error)
# # print(username_error)
# # print(mydb)


