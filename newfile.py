# # triple double quotation mark and single quotation mark
# print("""Hi this is just for test""")
# print('''Hi this is ''just'' for test''')

# #if you want to you use double quotation mark in the string which is used double quotation mark have to use backslash before each double quotation mark
# print("Hi this is \"just\" for test")
# print('This is Salman\'s house')

# #end parameter: append new line after the last value if you use \n for end parameter
# # what if you don't use \n in the end parameter two  different values will be  will be in the one line
# print("Welcome to our course", end = "#")
# print("Some random words")

# print("Welcome to our course", end = "\n#")
# print("Some random words")
# #2 new lines
# print("Welcome to our house", end = "\n#\n")
# print("Some random words")

# #value before \n in the end parameter
# print("Just diving into deep" , end = "#\n")
# print("what's gonna happen")


# #sep parameter: leaves space or something you want between values
# print("Welcome to our course" ,"Hi this is me", sep = " SPACE ")
# print("Welcome to our course" ,"Hi this is me", sep = " \n ")

# print("Salam" , "Necesiz")

#Input 
# isupper
# islower
#endwith
#startwith

# Tasks

# print("My username is Salman.m")

# username = input("what is your name:")
# print(username.islower())
# print(username.isupper())
# print("My email is salmanmammadli@hotmail.com")
# email = input("what's your email adress:")
# print(email.find("@"))
# print(email.index("@"))


# sentence = "The quick brown fox jumps over the lazy dog"
# search = input("")
# print(sentence.count(search))


# name = input("my name is: ")

# print(name)


# surname = input("my surname is:")

# print(surname)


# print(name.strip())
# print(surname.strip())

# word = "Coders Caravan"

# print(word[0:6]) #Coders
# print(word[-7:]) # Caravan
# print(word[2:6]) #ders
# print(word[::-1]) # navaraC sredoC
# print(word[::2]) #Cdr aaa
# print(word[7::2]) #Crvn
# print(word[11::-2]) #

# password = input("My password is:")
# print(password[0].isnumeric())



# 3Example: word="Coders Caravan"; text1="Coders"; text2="Azerbaijan"
# 	 Output: Coders Azerbaijan

# word = input("my word is:")
# text1= input("text1 is ")
# text2 = input("text2 is ")

# print(word)
# print(text1)
# print(text2)

# print(word.replace(text1,text2))


# sentence = input(" ")
# print(sentence.title())


# password = input("is it:  ")
# print(password.isalnum())

# sentence = input("")
# x = sentence.lower()

# print(x.split())


# num1 = 20
# num2 = 30
# print(num1 > num2)
# print(num1 < num2)
# print(num1 == num2)
# print(num1 != num2)
# print(not num1 == num2)

# num3 = 30
# num4 = 30.0

# x = (str(id(num3)))
# print(len(x))

# y = (str(id(num4)))
# print(len(y))

# print (x == y)





# number1 = 853326577
# number2 = 934325932

# print(str(id(number1))[:4] == str(id(number2))[:4])


# a = id(num3)
# print(a[0:4])

# name1 = input("name1 is: ")
# name2 = input("name2 is: ")

# print((name1[0]==name2[0]) or name1[-1] == name2[-1] )
# print((len(name1)==len(name2) and (id(name1) >= id(name2)) or (name1==name2 and id(name1)==id(name2))))

# a,b = "Baku ", "is beatiful city"
# print(a)
# print(b)
# a += b

# print(a)



# p = 3.14
# cevre = int(input("radius"))
# b= (cevre * 2 * p  )
# print(b)

# cevre = input("radius:")

# a = float(cevre)

# b = (a*3.14*2)

# print(b)


# kvadrat = int(input("kvadrat terefi:"))
# s = (kvadrat*kvadrat)
# p = (kvadrat*4)

# print("sahesi:",s , "perimetri:",p)

# 

# mevacib = float(input("indiki mevacib:"))
# artim = mevacib*1.20

# print(artim)



# a = input("my final list: ")
# a1 = input()
# a2 = input()
# a3 = input()
# a4 = input()

# a.extend(a1,a2,a3,a4)

# mylist3 = ["akfk", 3, "etwet",44,"tiert", 29]
# mylist3.sort()

# print(mylist3)

# index_count = 0
# word = 'abcde'
# for letter in word:
#     print(word[index_count])
#     index_count+=1


