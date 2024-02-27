# List methods


list1 = [10, 20, 30, 40, 50]


# list1.reverse()
# list1 = list1[::-1]

# print(list1)


# list2 = [10, 3, 56, 78, 23, 19]


# list2.sort()

# print(list2)



# Tuple operations


# tuple1 = (10, 20, 30)
# tuple2 = (40, 50, 60)

# print(tuple1 + tuple2)



# Dictionaries

dict1 = {
    "Fuad": "7y78ty7867876", # --> ("Fuad", "7y78ty7867876")
    "Salman": "278934892374982",# --> ("Fuad", "7y78ty7867876")
    "Mehemmed": "23467872334678",# --> ("Fuad", "7y78ty7867876")
    "Samir": ["2364t23784", "278364823467"]# --> ("Samir", ["2364t23784", "278364823467"])
}

# dict1['Xanim']= ['something new']

# print(dict1)

# print(dict1["Fuad"])
# print(dict1["Samir"][1])


# dict2 = {
#     10: "salam",
#     50.6: 89,
#     (10, 20, 30): "coders"
# }


# print(dict2[10])
# print(dict2[50.6])
# print(dict2[(10, 20, 30)])



# print(f"Before: {dict1}")


# dict1["Fuad"] = ["994xxxxxxxx", "7y78ty7867876"]


# print(f"After: {dict1}")


# del dict1["Fuad"]

# print(f"After: {dict1}")




# Dictionary methods


# 1) Len method


# print(len(dict1))


# 2) Keys, values, items

# print(list(dict1.keys()))
# print(list(dict1.values()))
# print(list(dict1.items()))


# 3) Get method


# print(dict1["Fuad"])
# print(dict1["Namiq"])


# value1 = dict1.get("Fuad")
# print(value1)



##if there are two keys inside of get method it will return  value of first key
# value2 = dict1.get("Fuad", "Salman")
# print(value2)





# # 3) update method

# if the key that you set is not in the dictionary it'll added to end of dict as a new value and key
# # dict1["Fuad"] = "994xxxxxxxx"
# dict1["Celal"] = "2348923478923874" 

# print(dict1)



# dict1.update({"Fuad": "coders", "Celal": "128734678234678"})

# print(dict1)
# print(len(dict1))




# dict3 = {"number1": 20, "number2": 10}
# dict4 = {"number3": 70.8}


# # print(dict3.get("number1") + dict3.get("number2"))

# dict3.update(dict4)

# print(dict3)

