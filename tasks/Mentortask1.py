#1.	Userden ad, soyad ata adi alin, neticede ekrana yalniz bas herfleri boyuk cixsin.
#Input : meRDan balayev Etibar
#Output: Merdan Balayev Etibar

# name = input("my name:").capitalize()
# surname = input("my surname:").capitalize()
# fathname = input("father's name: ").capitalize()

# print(name,surname,fathname)

# #Indexlemeden istifade ederek ‘azərbaycan’ stringinden asagidaki sozleri ekrana yazdirin:
# #azər, zər,zərb, ar, can, naz, car, baybay, az-az
# st = "azərbaycan"
# # print(st[0:4])
# # print(st[1:4])
# # print(st[1:5])
# # print(st[0:4:3])
# # print(st[-3::1])
# # print(st[-1::-4])
# # print(st[-3:-8:-2])
# # print(st[4:7]*2)
# print(st[0:2], st[0:2],sep="-")

# #Asagidaki teksti kodu bir setr yazmaqla  herfleri kicildin,? Isaresini silin,python sozunu django ile evez edin
# text ="MEN PYTH?ON OYRENIREM"
# print(text.replace("?", "").replace("PYTHON","DJANGO").lower())

# Istifadeciden telebenin 3 semestr fenninden qiymetlerini alin ve onlarin ortalama balini ekrana cixaran kodu yazin.

sm1 = int(input("semestr 1: "))
sm2 = int(input("semestr 2: "))
sm3 = int(input("semestr 3: "))

a=[sm1,sm2,sm3]
print(sum(a)/len(a))

#5. Asagidaki stringde a herfinin sayinin diger butun herflerin sayinin nece faizi oldugunu hesablayan kodu yazin. 
# text ="atakama dunyanin en quru sehrasidir"

# onlya = text.count("a")
# space = text.count(" ")
# others = text.count("") - onlya - space

# percentage = (onlya*100)/others
# print(percentage)




# mylist = [20,40,50,100,80,30,60]

# mylist.sort()

# print(mylist[0])
# print(mylist[-1])


#1.	Userden ad, soyad ata adi alin, neticede ekrana yalniz bas herfleri boyuk cixsin.
# Input : meRDan balayev Etibar
# Output: Merdan Balayev Etibar

# name = input("my name:").capitalize()
# surname = input("my surname:").capitalize()
# fathname = input("father's name: ").capitalize()

print(input("name surname father's name : ").title())