# index_count = 0
# word = 'abcde'
# for letter in word:
#     print(letter[index_count])
#     index_count+=1


# a = "hi guys"
# b = "circumstance"
# c = "50"

# a = a.zfill(10)

# b= b.zfill(10)

# c= c.zfill(10)

# print(len(a))

# print(len(b))

# print(len(c))


# mylist = ["a","b","c","d","e"]

# index = mylist[1]
# index.pop()
# mylist.insert(1,"f")

# print(index)
# print(mylist)


# for i in range(1,6):
#     for k in range(5-i):
#         print(" ",end = " ")
#     for j in range(i):
#          print("*",end = " ")
#     print(" ")

# for i in range(1,6): 
#     print("*"*i, sep = "")

# age = int(input("your age: "))

# if age >= 18:
#     print("1000 manata xirdalandan ala bilersen")
# else:
#     print("hele vaxtiva var")

# for i in range(4,5):
#     for k in range(i):
#         for j in range(i):
#             print("*"*i)

# num1 = int(input("number1: "))
# num2 = int(input("number2: "))

# if num1 > num2:
#     print(num1)
# elif num1 < num2:
#     print(num2)
# else:
#     print("they are equal")

# num1 = int(input("number1: "))
# num2 = int(input("number2: "))
# num3 = int(input("number3: "))

# if num1>num2>num3 or num3>num2>num1 :
#     print(num2)
# elif num2>num1>num3 or num2<num1<num3:
#     print(num1)
# elif num2>num3>num1 or num2<num3<num1:
#     print(num3)
# else:
#     print("they are equal")

# if num1 >= num2 and num1 <= num3 and num1<=num2 and :
#     print(num1)
# elif num2 >=num1 and num2 <=num3:
#     print(num2)
# elif num3>=num1 and num3 <=num2:
#     print(num3)
# else:
#     print("beraberdir")
                
                


# elif num1 < num2:
#     print(num2)
# else:
#     print("they are equal")

# num1 = int(input("number1: "))
# num2 = int(input("number2: "))
# num3 = int(input("number3: "))

# if num1>=num2 or num2 >= num3:
#     print()
#     if num1


# def get_even(numbers):
#     return [num for num in numbers if not num % 2]


# get_even([1, 2, 3, 4, 5, 6])


# def mean(sample):
#     return sum(sample) / len(sample)


# print(mean([1, 2, 3, 4]))


# def add_one(x):
#     # No return statement at all
#     result = x + 1
#     return x+1

# value = add_one(5)
# value

# print(value)



# def prepare_star_figure():
#     for i in range(6):
#         for j in range(i):
#             print("*", end=" ")
        
#         print("")



# print(prepare_star_figure())

# # def prepare_star_figure(n):
# #     for i in range(n):
# #         for j in range(i):
# #             print("*", end=" ")
    
# #         print("")



# # print(prepare_star_figure(5))

# def prepare_star_figure(n):
#     for i in range(n):
#         for j in range(i):
#             print("*", end=" ")
        
#         print("")
# myfunct = prepare_star_figure(5)


# print(myfunct)

# def say_hello(name, surname, age):
#     print(f"Hello {name} {surname} {age}")


# func3 = say_hello(name='Fuad', surname='Huseynov', age=20) #--> keyword arguments
# print(func3)


# func1 = say_hello(name='Fuad', surname='Huseynov', age=20) #--> keyword arguments

# def say_hello(name, surname, age):
#     return f"Hello {name} {surname} {age}"


# func3 = say_hello(name='Fuad', surname='Huseynov', age=20) #--> keyword arguments
# print(func3)


# def example_func(*args):
#     print(args)
    

# obj1 = example_func(1,2,3,'girls')
# print(obj1)

# def example_func(**kwargs):
#     print(kwargs)
    

# obj1 = example_func(home = "baku", street = "kazimaga", year = '14')
# print(obj1)


# obj1 = example_func(name="hello", s="canavar",  course="coders")


# *a, b, c = 10, 20, 30, 40, 50
# print(a,b,c)
# a,* b, c = 10, 20, 30, 40, 50
# print(a,b,c)
# a, b, *c = 10, 20, 30, 40, 50
# print(a,b,c)

# a, b*,*c = 10, 20, 30, 40, 50

# def lower_text(text):
#     return text.lower().strip()


# def check_lower_word(text1, text2):
#     return lower_text(text1) == lower_text(text2)


# word1 = "Coders"
# word2 = "coDeRs "

