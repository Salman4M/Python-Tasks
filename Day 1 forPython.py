# ##############################
# 	Day 1
# ##############################


# 1) listin icindeki ededlerin ortalamasini tapan bir funksiya yazin


# class SolutionAve:
#     def __init__(self,nums):
#         self.nums=nums
#     def AveNums(self):
#         return sum(nums)/len(nums)
    
# # nums = [1,2,3,4,5,6,7,8,9,10]

# # myobj = Solution(nums)
# # print(myobj.AveNums())


# # 2) listin icindeki ededlerin hasilini tapan bir funksiya yazin


# class SolutionMulti:
#     def __init__(self,nums):
#         self.nums=nums
#     def MultiNums(self):
#         n=1
#         for i in range(len(nums)):
#             n= nums[i]*n
#         return n
# # nums = [1,2,3,4,5,6,7,8,9,10]

# # myobj = Solution(nums)
# # print(myobj.MultiNums())

# # 3) listin icindeki ededlerin cemini tapan bir funksiya yazin

# class SolutionSum:
#     def __init__(self,nums):
#         self.nums=nums
#     def SumNums(self):
#         n=1
#         for i in range(len(nums)):
#             n= nums[i]+n
#         return n
# # nums = [1,2,3,4,5,6,7,8,9,10]

# # myobj = Solution(nums)
# # print(myobj.SumNums())


# # 4) listin icindeki ededlerin maximunu tapan bir funksiya yazin

# class SolutionMax:
#     def __init__(self,nums):
#         self.nums=nums
#     def MaxNums(self):
#         for ind1,val1 in enumerate(nums):
#             for ind2,val2 in enumerate(nums):
#                 if val1<val2:
#                     break
#         else:
#             return val1

# # nums = [1,2,3,4,5,6,7,8,9,10]

# # myobj = Solution(nums)
# # print(myobj.MaxNums())


# # 5) listin icindeki ededlerin minimunu tapan bir funksiya yazin

# class SolutionMin:
#     def __init__(self,nums):
#         self.nums=nums


#     def MinNums(self):
#         for ind1,val1 in enumerate(nums):
#             for ind2,val2 in enumerate(nums):
#                 if val1>val2:
#                     break
#         else:
#             return val2

# nums = [1,2,3,4,5,6,7,8,9,10]

# # myobj = Solution(nums)
# # print(myobj.MinNums())


# # 6) Bir Operation adinda class yaradin. bir list qebul edecek ve 
# # showResult methodunda yuxaridaki butun funksiyalarin neticelerini bir dict icinde qaytaracaq

# class Operation:
#     def __init__(self,mylist):
#         self.mylist = mylist
#     def showResult(self):
#         d = {
#             'Average': SolutionAve.AveNums(mylist),'Maximum':SolutionMax.MaxNums(mylist),
#             'Sum':SolutionSum.SumNums(mylist), 'Min':SolutionMin.MinNums(mylist),
#             'Multiply':SolutionMulti.MultiNums(mylist)
#         }
#         return d


# mylist = [1,2,3,4,5,6,7,8,9,10]
# myobj = Operation(mylist)


# print(myobj.showResult())
        
# db = [{"username": "fhuseyn", "password": "admin123"}, {"username": "admin", "password": "hello#admin123"}]

#   Register sistemi yaradin. Userden iki input isteyin (username, password). Daha sonra asagidaki sertlere gore yoxlamalar edin

# uslist = ['a']
# usdict = {'BBB':"ccc"}

# print(uslist+list(usdict))

# use = input("my username: ")
# psw = input("my password: ")
# d= []

# if len(use) > 8 and len(psw)>6:
#     if use[0].isupper():
#             if psw.isdigit() != True and psw.isalpha()!=True:
#                  d.append({"username":use, 'password':psw})
#             else:
#                 print("there are at least a number and a letter")
#     else:
#         print("First letter is not Upper")

# else:
#     print("not enough characthers")

# print(d)
# # 	* username uzunlugu 8den cox olmalidir
# 	* password uzunlugu 6dan cox olmalidir
# 	* password boyuk herfle baslamalidir
# 	* passwordun icinde en azi bir reqem ve bir herf olmalidir

# Eger yuxaridaki sertler qarsilanirsa db listine dict olaraq elave edin

# 2) Login sistemi yaradin. Userden iki input isteyin (username, password). Eger bu iki inputa esasen dict varsa
#  onda "Sisteme xos geldiniz yazisini gosterin". Eks halda "Username ve ya password yalnisdir"



# 3) Userden bir input isteyin (sentence). Cumle daxil edin. Daha sonra hemin cumledeki her bir sozu kicik ve
#  boyuk herflerin cemi ile evez edin


# db = [{"username":'salmanMammadli','password':'oebediguluslerin'},
#       {'username':'ElnurElnur','password':'italiano'},
#         {'username':'Maqa','password':'frizbi123'}]

# # print(db)

# use = input("my username: ")
# psw = input("my password: ")

# for ind,val in enumerate(db):
#      if val['username'] == use and val['password'] == psw:
#                print("Sisteme xos geldiniz")
#                break
    
# else:
#     print("Username ve ya Password yanlisdir")


# n = int(input('my number: '))
# q =0
# while n>1:
#       if n%2==0:
#             n = n//2
#       else:
#             n+=1
#       q+=1

# print(q)
        
        
            


# print(n)


# g1 = ['etirsah',' krokus', 'benovse'][0,1,2]
# g1 = ['benovse','etirsah','krokus'][2,0,1]

# g2 = ['krokus', 'benovse','etirsah'][1,2,0]
# g3 = ['etirsah','krokus','benovse'][0,1,2]


# k = int(input('nece gun: '))
# if k%4 == 1:
#         print("2ci gun")
# if k%4 == 2:
#         print("3cu gun")
# if k%4 == 3:
#         print('4cu gun')
# else:
#         print("5ci gun")


mywage = (input("my wages: "))

a = mywage.split(' ')
print(a)

b = []
for ind1,val1 in enumerate(a):
            for ind2, val2 in enumerate(a):
                if val1<val2:
                        break
else:
        b.append(int(float(val2)))

print(b)


