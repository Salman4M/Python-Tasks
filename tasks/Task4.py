# 1) mydict = {"name": "Fuad", "surname": "Huseynov", "age": 23}. Aşağıdakı əməliyatları kod olaraq yazın
# 	* dictionarydəki key-ləri list olaraq ekrana çap edin
mydict = {"name":"Fuad", "surname":"Huseynov","age":23}
print(list(mydict.keys()))
# # 	* dictionarydəki value-ları list olaraq ekrana çap edin
print(list(mydict.values()))
# # 	* Userdən bir input (keyword) istəyin. Daha sonra həmin keyə uyğun value ekrana çap eləsin. Belə bir key olmadığı təqdirdə ekrana "Düzgün key daxil edin" yazısı çıxsın
keyword = input("my keyword is: ")

print(mydict.get(keyword,"Düzgün key daxil edin"))

# 2) dict1 = {1: [10, 45, 36, 78, 32], 2: [45, 67, 89, 27]}. Valuelardaki en boyuk ve en kicik ededi cap edin. (if olmadan)
#Output: En kicik: 10, En boyuk: 89
# dict1 = {1: [10, 45, 36, 78, 32], 2: [45, 67, 89, 27]}

# a = (dict1[1]+dict1[2])
# a.sort()
# print(a[0],a[-1])


# 3) dict1 = {"name": "Fuad", "students": {"student1": "Salman", "student2": "Mehemmed" } }. Burada 

# dict1 = {"name": "Fuad", "students": {"student1": "Salman", "student2": "Mehemmed" } }

# # # 	* studentlerin adlarini list olaraq ekrana cap edin.

# print(list(dict1["students"].values()))

# # # 	* Userden bir input (student_name) isteyin ve həmin keyə uyğun value ekrana çap eləsin. Belə bir key olmadığı təqdirdə ekrana "Düzgün key daxil edin" yazısı çıxsın

# student_name = input("student's key is: ")

# print(dict1["students"].get(student_name,"Düzgün key daxil edin"))