# print(check_lower_word(word1, word2))


# # def low(text):
# #     return text.lower().strip()

# # def low_checker(text1,text2):
# #     return   low(text1) == low(text2)

# # word1 = "Coders"
# # word2 = "coDeRs"

# # print(low_checker(word1,word2))


# """
# Tasks

# 1) s = "Coders Azerbaijan: Say 'Hello World!' "
# Output: codersazerbaijansayhelloworld

# Yuxaridaki neticeni almaq ucun funksiya yazin

# def spaces(s):

#     return s.lower().split()

# def alphas(b):

#     for i in str(spaces(b)):
#         if i.isalpha()==True:
#             print(i, end = "")

# myfunct = alphas("Coders Azerbaijan: Say 'Hello World' ")
# print(myfunct)



# def pretify_string(func):
    
#         def capitalize_text(text):
#             return text.lower().capitalize()
        
#         return capitalize_text



# @pretify_string
# def say_hello(text):
#     return text


# myfunct = say_hello("sAlamlar Baku")

# print(myfunct)



# def pretify_string(func):
    
#         def capitalize_text(text):
#             if type(text)!=str:
#                  raise ValueError("Not string ")
#             return text.lower().capitalize()
        
#         return capitalize_text



# @pretify_string
# def say_hello(text):
#     return text


# myfunct = say_hello(7)

# print(myfunct)


# def pretify_string(func):
    
#         def capitalize_text(*args,**kwargs):
#             print(args)
#             print(kwargs)
#             text3 = kwargs.get("text3")
#             if type(text3)!=str:
#                  raise ValueError("Not string ")
#             return text3.lower().capitalize()

#         return capitalize_text



# @pretify_string
# def say_hello(text,text2,text3):
#     return text


# myfunct = say_hello(text = "see ya", text2 = "salam",text3 =  "Baku" )

# print(myfunct)



  # text = kwargs.get("text")
            # if type(text)!=str:
            #      raise ValueError("Not string ")
            # return text.lower().capitalize()




# def pretify_string(func):



#     def capitalize_text(*args, **kwargs):
#         print(args)
#         print(kwargs)


#         text = kwargs.get("text2")
#         if type(text) != str:
#             raise ValueError("Nagarsan  qadanalim")
#         return text.lower().capitalize()
#     # return func(*args, **kwargs)


#     return capitalize_text





# @pretify_string
# def say_hello(text, text2,text3,text4,text5):
#     return text


# func1 = say_hello(text="azerbaijan", text2="coders")


# print(func1)


# class checker():
 
#     def isin(self,ransomNote,magazine ):
#         self.ransomNote = ransomNote
#         self.magazine = magazine
#         for i in magazine:
#             if ransomNote.count() <= i.count():
#                 if ransomNote in i:
#                     print("True")
#             else:
#                 print("False")

# my_func = checker.isin("aa","aab")

# print(my_func)


# s= "abcde"
# d = "bcrde"

# for i in d:
#     for j in i:
#         if j != s:
#             print(, end = " ")
#         else:


# digits = [1,2,3]

# for i in digits:
#     print(i, end = "")



# nums = [3,2,3,5,2,2,2]
# n = 3
# mylist = []
# for i in nums:
#   if i == n:
#     print(mylist.append(i))
#     print(mylist)

#   if len(nums) / 2 > 3:
#     print(len(nums) / 2)
#   else:
#     print(mylist[0])



# nums = [1,2,3,1] 


# for i in range(0,6):
#     for j in nums:
#       if j.count(j[range]) > 1:
#         print(j.index(j)) 
#     print("")

# print(nums.count(nums[0]))




# nums = [0,1]
# mylist = []

# a = max(nums)  

# for i in range(0,a+1):
#     mylist.append(i)
#     if set(mylist) - set(nums) != set():
#       print(set(mylist) - set(nums))
#     else:
#        a+1


# print(mylist)

# class myClas:
#     def __init__(self, nums):
#       self.nums = nums

#     def myrange(self):
#        mylist = []
#        anotlist = []
#        for i in range(0,10):
#           mylist.append(i)
#        for j in self.nums:
#           anotlist.append(int(j)) 
#           d=set(mylist) - set(anotlist)
#           return d
 
# myobj = myClas("123456789")

# print(myobj.myrange())




# myyylist = [1,2,3,4,5,6,7,8,9]

# d = {"nums":"12345689"} 

