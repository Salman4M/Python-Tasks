# # Sets

# set1 = {12, 23, 45, 67}

# print(set1)
# print(type(set1))


# set2 = {}

# print(type(set2))


# set3 = {12, 1, 1, 3, 5, 8}

# # print(set3)



# list1 = [12, 34, 56, 78, 19, 12, 34, 12]

# print(list(set(list1)))



# Operator and methods


x1 = {"coders", "azerbaijan"}
x2 = {"coders", "caravan"}


# 1) Union

# print(x1 | x2) # --> union operator
# print(x1.union(x2)) # --> union method


# 2) Intersection


# print(x1 & x2)
# print(x1.intersection(x2))


# # 3) Difference

# print(x1 - x2)
# print(x1.difference(x2))


# # # 4) Symmetric difference

# print(x1 ^ x2)
# print(x1.symmetric_difference(x2))


# print((x1 | x2) - (x1 & x2))


# # 5) Issubset, Issuperset

x3 = {12, 34, 56, 78} 
x4 = {12, 34}
x5 = {12, 34, 56, 78}
x6 = {12, 34, 90}

# print(x3.issubset(x4))
# print(x4.issubset(x3))
# print(x3.issubset(x5))
# print(x6.issubset(x5))



# # print(x3.issuperset(x4))

# print(x3.issubset(x4) == x4.issuperset(x3))

# # # Operators


# print(x3 > x4)
# print(x3 > x6)

# print((x3>x4) and (x4.issubset(x3) and x3.issuperset(x4)))

# print(x3 >= x5)
# print(x3 > x5)


# # Modifying sets


# # 1) Union

# # x1 = x1 | x2

# # x1 |= x2
# # x1.update(x2)
# # print(x1)


# # 2) Intersection

# print(x1,x2)
# x1 &= x2
# x1.intersection_update(x2)
# print(x1)


# # 3) Difference
# print(x1,x2)
# x1 -= x2
# # # x1.difference_update(x2)
# print(x1)


# # # 4) Symmetric difference
# print(x1,x2)

# x1 ^= x2

# # # x1.symmetric_difference_update(x2)
# print(x1)



# # Set methods


myset = {'Fuad', 'coders', 'azerbaijan'}

# # # 1) Add methodu


myset.add('Samir')
# # # myset.add('Salman')
# print(myset)


# # 2) Remove

myset.remove('Samir')

# # myset.remove('Samir')

print(myset)


# # 3) Discard


# myset.discard('Samir')
# myset.discard('Samir')

# print(myset)


# # 4) Clear

# # myset.clear()


# # print(myset)


# # 5) pop
# print(myset)

# x = myset.pop()
# myset.pop()
# # myset.pop()

# print(myset)

# print(x)
