# def helper(x, y):
#     return x + y

# func1 = helper(10, 20)
# func1 = helper(x=10, y=20)


# print(func1)

# Recursive functions


# def calc_for_range(n):
#     sum = 0
#     for i in range(n+1):
#         sum += i
    
#     return sum


# func1 = calc_for_range(5)
# print(func1)





def calc_for_range(n):
    return n + calc_for_range(n-1) if n > 1 else 0


func1 = calc_for_range(4)

print(func1)

# Input: n=5

# 1-ci calc_for_range(5) --> 5 + calc_for_range(4) --> 5 + 10 --> 15
# 2-ci calc_for_range(4) --> 4 + calc_for_range(3) --> 4 + 6 --> 10
# 2-ci calc_for_range(3) --> 3 + calc_for_range(2) --> 3 + 3 --> 6
# 2-ci calc_for_range(2) --> 2 + calc_for_range(1) --> 2 + 1 --> 3
# 2-ci calc_for_range(1) --> 1 + calc_for_range(0) --> 1 + 0 ---> 1
# 2-ci calc_for_range(0) --> 0





# def pretify_string(func):


#     def capitalize_text(*args, **kwargs):
#         print(args)
#         print(kwargs)


#         text = kwargs.get("text")
#         if type(text) != str:
#             raise ValueError("Nagarsan  qadanalim")
#         return text.lower().capitalize()
#         # return func(*args, **kwargs)


#     return capitalize_text





# @pretify_string
# def say_hello(text, text2):
#     return text


# func1 = say_hello(text="azerbaijan", text2="coders")


# # print(func1)







# def check_value_type(func):
#     print(f"func: {func}")

#     def inner(*args, **kwargs):
#         type_list = list(set([type(i) for i in args]))
#         type_list += list(set([type(i) for i in kwargs.values()]))
        
#         if not set(type_list) <= {int, float}:
#             raise ValueError("NOTE: Must be integer or float data type")
#         return func(100, 100)
    
#     return inner



# @check_value_type
# def sum_operation(x, y):
#     return x + y



# @check_value_type
# def minus_operation(x, y):
#     return x - y

# func1 = check_value_type(sum_operation)(x=10, y=5)
# func1 = sum_operation(x=10, y=5)
# print(func1)


# func1 = minus_operation(x=10, y=5)
# print(func1)

# 1-ci --> pretify_string ---> capitalize_text()


# 1, 1, 2, 3, 5, 8, 13, ...


# n=7


# def fibonacci_list(n):

#     def recur_fibo(n):
#         if n <= 1:
#             return n
#         else:
#             return(recur_fibo(n-1) + recur_fibo(n-2))
    
#     mylist = []
#     for i in range(1,n+1):
#         print(i, recur_fibo(i))
#         mylist.append(recur_fibo(i))
    
#     return mylist

    

# func1 = fibonacci_list(7)
# print(func1)




# 1-ci == 1 --> [1]
# 2-ci == 2 --> [1, 1]
    # --> recurfibo(1) + recurfibo(0) --> 1 + 0 --> 1

# 3-cu == 3 --> [1, 1, 2]
    # --> recurfibo(2) + recurfibo(1) --> 1 + 1 --> 2


# 4-cu == 4 --> [1, 1, 2, 3]
    # --> recurfibo(3) + recurfibo(2) --> 2 + 1  --> 3


# 5-ci == 5 --> [1, 1, 2, 3, 5]
    # --> recurfibo(4) + recurfibo(3) --> 3 + 2 --> 5


