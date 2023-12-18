# 1.İstifadəcinin daxil etdiyi ədədin təkmi cütmü olduğunu print etdirin. Əgər təkdirsə kvadratını, cütdürsə 5-ə bölünməsindən alınan qalığı print etdirin.

# num1 = int(input("user's number is: "))
# if num1 % 2 == 0:
#     print("even", num1*num1)
# else:
#     print("odd", num1 % 5)



# 2.Istifadiciden bir string alin ve bu stringi 20 defe print etdirin.

# st1 = input("my string is: ")
# for i in range(20):
#     print(st1)

# myword = input()
# i=0
# while i<=20:
#     print (myword)
#     i+=1
# 3. İstifadəçidən 3 ədəd alın və ən kiçiyini print etdirin.

# num1 = int(input("number1: "))
# num2 = int(input("number2: "))
# num3 = int(input("number3: "))

# if num3>num2>num1 or num2>num3>num1:
#     print(num1)
# elif num3>num1>num2 or num1>num3>num2:
#     print(num2)
# elif num1>num2>num3 or num2>num1>num3:
#     print(num3)
# else:
#     print("they are equal")

# 4.Tərəfləri daxil edilmiş üçbucağın növü müəyyənləşdirilməlidir. Bərabərtərəflidirsə ekrana 1, bərabəryanlıdırsa ekrana 2, müxtəliftərəflidirsə ekrana 3 yazılsın.

# side1 = input("sides are: ")

# a =side1.split(" ")


# x=int(side1[0])

# y=int(side1[2])

# z=int(side1[4])


# if x==y==z:
#     print("1")
# elif x == y != z or x == z !=y or z==y !=x:
#     print(2)
# else:
#     print(3)

# print(side1)
# print(a)

# Tək sətirdə boşluqla ayrılmış şəkildə 3 tərəf daxil edilir və nəticə ekrana yazdırılır.
# İnput: 3 4 3                                                  Output:2

# 5.Daxil edilen stringin palindrom olub=olmamasini yoxlayib print edin.
# Input				output
# Ata				polindromdur	
# fezail				polindrom deyil

# st = input("name: ")


# if st == st[::-1]:
#     print(" palindromdur")
# else:
#     print("palindrom deyil")

# 6. Istifadeciden email-ni daxil etmesini isteyin, eger email-i test@mail.com-a        
# beraberdirse,daha sonra password daxil etmesini isteyin, eger password test1234-e beraberdirse "Welcome to website!" mesaji ekrana yazdirin, 
# eger password dogru deyilse "Wrong password" mesaji ekrana yazdirin.Eger email dogru olmasa "Wrong email!" ekrana yazdirin.

# myemail = "test@mail.com"
# mypass = "test1234"
# usemail = input("my email: ")
# uspass = input("my password:")


# if myemail == usemail:
#     print(uspass)
#     if mypass==uspass:
#        print("Welcome to the website")
#     else:
#         print("wrong password")
  
# else:
#     print("wrong email")

  

    



# 7. Bir n ədədi daxil edilir və 0-dan bu ədəd qədər olan ədədlərin kvardatını print etdirin.
# İnput:
# 5
# Output:
# 0
# 1
# 4
# 9
# 16

# num3 =int(input("my number: "))
# for i in range(num3):
#         print(i**2)

# a, b, c = map(int, input().split("-"))

# if a == b == c:
#     print(1)
# elif a == b or b == c or c == a:
#     print(2)
# else:
#     print(3)