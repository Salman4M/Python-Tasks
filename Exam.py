# 1) Rəqəmlərdən ibarət bir list və bir target verilib. Əgər listdən hər hansısa iki ədədin cəmi targetə bərabərdisə həmin ədədlərin indekslərini list olaraq qaytarın.

# 	NOTE: Yazdığınız kod aşağıdakı 3 nümunəni qarşılamalıdı və classla yazılmalıdı əks halda qəbul olunmayacaq

# 	Ex.1: Input: nums = [2,7,11,15], target = 9 ---> Output: [ [0, 1] ]
# 	Ex.2: Input: nums = [3,2,4], target = 6 ---> Output: [ [1, 2] ]
# 	Ex.3: İnput: nums = [3,2,1,4,9,7,8,6,], target = 7 ---> Output: [ [0, 3], [2, 7] ]


# nums = [2,7,11,15]
# nums = [3,2,4]
# nums = [3,2,1,4,9,7,8,6]
# # target = 9
# # target= 6
# # target = 7

#DUZELTME
# class Solution:
#     def __init__(self,nums,target):
#         self.nums = nums
#         self.target = target
#     def find_two_sum(self):
#         d=[]
#         for ind,val in enumerate(nums) :
#             for j in range(ind+1, len(nums)):
#                 if val + nums[j] == target:
#                     d.append([ind,j])
#         return d 
    
# nums = [3,2,1,4,9,7,8,6]

# target = 7


# result = Solution(nums, target)
# print(result.find_two_sum())
                                                               




# 2) word və target deyə iki string var. Sizdən istənilən targetin wordun içində başladığı ilk indeksi qaytarmaqdır. Əgər target wordun içində yoxdursa onda -1 qaytarmalısız.
	
# 	NOTE: Yazdığınız kod aşağıdakı nümunələri qarşılamalıdı və classla yazılmalıdı əks halda qəbul olunmayacaq
	
# 	Ex.1: word = "qaçhaqaç", target="qaç" ---> Output: 0
# 	Ex.2: word = "coders", target="ders" ---> Output: 2
# 	Ex.3: word = "azərbaycan", target="azəri" ---> Output: -1

# word = "hacim"
# target="azəri"
# # a= []

# index =  word.find(target)

# print(index)

# print(a)

# word = "qachib"
# target = "ders"
# ind = word.find(target)
# print(ind)
# a = []

# for ind1, val1 in enumerate(word):
#     for ind2, val2 in enumerate(target):
#         if val2 in val1:
#             if len(a) < 1:
#                 a.append(ind1)
#                 break
#     else:
#         print(-1)
# print(a[0] if a else -1)



# 3) Bir string verilib. Sizdən istənilən sonuncu sözün uzunluğunu qaytarmaqdır.

# 	NOTE: Yazdığınız kod aşağıdakı 3 nümunəni qarşılamalıdı və classla yazılmalıdı əks halda qəbul olunmayacaq

# 	Ex.1: s = "Hello World" ---> 5 ("World"-un uzunluğu)
# 	Ex.2: s = "   fly me   to   the moon  " ---> 5 ("moon"-un uzunluğu)

# s = "Hello World"
# # s = "   fly me   to   the moon  "


# class Solution:
#     def __init__(self, s):
#         self.s = s
#     def check(self):
#         a = s.split(' ')
#         d = []
#         for i in range(len(a)-1,0,-1):
#             if a[i] == '':
#                 continue
#             else:
#                  d.append(a[i])
#         return len(d[0])

# s = "Hello World"


# myobj = Solution(s)

# print(myobj.check())


# 4) Bir text stringi var. Aşağıdakı şərtləri qarşılayan bir class yazın:
	
# 	* Bütün hərflər böyük olmalıdır
# 	* Bütün hərflər kiçik olmalıdır
# 	* Ancaq ilk element kiçik olmalıdır

# 	Əgər text stringi bu şərtlərdən hər hansısa birini qarşılayırsa onda class True qaytarmalıdır əks halda False


# class Solution:
#      def __init__(self, text):
#         self.text = text
#      def Rules(self):
#         if self.text.isupper() or  self.text.islower() or self.text[0].islower():
#            return True
#         else:
#             return False

# myobj = Solution("cord")

# print(myobj.Rules())



	
# 5) İki list verilib. Bu iki listin ortaq elementlərin indeksləri cəmini qaytaran bir class yazın:

# 	NOTE: Yazdığınız kod aşağıdakı nümunələri qarşılamalıdı və classla yazılmalıdı əks halda qəbul olunmayacaq
	
# 	Ex.1: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","Hungry Hunter Steakhouse","Shogun"] ---> Output: [0 + 2] = [2]
# 	Ex.2: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"] ---> Output: [0+1, 1+0, 2+2] = [1, 1, 4]

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","Hungry Hunter Steakhouse","Shogun"]

