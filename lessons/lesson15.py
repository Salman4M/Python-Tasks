# """

# Dunder methods

# """


# from typing import Any


class Player:

    def __init__(self, name, age, position, price): # --> constructor
        self.name = name
        self.age = age
        self.position = position
        self.price = price
    

#     # def __del__(self):
#     #     print("__del__ file")

    def __str__(self):
        return f"{self.name} --> {self.price}"


#     def __repr__(self):
#         return f"Player({self.name}, {self.age}, {self.position}, {self.price})"
    
#     def __add__(self, other):
#         return self.price + other.price
    

#     def __gt__(self, other):

#         return self.price > other.price
    

#     # def __getattribute__(self, __name):
#     #     print(__name, "getattribute")

#     # def __getattr__(self, name):
#     #     print(name, "getattr")


#     # def __setattr__(self, __name, __value):
#     #     setattr(self, __name, __value)



# obj = Player('Fuad', 23, 'midfielder', 1000)
# obj1 = Player('Hormet', 23, 'midfielder', 1300)

# # a = obj.price
# # b = obj.discount

# # obj.price = 2000


# # print(obj.price, "akjshbdjkahbsdjkhas")
# print(obj)




# print(obj + obj1)


# print(obj > obj1) #--> __gt__
# # print(obj < obj1) #--> __lt__




"""
Task 1:
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

 

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 7
Output: false
"""


# class Solution(object):
#     def checkPerfectNumber(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         result = 0

#         for i in range(1, num):
#             if num % i == 0:
#                 result += i
        
#         return result == num
    

# obj = Solution()

# print(obj.checkPerfectNumber(28))


"""
Task 2
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

 

Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]
"""

# class Solution(object):
#     def selfDividingNumbers(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: List[int]
#         """
#         result = []
#         for elem in range(left, right+1):
#             check = True
#             for i in str(elem):
#                 if int(i) == 0:
#                     check = False
#                     break

#                 if elem % int(i) != 0:
#                     check = False
#                     break

#             if check: result.append(elem)
#         return result            


# obj = Solution()

# print(obj.selfDividingNumbers(47,85))



"""
Task 3
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
"""


# class Solution(object):
#     def addToArrayForm(self, num, k):
#         """
#         :type num: List[int]
#         :type k: int
#         :rtype: List[int]
#         """

#         # result = ""
#         # for i in num:
#         #     result += str(i)
#         result = str(int("".join(str(i) for i in num)) + k)
#         return [int(i) for i in result]


# obj = Solution()
# print(obj.addToArrayForm(num=[1,2,0,0], k=34))