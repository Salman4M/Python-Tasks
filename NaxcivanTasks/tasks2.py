
# # 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

# def dividers(num):
#   if num<0:
#     return False
  
#   return (num**0.5)**2==num


# myfunc= filter(lambda x:dividers(x),mylist)
# # myfunc=list(map(dividers,mylist))

# print(list(myfunc))



# # 2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:

# # input:[1,2,3,4,8,2,2,4,5,6,7,7] output:[1,3,8]

# mylist=[-1,1,2,2,6,7,7,'say']

# def NonRepeat(value):
#     return mylist.count(value)==1


# test=filter(lambda x:NonRepeat(x),mylist)

# print(list(test))



# # # 3)Verilmiş inputdakı bütün rəqəmlərin hasilini icra edən funksiya yazın

# def Puncher(value):
#     a=1
#     for i in range(len(value)):
#         a*=value[i]
#     return a


# values=(input('seperate numbers by comma: ')).split(',')
# list_of_values=[int(number) for number in values]

# print(Puncher(list_of_values))

# # # 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək bir listə əlavə edin və print edin

# mynumb=40
# mylist=[i for i in range(2,mynumb) if mynumb%i==0]

# print(mylist)


# # 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

# # mənim listim
# # mylist=['may','iyun','iyul']
# # bu şəkildə olacaq
# # {'may': 3, 'iyun': 4, 'iyul': 4}

# mylist=['may','iyun','iyul']

# mydict={}

# def MonthLen(value):
#    mydict={i:len(i) for i in value}
#    return mydict

# print(MonthLen(mylist))

# # mydict={i:len(i) for i in mylist}
    
# # print(mydict)


# # 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"] 
# # verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin.


# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# results=[ i.split()[0].lower() for i in names]
# print(results)


# def Changer(value):
#     return value.split()[0].lower()

# bbbb=list(map(Changer,names))
# print(bbbb)




# # 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]


# def Average(value1,value2):
#    return value1+value2/2



# lister=list(map(lambda x,y:Average(x,y),nums1,nums2))
# print(lister)