# list1 = ["happy","sad","good"]
# list2 = ["sad","happy","good"] 
# c = []

# for ind1, val1 in enumerate(list1):
#     for ind2, val2 in enumerate(list2):
#         if val1 == val2:
#             b = ind1+ind2
#             c.append(b)


# class Solution:
#     def __init__(self, list1,list2):
#         self.list1 = list1
#         self.list2 = list2
#     def InOrNot(self):
#         c = []
#         for ind1, val1 in enumerate(list1):
#             for ind2, val2 in enumerate(list2):
#                 if val1 == val2:
#                     b= ind1+ind2
#                     c.append(b)
#         return c
    
# # list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# # list2 = ["Piatti","Hungry Hunter Steakhouse","Shogun"]

# list1 = ["happy","sad","good"]
# list2 = ["sad","happy","good"]    
# myobj = Solution(list1,list2)

# print(myobj.InOrNot())


# 6) def myfunc(text):
# 	return text.upper()

# 	Yuxarıdakı funksiya üçün bir dekorator yazın hansıki texti sağ və sol boşluqlardan təmizləyəcək. Nümunə:
	
# 	text = "  Coders Girls " ---> decorator bu texti götürüb myfunc-un içinə "Coders Girls" kimi göndərməlidi


# def SpaceDeleter(func):

#     def Indent(text):
#         return text.strip()
        
#     return Indent

# @SpaceDeleter
# def myfunc(text):
#     return text.upper()

# func1 = myfunc("  Coders Girls ") 
# print(func1)

# 7) Userdən bir text stringi qəbul edin və bu textin içindəki elementləri təkrarlanmadan aşağıdakı nümunələrdəki kimi qaytarın

# 	Ex.1:  text = "Coders" ---> [("C", 0), ("o", 1), ("d", 2), ("e", 3), ("r", 4), ("s", 5)]
# 	Ex.2:  text = "Canavar" --> [("C", 0), ("a", 1), ("n", 2), ("v", 4), ("r", 6)]

# text = "Coders"
# text = "Canavar"
# d = []
# for ind, val in enumerate(text):
#     d.append((str(val),ind))

# print(d)

# 8) Bir list verilib. Aşağıdakı funksiyaları yerinə yetirən bir class yaradın.
	
# 	* Max-ı hesablasın
# 	* Min-i hesablasın
# 	* Ortalamanı hesablasın



# class Solution:
#     def __init__(self,list1,mymin,mymax):
#         self.list1 = list1
#         self.mymin = mymin
#         self.mymax = mymax
#     def MinMaxAv(self):
#         d = []
#         c = []
#         list1.sort()

#         val = 0
#         for ind1,val1 in enumerate(list1):
#             val +=val1 
#         return (val/len(list1)), self.mymin,self.mymax


# list1 = [2,7,4,8,3,1,9]
# mymin = list1[0]
# mymax = list1[-1]

# myobj = Solution(list1,mymin,mymax)
# print(myobj.MinMaxAv())


# list1.sort()

# mymin = list1[0]
# mymax = list1[-1]

# print(mymin)
# print(mymax)
# val = 0
# for ind,val1 in enumerate(list1):
#     val +=val1 
# print(val/len(list1))

# # for ind1,val1 in enumerate(list1):
# #     for ind2,val2 in enumerate(list1):
# #         if val1!=val2:
# #             if val1<val2:
# #                 break    

# # else:     
# #     d.append(val1)

# # print(d)

# for ind1,val1 in enumerate(list1):
#     for ind2,val2 in enumerate(list1):
#         if val1!=val2:
#             if val1>val2:
#                 print(val1)
#                 break   

# else:     
#     c.append(val2)

# print(c)



# 9) Userdən bir input istəyin (integer) və həmin inputa əsasən Fibonacci ardıcıllığını qaytaran bir funksiya yazın
	
	# * n = 5 -->  [0, 1, 1, 2, 3]
	# * n = 9 -->  [0, 1, 1, 2, 3, 5, 8, 13, 21]





# 10) Listin bütün ədədlərini cəmini hesablayan recursive funksiya yazın

# def mylist (list1):

#     sum = 0
#     for i in range(len(list1)):
#         sum+=list1[i]
#     return sum

# func1 = mylist([1,2,3,4,5,6,7,8])

# print(func1)

# def mylist(list1):
#     return list1 + mylist(len(list1)-1) if sum(list1) > 1 else 0

# # list1 = [1,2,3,4,5,6,7,8]
# # func1 = mylist(list1)

# # print(func1)

def recursive_sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + recursive_sum(nums[1:])

# Example usage
numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print(result)


