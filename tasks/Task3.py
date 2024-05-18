# # 1) Bir boş list yaradın. Daha sonra userdən iki input (name, surname) götürün və həmin inputları listin içinə əlavə edin
# mylist =[]
# name = input("name:")
# username = input("username:")
# mylist.insert(0,name)
# mylist.append(username)
# print(mylist)

# # 2) Bir list yaradın (içində ən azı 5 element olsun).Daha sonra userdən bir input (index) götürün və həmin inputa uyğun indeksdəki elementi listdən çıxarıb ekrana çap edin
# # (2 müxtəlif yolla) 

# mylist2 = ["a","b","c","d","e","f"]

# # willremove = int(input("removed index of  element:"))

# # print(mylist2.pop(willremove))

# willremove2 = int(input("removed index of element:"))

# del mylist2[willremove2]

# print(mylist2[willremove2])


# # 3) Bir list yaradın (içində ən azı 2 element (meyvə, terevez falan) olsun).
# #  Daha sonra userdən bir input (meyvə, terevez falan) götürün və həmin inputu listin içinə ən başına əlavə edin (2 müxtəlif yolla)

# mylist3 = ["apple","kiwi","banana","heyva","nar"]

# vegfr = input("vegs and fruits that will be added:")

# mylist3.insert(0,vegfr)
# print(mylist3)

# mylist3 =[vegfr] + mylist3
# print(mylist3)

# # 4) Bir list yaradın (içində ən azı 10 element olsun). Daha sonra userdən iki input (start, end) götürün və bu inputlar aralığındakı (start:end) elementləri silin
# ml=["ab","bc","cd","de","ef","fg","gh","hj","jk","kl","lm"]
# start = int(input("start:"))
# end = int(input("end:"))
# del ml[start:end]

# print(ml)

# # 5) Bir boş tuple yaradın. Daha sonra userdən iki input (name, surname) götürün və həmin inputları tuple içinə əlavə edin
# mytup = ()

# name = input("my name:")
# surname =input("my surname:")
# mytup=mytup+(name,surname)

# print(mytup)

# # 6) Bir tuple yaradın (içində ən azı 10 element olsun). Daha sonra userdən iki input (start, end) götürün və bu inputlar aralığındakı (start:end) elementləri silin
# tpl=("ab","bc","cd","de","ef","fg","gh","hj","jk","kl","lm")

# start = int(input("start index: "))
# end = int(input("end index: "))

# a = list(tpl)
# del a[start:end]

# print(tuple(a))

# 7) Bir list yaradın (içində ən azı 10 element olsun). Daha sonra userdən iki input (index, value) götürün və daha sonra həmin indeksdəki elementi value ilə əvəz edin
# al=["ab","bc","cd","de","ef","fg","gh","hj","jk","kl","lm"]

# index = int(input("my index: "))
# value = input("my value: ")
# al.pop(index)
# al.insert(index,value)
# print(al)

# # 8) Bir list yaradın (içində ən azı 10 element olsun).
# # Daha sonra userdən üç input (start, end) götürün və daha sonra bu inputlar aralığındakı (start:end) elementləri ["I", "am", "developer", "of", "future"] ilə əvəz edin
# ql=["ab","bc","cd","de","ef","fg","gh","hj","jk","kl","lm"]

# start = int(input("start:"))
# end = int(input("end: "))

# ql[start:end]=["I", "am", "developer", "of", "future"]

# print(ql)

# 9) Bir list yaradın (içində ən azı 5 element olsun).Daha sonra userdən bir input (value) götürün və həmin inputa uyğun elementi listdən çıxarıb ekrana çap edin
list6 = ["a","b","c","d","e","f"]
value = input("my value: ")
list6.remove(value)

print(value)
print(list6)




