#69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
# c= []
# b = int(input("my number is: "))
# for i in range(0,b):
#     for j in range(0,b):
#         if i==j:
#             if i*j<=b:
#                 c.append(i)
# print(max(c))

# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# def fibonacci(n):

#     x = [1, 2]
#     while len(x) < n:
#         next_number = x[-1] + x[-2]
#         x.append(next_number)
#     return x

# ob=fibonacci(n=5)
# print(max(ob))


# 202. Happy Number


# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

# 2 = 2
# 3 = 3
# 4 = 5
# 5 = 8
# 6 = 13
# 7 = 21
# 8 = 34


# n = ['1','9']
# c = ['1']
# while len(n)> len(c):
#     for ind1,val1 in enumerate(n):
#         for ind2,val2 in enumerate(n):
#             if int(val1) != int(val2):
#                 n = int(val1)**2 + int(val2)**2
#                 if n!=1:
#                     n=n
#                 else:
#                     print(True)
#                     break



# 2706. Buy Two Chocolates

prices = [1,2,2]
mymoney = 4

prices.sort()


for ind1,val1 in enumerate(prices):
     for ind2,val2 in enumerate(prices):
          if ind1!=ind2:
               b = val1+val2
               if b <= mymoney:
                    print(mymoney-b)
                    break
else:
    print (mymoney)


# You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.

# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

# Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

 

# Example 1:

# Input: prices = [1,2,2], money = 3
# Output: 0
# Explanation: Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.
# Example 2:

# Input: prices = [3,2,3], money = 3
# Output: 3
# Explanation: You cannot buy 2 chocolates without going in debt, so we return 3.