# a = d.get("nums")
# b = set(list(a))
# print(type(a))
# print(list(a))
# print(a)
# print(b)

# c = []
# for i in b:
#     c.append(int(i))

# print(c)


# print(set(myyylist) - set(c))

        

# Task2 Nim Game


# class solution:
#    def canWinNim(self,n):
#       self.n = n
#    def removeEl(self):
#       mylist = ['o','o','o','o']
#       if mylist[0:self.n] 

# n =3
# mylist = ['o','o','o','o']

# if n > 1:
# mylist[0,n+1]   

# print(mylist == mylist.clear())
# mylist[0:5] = []

# print(mylist)
# print(len(mylist))


#Task 2 
# n = int(input("my number: "))
# mylist = []
# for i in range(2,n+1):
#    if n%i == 0:
#        print((mylist.append(int(n/i))))
#    else:
#       continue

# if sum(mylist[::]) == n:
#    print(True)
# else:
#    print(False)


# class Checker:
#    def __init__(self, n):
#       self.n = n
#    def checking(self):
#       result = 0
#       for i in range(1,n):
#           if n%i==0:


# a = int(input("my number a  is: "))
# b = int(input("my number b is: "))
# for i in range(a,b+1):
#    if i % (a//10) == 0  and i % (a%10) ==0:
#       print(i) 

# b = 45
# print(47//10)
# print(47%10)
      


# mylist = [1,2,0,0]
# k = 34

# mylist2 = []

# for i in mylist:
#    mylist2.append(str(i))


# print(mylist2)

# mylist3 = [] 
# for j in mylist2:
#    mylist3.append(int(i) + k)

# print(mylist3)
   

# print(list((str(k))))


# str(mylist[0])

# print(mylist)

mylist = []


# # for i in range(-10,11,1):
# #     mylist.append(i)
# #     if len(mylist)==5:
# #         print(mylist)


# # and sum(mylist[::]) == 0:

# import random

# b= random.randint(-10,10)

# mylist.append(b)
# print(mylist)
# for i in mylist:
#     print(i.append(random.randint(-10,10)))
#     if len(mylist)==5:
#         print(mylist)
    


# cr =  [[1,2],[2,3],[4,4],[4,5],[5,6],[6,7]]

# d= len(cr)

# # for i in range(0,d):
# #    if (cr[i+1]) < cr[d-1]:
# #       if sum(cr[i+1]) - sum(cr[i]) == 2:
# #          print(True)
# #       else:
# #          print("not a straight line")
# #          break
# #    else:
# #       break


# for i in range(len(cr)-1):
#    if sum(cr[i+1]) - sum(cr[i]) == 2:
#          print(True)
#    else:
#          print("not a straight line")
         
  
# # class solution:
# #    def __init__(self, cr):
# #       self.cr = cr
# #    def check(self):
# #       for i,item in enumerate(self.cr):
# #          if sum(self.cr[i+1]) - sum(self.cr[i]) == 2:
# #           return True
# #          else:
# #           return "Not a straight line"


# # cr = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

# # obj = solution(cr)

# # print(obj.check())



# class Solution:
#     def __init__(self, cr):
#         self.cr = cr

#     def check(self):
#         for i in range(len(self.cr)-1):
#             if sum(self.cr[i+1]) - sum(self.cr[i]) == 2 or sum(self.cr[i+1]) - sum(self.cr[i])==4 or sum(self.cr[i+1]) - sum(self.cr[i]) == 6 or sum(self.cr[i+1]) - sum(self.cr[i]) == 8 :
#                 return True
#             else:
#                 return "not a straight line"

# cr = [[1,5],[5,9]]
# obj = Solution(cr)

# print(obj.check())




# myj = [[1,5],[5,9]]


# if sum(cr[i+1]) - sum(cr[i]) == 2:
# n =  0
# # for i in coordinates:
# #     if sum(i[n+1])-sum(i[n]) == 2:
# #         print(True)
        
# # print(sum(coordinates[0]))

# for i in range(n):
#     print(sum(coordinates[n+1]))
#     n+=1


# print(sum(coordinates[n+1])-sum(coordinates[n]))

# tup = ([2,3])
# print(sum(tup))



# mynum = 3456345
# mydict = {}
# for i in str(mynum):
#     if str(i) == str(i[0]):

#       mydict[i] = [i.count(i)]


# print(mydict)



# b='3'
# d = ''
# for i in range(1,100):
#     d+=str(i)

