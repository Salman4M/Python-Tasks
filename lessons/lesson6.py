# If elif else


# number1 = int(input("Number1: "))
# number2 = int(input("Number2: "))


# if number2 > number1:
#     print("Salam")
# else:
#     print("Coders")


# if number1 > number2:
#     print(f"{number1} {number2}-den boyukdur")
# elif number1 < number2:
#     print(f"{number1} {number2}-den kicikdir")
# elif number1 <= number2:
#     print(f"{number1} {number2}-den kicik ve ya beraberdir")
# else:
#     print(f"{number1} {number2}-e beraberdir")



# if number1 > number2:

#     if number1 > 0 and number2 > 0:
#         print("Coders Azerbaijan")
    
#     else:
#         print("Menfi ededler")

# For loop


# for i in range(10, 3, -1):
#     print(i)


# 1ci element: 10
# 2-ci element: 9



# str1 = "Coders"
list1 = list("Samir")
# tuple1 = (10, 20, 30, 40)
# dict1 = {"name": "Fuad", "surname": "Huseynov"}



# for i in str1:
#     print(i)

# print(list1)

# for i in list1:
#     print(i)


# for i in tuple1:
#     print(i)


# for key, val in dict1.items():
#     print(key, val)


# print(list1)

# for i in list1:
#     for j in range(3):
#         print(i*j)


# i1 = S,
    # j1 = 0
    # j2 = 1
    # j3 = 2
# i2 = a
    # j1 = 0
    # j2 = 1
    # j3 = 2




# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
    
#     print("")



"""
* * * * *           * 
  * * * *         * *
    * * *       * * *
      * *     * * * *
        *   * * * * *
"""


# i1 = 1
    # j1 = 0 --> *

# i2 = 2
    # j1 = 0 --> *
    # j2 = 1 --> * *

# i3 = 3
    # j1 = 0 --> *
    # j2 = 1 --> * *
    # j3 = 2 --> * * *


# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end =" ")
#     for k in range(i):
#         print("*",end=" ")
#     print("")

for i in range(5, 0, -1):

    for k in range(5-i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")
    
    print("")


# i1 = 5
    # k1 = 0 --> ""

    # j --> * * * * *



# i2 = 4

    # k1 = 0 --> " "


    # j --> " " * * * *


# for i in range(5, 0, -1):

#     for k in range(i-1):
#         print(" ", end=" ")

#     for j in range(6-i):
#         print("*", end=" ")
    
#     print("")


# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
    
#     print("")


# for i in range(1, 6):
#     print("* "*i)


# mylist = []
# for i in range(10):

#     if i == 4:
#         continue
    
#     if i % 2 == 0:
#         # print(i, end=" ")
#         mylist.append(i)


# print(mylist)



# for i in range(5):
#     ...


# if True:
#     ...


# list3 = []

# number1 = 10

# while number1 > 0:
#     list3.append("Samir")
#     number1 -= 1


# print(len(list3))