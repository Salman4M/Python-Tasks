
# # Lists

# mylist = []
# mylist1 = ["admin", 1, 2]
# mylist2 = ["coders", 30, 60, [79.5, "azerbaycan"]]

# # print(type(mylist))


# # print(mylist2[0])
# # print(mylist2[3])
# # print(mylist2[3][1])


# # print(mylist2[:-1])
# # print(mylist2[-5:-3:1])


fruits = ["alma", "armud", "heyva", "nar"]

# # # List methods

# # # 1) Append methodu

# # fruits.append("alca")

# # # 2)  Insert method

# fruits.insert(0, "uzum")
# # fruits.insert(-4, "mandalin")

# print(fruits)

# # # 3) Toplamaq

# additional_vegetables = ["kartof", "pomidor", "sogan"]


# print(fruits + additional_vegetables)

# fruits += additional_vegetables
# print(fruits)

# # 4) Extend methodu

# a= [["baaa","caaa","daaa","eaaa","faaa"]]
# a= ["baaa","caaa","daaa","eaaa","faaa"]
# a=(('baa','caaa','daa'),)
# fruits.extend(a)
# fruits.append(a)

# fruits.extend(["kivi","pear"])



# fruits.extend("kivi")
# '''
# 'k','i','v','i'
# '''

# print(fruits)



# # list funksiyasi


# str1 = "Coders"

# print(list(str1))



# # remove methodu

# fruits.remove("alca")
# # fruits.remove("portagal")

# print(fruits)


# # del funksiya

# del fruits[-1]
# # del fruits[:3]
# # del fruits

# print(fruits)


# # pop methodu

# print(fruits)

# x = fruits.pop()
# x = fruits.pop(3)

# print(f"x: {x}, fruits: {fruits}")
# print(x)
# print(fruits)

# # len funksiyasi

# # print(len(fruits))


# # count methodu


# # print(fruits.count("alca"))



# print(fruits)


# # fruits[0] = "portagal"
# # fruits[0] = ["portagal", "kivi", "banan"]

# # fruits[1:4] = ["portagal", "kivi", "banan"]
# # fruits[1:4] = "portagal"

# # fruits[0:1] = ["portagal", "kivi", "banan"]

# # print(fruits)

# mylist3 = ["apple","kiwi","banana","heyva","nar"]

# mylist3[0] = ["portagal", "armud", "visne"]
# print(mylist3)
# mylist3[0:1] = ["portagal", "armud", "visne"]
# print(mylist3)
# mylist3[0:4] = ["portagal", "armud", "visne"]
# print(mylist3)
# mylist3[-4:-1] = ["portagal", "armud", "visne"]
# print(mylist3)


# # Tuples

#Note: In case your generating a tuple with a single element, make sure to add a comma after the element

#a tuple
# mytuple = ("Geeks",)
# print(type(mytuple))

# #NOT a tuple
# mytuple = ("Geeks")
# print(type(mytuple))

# Output:

# <class 'tuple'>
# <class 'str'>


# tuple1 = ()
tuple2 = ('alma', 'armud', 'heyva', 'portagal')
# # tuple3 = ('nar', )

# # print(type(tuple1))
# # print(type(tuple2))
# # print(type(tuple3))


# # print(tuple2[0])
# # print(tuple2[-1])
# # print(tuple2[:-1])


# tuple2[0] = "kivi"



# # len funksiyasi


# print(len(tuple2))






# print(tuple2)


# list2 = list(tuple2)
# list2.append('alca')

# print(list2)
# tuple2 = tuple(list2)