# Initial call: recursive_sum([1, 2, 3, 4, 5])
# nums[0] is 1, and we make a recursive call: 1 + recursive_sum([2, 3, 4, 5])
# nums[0] is 2, and we make another recursive call: 2 + recursive_sum([3, 4, 5])
# nums[0] is 3, and we make another recursive call: 3 + recursive_sum([4, 5])
# nums[0] is 4, and we make another recursive call: 4 + recursive_sum([5])
# The base case is reached with len(nums) == 1, and we return the only element left: 5.
# The recursive calls resolve back: 4 + 5 = 9, 3 + 9 = 12, 2 + 12 = 14, 1 + 14 = 15.
# The final sum is 15.


# 11) User classı yaradın. Attributeları --> ["username", "email" (default olaraq None), "name"(default olaraq None), "surname" (default olaraq None), "password"]
# 			 Methodları --> ["check_password", "create_user", "make_password"]
	
# class Users:
#     def __init__(self,username,email,name,surname,password):
#         self.username = username
#         self.password = password
#         self.email = email
#         self.surname = surname
#         self.email = name
#     @staticmethod
#     def make_password(password):

#         return str(password)+"secretkey"
    
#     def check_password(self):
#         password = 'akfaskfksfas'
#         if password == self.password:
#             return True
#         else:
#             return False
#     @classmethod
#     def create_user(cls, username,name, surname, email ,make_password):
#         return cls(
#             name=name,
#             surname=surname,
#             username = username,
#             email = email,
#             make_password = make_password

#         )

# myobj = Users("smammadli", 'smammadli@hotmail.com', 'salman', 'mammadli', '1324432')
# print(myobj.create_user("smammadli", 'smammadli@hotmail.com', 'salman', 'mammadli', '1324432'))

# 	* make_password --> @staticmethod decorator ilə yazın. Bir password qəbul edəcək və bu passwordla "secretkey" stringini birləşdirib qaytaracaq
# 	* check_password --> funksiya olaraq bir password stringi götürəcək və bu passwordla User obyektinin içindəki passwordla müqayisə edəcək və True ya da False qaytaracaq
# 	* create_user --> @classmethod decorator ilə yazın. Username, email, name, surname və make_password methodunun qaytardığı password ilə user obyekti yaradıb qaytaracaq

# 12) results = {1: "Lionel Messi", 2: "Cristiano Ronaldo", 3: "Johan Cruyff", 4: "Marco van Basten", 5: "Michel Platini"}. Userdən bir input (yer) götürün və
#  həmin inputa əsasən nəticəni ekrana çap edən bir funksiya yazın. Əgər input results'ın içində yoxdusa "Axtardığınız rəqəmə uyğun nəticə yoxdur.
#  Yenidən yoxlayın..." yazısını ekrana çıxardın və prosesi yenidən başladın.

# results = {1: "Lionel Messi", 2: "Cristiano Ronaldo", 3: "Johan Cruyff", 4: "Marco van Basten", 5: "Michel Platini"}

# input_ = int(input("Get keyword: "))

# try:
#      print(results[input_])
# except:
#      print("Axtardiginiz reqeme uygun netice yoxdur , yeniden yoxlayin")



# 13) Aşağıdakı örnəyi koda çevirin
	
# 	* * * * *
# 	  * * * *
# 	    * * *
# 	      * *
# 		    *

# for i in range(5, 0, -1):

#     for k in range(5-i):
#         print(" ", end=" ")

#     for j in range(i):
#         print("*", end=" ")
    
#     print("")

# 14) Userdən bir input götürün (rəqəm) və bu inputun "palindrom" olub-olmadığını yoxlayın

# myn = (input("my number is: "))

# if myn ==myn[::-1]:
#     print("polindromdur")
# else:
#     print("deyil")



# 	Note: Palindrom ədədlər tərsi ilə özü eyni olanlardı. Məsələn 121, 545 və s. palindrom ədədlərdir


# 15) mydict = {"name": "Fuad", "surname": "Huseynov"}. Bu dictionarydəki key və valueların yerini dəyişib qaytaran funksiya yazın. Yəni nəticə belə olmalıdır
	
# 	Output:  {"Fuad": "name", "Huseynov": "surname"}
	
# mydict = {"name": "Fuad", "surname": "Huseynov"}
# mydict1 = {}
# # # mydict1 = {mydict['name']:,"Huseynov"mydict["surname"]}


# for ind, val in enumerate(mydict):
#     mydict1={mydict[val]:str(val)}

# print(mydict1)


#DUZELTME

# mydict = {"name": "Fuad", "surname": "Huseynov"}
# # mydict1 = {mydict['name']:,"Huseynov"mydict["surname"]}

# mydict1 = {}
# for ind, val in enumerate(mydict):
#     mydict1[mydict[val]]=val

# print(mydict1)