# print(d)
# # print(d.count('3'))




# #Task Move Zeroes


# # mynums = [0,1,0,3,12]

# # mynums2 = [0,0,0,5,6,3,0,2,8,0,9,9]

# # for i in mynums2:
# #     if i == 0:
# #         mynums2.remove(i)
# #         mynums2.append(i)


# # print(mynums2)

# # class zeroes:
    
# #     def __init__(self,nums):
# #         self.nums = nums
    
# #     def randa(self):
# #         mylist0= []
# #         for i in self.nums:
# #             if i == 0:
# #                 mylist0.append(i)
# #         for zero in mylist0:
# #             self.nums.remove(zero)
# #             self.nums.append(zero)
# #         return self.nums


# # nums = [0,1,0,3,12]
# # nums = [0,0,0,5,6,3,0,2,8,0,9,9]

# # myobj = zeroes(nums)

# # print(myobj.randa())



# #Task 3Sum  Closest


# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result = []
 
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         data = [nums[i], nums[j], nums[k]]
 
#                         check = True
#                         for d in result:
#                             if sorted(d) == sorted(data):
#                                 check = False
#                                 break
 
#                         if check: result.append(data)        
#         return result
 
 
 
# obj = Solution()
# print(obj.threeSum([-1,0,1,2,-1,-4]))

# numser = [-1,2,1,-4]
# target = 2
# rlist = []
# for i in range (len(numser)):
#     for j in range(i+1,len(numser)):
#         for k in range(j+1,len(numser)):
#             rlist.append(numser[i]+numser[j]+numser[k])
# print(rlist)

# rlist.append(list(target))
# print(rlist)

# rlist.find(target-1) - rlist.find(target+1) 
        

# target = 2

# a= (-1+2+1)
# b= (-1+2-4)
# c= ( 2+1-4)
# d= (-1+1-4)


# alist= []
# blist= []
# clist= []
# dlist= []
# rlist =[]
# alist.append(a)
# blist.append(b)
# clist.append(c)
# dlist.append(d)

# rlist = alist+blist+clist+dlist

# rlist.sort()

# # print(rlist)

# # rlist.append(target)

# for i in range (rlist.index(target)-1, rlist.index(target)+1):
#     print(rlist)

# list1=[]
# list2=[]
# arr1 = [2,3,1,3,2,4,6,7,9,2,19]
# arr2 = [2,1,4,3,9,6]
# Output = [2,2,2,1,4,3,3,9,6,7,19]

# for i in arr2:
#     for j in arr1:
#         if i==j:
#             list1.append(j)


# for k in arr1:
#     if not k in arr2:
#         list2.append(k)


# print(list1+list2)


# nums = [3,1,6,5]
# target = 6

# indlist = []

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#       if nums[i]+nums[j] == target:
#          indlist.append(i)
#          indlist.append(j)
# print((indlist))

# n= int(input("my number is: "))
# if  n %2 !=0:
#     print("Weird")
# elif n%2==0:
#     if 2<=n<=5:
#         print("Not Weird")
#     elif 6<=n<=20:
#         print("Weird")
#     elif n>20:
#         print("Not Weird")

# def is_leap(year):
#     leap = False
    
#     if year % 4 == 0 and year %400 == 0:
#         leap = True
#     else:
#         leap
    
#     return leap

# year = int(input())
# print(is_leap(year))


# 7. Reverse Integer
# Medium
# 10.9K
# 12.3K
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit
#  integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# class Solution:
#         def __innit__(self,c):
#                 self.c = c 
#         def reverse(self):
#             for ind,val in enumerate(str(c)):
#                     if val == '-':
#                         val.replace('-','')
#                         val+'-'
        
#                 elif d[-1] == str(0) and  not'-' in d:
#                     d.remove('0')

#                 elif d[-1]!=0 and '-' in d:
#                     d.remove('-')
#                     d.append('-')
#             return d[::-1]



# c = -102
# c= str(c)
# d = 0
# d= str(d)
# if c[-1]=='0':
#       c=c.replace('0','')
# if '-' in c:
#         c=c.replace('-','')
#         if c[-1] == 0:
#             c = c.remove((0))
#             d = '-'+ c
#         else:
#               d='-'+ c
# elif not '-' in c:
#       d=c 
# print(d[::-1])

# if not '-' in c:
        


# myobj = Solution()

# print(myobj.reverse())



a1 = [1,2,3] #-->4
a2 = [1,2,3,5] #-->4
a3 = [-1,-3,-7] #-->1

# d = []
# c = []
# e = []
# for ind, val in enumerate(a2):
#     if val>0:
#         for i in range(min(a2),max(a2)+1):
#                 d.append(i)
#                 c.append(val)
#                 e = set(d)-set(c)
#         if len(e)==1:
#             print(e)
#         elif len(e)==0:
#             b=val+1
#     else:
#          print(1)
#          break
         

# class Examples:
#     def __init__(self, ab):
#         self.ab = ab

#     def Solution(self):
#         d = []
#         c = []
#         e = []
#         for ind, val in enumerate(self.ab):
#             if val > 0:
#                 for i in range(min(self.ab), max(self.ab) + 1):
#                     d.append(i)
#                 c.append(val)
#                 e = set(d) - set(c)
#                 if len(e) == 1:
#                     return e
#                 elif len(e) == 0:
#                     return val + 1
#             else:
#                 return 1


# ab = [1,2,3] #-->4
# # ab = [1,2,3,5] #-->4
# # ab = [-1,-3,-7] #-->1

     
# myobj = Examples(ab)
# print(myobj.Solution()) 








# if a3<=0
# for i in range (len(a1)-1):
#     for val,ind in enumerate(a1):
#         if i not in val:
#             print(i)





#rock paper scissors


# class Solution:
#     def RPS(self,inp1,inp2):
                
#         a = "rock"
#         b= "paper"
#         c = "scissors"

#         point1=0
#         point2=0

#         inp1 = input("your choice: ").strip()
#         inp2 = input("opponent choice: ").strip()

#         if a==inp1:
#             if inp2==b:
#                 point2+=1
#             elif inp2==c:
#                 point1+=1

#         elif b==inp1:
#             if inp2==a:
#                 point1+=1
#             elif inp2==c:
#                 point2+=1

#         elif c==inp1:
#             if inp2==a:
#                 point2+=1
#             elif inp2==b:
#                 point1+=1

        # if point1<1 or point2<1:

# a = "rock"
# b= "paper"
# c = "scissors"

# point1=0
# point2=0

# inp1 = input("your choice: ").strip()
# inp2 = input("opponent choice: ").strip()

# if a==inp1:
#     if inp2==b:
#         point2+=1
#     elif inp2==c:
#         point1+=1

# elif b==inp1:
#     if inp2==a:
#         point1+=1
#     elif inp2==c:
#         point2+=1

# elif c==inp1:
#     if inp2==a:
#         point2+=1
#     elif inp2==b:
#         point1+=1

# print(point1,point2)

# if point1!=2 or point2!=2:
#     inp1 = input("your choice: ").strip()
#     inp2 = input("opponent choice: ").strip()
#     if a==inp1:
#         if inp2==b:
#             point2+=1
#         elif inp2==c:
#             point1+=1

#     elif b==inp1:
#         if inp2==a:
#             point1+=1
#         elif inp2==c:
#             point2+=1

#     elif c==inp1:
#         if inp2==a:
#             point2+=1
#         elif inp2==b:
#             point1+=1

# print(point1,point2)


# if point1!=2 or point2!=2:
#     inp1 = input("your choice: ").strip()
#     inp2 = input("opponent choice: ").strip()
#     if a==inp1:
#         if inp2==b:
#             point2+=1
#         elif inp2==c:
#             point1+=1

#     elif b==inp1:
#         if inp2==a:
#             point1+=1
#         elif inp2==c:
#             point2+=1

#     elif c==inp1:
#         if inp2==a:
#             point2+=1
#         elif inp2==b:
#             point1+=1

# print(point1,point2)





# import the time module 
# import time 

# # define the countdown func. 
# def countdown(t): 
	
# 	while t: 
# 		days,remainder1 = divmod(t,86400)
# 		hours,remainder = divmod(remainder1, 3600) 
# 		mins,secs = divmod(remainder,60)
# 		timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days,hours,mins, secs) 
# 		print(timer, end="\r") 
# 		time.sleep(1) 
# 		t -= 1
	
# 	print('Fire in the hole!!') 


# # input time in seconds 
# t = input("Enter the time in seconds: ") 

# # function call 
# countdown(int(t)) 

# from bs4 import BeautifulSoup

# with open('filename.html', 'r') as html_file:
#     content = html_file.read()

# 	soup = BeautifulSoup(content,'lxml')