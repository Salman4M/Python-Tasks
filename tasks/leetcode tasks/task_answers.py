# """
# Task 1
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"
# """


# # class Solution:


# #     def prepare_num(self, num):
# #         num_list = [int(i) for i in num]
# #         num_list.reverse()
# #         new_num = 0
# #         for index, elem in enumerate(num_list):
# #             new_num += elem * (10 ** index)
# #         return new_num

# #     def addStrings(self, num1, num2):
# #         num1 = self.prepare_num(num1)
# #         num2 = self.prepare_num(num2)        
# #         result = num1 + num2
# #         return str(result)



# # obj = Solution()

# # print(obj.addStrings(num1="0", num2="0"))


# """
# Task 2
# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

 

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).
# """


# # num = int(input("Enter a number: "))



# # def check_power_of_three(num):
# #     if num <= 0:
# #         return "Nagarsan qadanalim"
    
# #     if num % 3 == 0:
# #         if num / 3 == 1:
# #             return True
# #         else:
# #             return check_power_of_three(num/3)
# #     else:
# #         return False
    
# # print(check_power_of_three(num))



# """
# Task 3:
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
# """

# # num = int(input("Enter a number: "))

# # def check_ugly_number(num):
# #     if num == 1:
# #         return True

# #     if num % 2 == 0:
# #         return check_ugly_number(num/2)
    
# #     if num % 3 == 0:
# #         return check_ugly_number(num/3)
    
# #     if num % 5 == 0:
# #         return check_ugly_number(num / 5)

# #     return False


# # print(check_ugly_number(135))

# """
# Task 4:
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
# """

# # nums = [3,0,1]
# # # nums = [0,1]
# # # nums = [9,6,4,2,3,5,7,0,1]


# # class Solution:

# #     def missingNumber(self, nums):
# #         nums.sort()
# #         last_num = nums[-1]

# #         set1 = set(nums)
# #         set2 = set([i for i in range(0, last_num+1)])
# #         if set2 - set1 != set():
# #             return list(set2-set1)[0]
# #         else:
# #             return last_num + 1


# # obj = Solution()
# # print(obj.missingNumber(nums))




# # Task 1122. Relative Sort Array
# # class elem:
# #     def __init__(self,arr1,arr2):
# #         self.arr1 = arr1
# #         self.arr2 = arr2
# #     def sol(self):
# #         list1=[]
# #         list2=[]
# #         for i in arr2:
# #             for j in arr1:
# #                 if i==j:
# #                     list1.append(j)
# #         for k in arr1:
# #             if not k in arr2:
# #                 list2.append(k)
# #         return list1 + list2
    
# # arr1 = [2,3,1,3,2,4,6,7,9,2,19]
# # arr2 = [2,1,4,3,9,6]
    
# # myobj = elem(arr1,arr2)

# # print(myobj.sol())


# # #Task 290. Word Pattern

# # class Solution:
# #     def __init__(self,pattern,s):
# #         self.pattern = pattern
# #         self.s = s
# #     def wordPattern(self):
# #         res = {}
# #         self.s = self.s.split()
# #         if len(self.pattern) != len(self.s):
# #             return False
# #         for i in range(len(self.pattern)):
# #             if self.pattern[i] not in res.keys():
# #                 if self.s[i] not in res.values():
# #                     res[self.pattern[i]] = self.s[i]
# #                 else:
# #                     return False
# #             elif res[self.pattern[i]] != self.s[i]:
# #                 return False
# #         return True

# # myobj = Solution('abba','dog cat cat dog')

# # print(myobj.wordPattern())



# # pattern = "abba"
# # s = "dog cat cat dog"


# # res = {}
# # s = s.split()
# # if len(pattern) != len(s):
# #         print(False)

# # for i in range(len(pattern)):
# #     if pattern[i] not in res.keys():

# #         if s[i] not in res.values():
# #             res[pattern[i]] = s[i]
# #         else:
# #             print(False)

# #     elif res[pattern[i]] != s[i]:
# #                 print(False)
# # print(True)


# # print(res)


# # b = s.split(' ')
# # c=  list(pattern)
# # print(b)
# # print(c)

# # print((c[0])+(b[0]))
# # print((c[1])+(b[1]))
# # print((c[2])+(b[2]))
# # print((c[3])+(b[3]))


# # for i in pattern:
# #     if pattern.count(i)<=1:
# #         print(pattern.count(i))

# # print("##############")
# # for j in b:
# #     if  b.count(j) <= 1:
# #          print(b.count(j))

# # if pattern.count(i) == b.count(j):
# #      print(True)


# # 1726. Tuple with Same Product

# # nums = [2,3,4,6]
# # n=0

# # llist = []
# # for i in range(len(nums)):
# #     for j in range(i+1,len(nums)):
# #         for k in range(j+1,len(nums)):
# #             for l in range(k+1,len(nums)):
# #                 if nums[i]!=nums[j]!=nums[k]!=nums[l]:
# #                     llist.append(nums[i])
# #                     llist.append(nums[j])
# #                     llist.append(nums[k])
# #                     llist.append(nums[l])

# # print(llist)

# #1. Two Sum

# # class Solution:
# #    def __init__(self,nums,target):
# #       self.nums = nums
# #       self.target = target
# #    def app(self):
# #     indlist = []
# #     for i in range(len(nums)):
# #       for j in range(i+1,len(nums)):
# #         if nums[i]+nums[j] == target:
# #           indlist.append(i)
# #           indlist.append(j)
# #     return indlist

# # nums = [3,1,6,5]
# # target = 6
# # myobj = Solution(nums,target)

# # print(myobj.app())



# # n= input('my numb: ')
# # mylist = []
# # manumb = []
# # # mylist.append((n))
# # # print(mylist)

# # for i in range(len(n)):
# #     mylist.append(n[i])
# # j  = list(max(mylist))
# # f  = list(min(mylist))
# # # print(j)
# # # print(f)




# # c= j+f
# # d = set(n) - set(c)
# # print(c)
# # print(list(d))

# # print(max(mylist))
# # print(min(mylist))

# # for i in range(len(mylist)-1):
# #     if n[i]>n[i+1] > n[i+2]:
# #         manumb.append(n[i])

# # print(manumb)

# # 506. Relative Ranks

# # score = [10,3,8,9,4]
# # score.sort()
# # # score.reverse()

# # print(score)

# # b = score[::-1]

# # # print(b)


# # # Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# # # Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
    
# # placeup = ["Gold Medal", "Silver Medal","Bronze Medal"]
# # underplace = {}

# # for i in range(5):
# #     score.sort()
# #     if i <= 2:
# #         if b[i] not in underplace.keys():
# #             if placeup[i] not in underplace.values():
# #                 underplace[b[i]]=placeup[i]
# #     elif i>=3 and not i > 4:
# #         int(i)



# # print(underplace)


# # 747. Largest Number At Least Twice of Others

# # nums = [3,6,1,0]
# # nums = [1,2,3,4]
# # nums = [3,4,2,1,9]

# # nums.sort()
# # nums.reverse()

# # print(nums.index(0))


# # for i in range(len(nums)):
# #     for j in range(len(nums)):
# #         if i!=j:
# #             if not nums[i]>=nums[j]*2:
# #                 print(nums[-1])
# #                 break
                
# #             elif nums[i]>=nums[j]*2:
# #                 print(nums.index(nums[i]))
# #                 break
                

# # class Solution:
# #     def __init__(self,nums):
# #         self.nums = nums
# #     def dominantIndex(self):
# #         for i in range(len(nums)):
# #             for j in range(len(nums)):
# #                 if i!=j:
# #                     if not nums[i]>=nums[j]*2:
# #                         print( nums[-1])
# #                         break
# #                     elif nums[i]>=nums[j]*2:
# #                         print( nums.index(nums[i]))
# #                         break

# # nums = [3,6,1,0]

# # myobj = Solution(nums)

# # print(myobj.dominantIndex())
                        

# # # 1365. How Many Numbers Are Smaller Than the Current Number
# # n=0
# # nums = [8,1,2,2,3]
# # divlis = []

# # for i in range(len(nums)):
# #     for j in range(len(nums)):
# #         n+=1
# #         if nums[i]!=nums[j]:
# #             if nums[i]>nums[j]:
# #                 divlis.append(i)


# # print(divlis)

# # myout = [4,0,1,1,3]
# # divlist = []

# # nums.sort()
# # nums.reverse()

# # print(nums)


# # for i in range(len(nums)):
# #     for j in range(len(nums)):
# #         if i!=j:
# #             if nums[i]>nums[j]:
# #                 divlist.append(nums[j])
# #                 print(len(divlist))
                                



# # 1337. The K Weakest Rows in a Matrix

# # class Solution:
# #     def __init__(self, mat,k):
# #         self.mat = mat
# #         self.k = k
# #     def kWeakestRows(self):
# #         lll = []
# #         acz =[]
# #         listfk =[]
# #         for i in range(len(mat)):
# #             c = mat[i].count(1)
# #             lll.append(c)

# #         sorted_lll = sorted(lll)
# #         print(lll)
# #         print(sorted_lll)
# #         for it,valueit in enumerate(sorted_lll):
# #             for ij,valuejt in enumerate(lll):
# #                 if acz.count(ij)<1:
# #                     if valueit == valuejt:
# #                         acz.append(ij)
        
# #         for i in range(k):
# #             listfk.append(acz[i])
# #         return listfk


# # mat =[[1,1,0,0,0],
# #       [1,1,1,1,0],
# #       [1,0,0,0,0],
# #       [1,1,0,0,0],
# #       [1,1,1,1,1]]
# # k=3

# # myobj = Solution(mat,k)

# # print(myobj.kWeakestRows())


# # 1331. Rank Transform of an Array


# # arr = [40,10,20,30]
# # arr = [100,100,100]
# # arr = [37,12,28,9,100,56,80,5,12]
# # sorted_arr = sorted(arr)
# # # sorted_arr.reverse()
# # print(sorted_arr)
# # print(arr)
# # lima = []
# # for index1,item1 in enumerate(arr): 
# #     for index2,item2 in enumerate(sorted_arr):
# #         if arr == sorted_arr:
# #             lima.append(1)
# #             break
# #         elif item2 == item1:
# #                 lima.append(index2)


# # print(lima)


# # class Solution:
# #     def arrayRankTransform(self):
# #         list1=[]
# #         x=sorted(set(arr))
# #         dict1={}
# #         for i in range(len(x)):
# #             dict1[x[i]]=i+1
# #         for j in arr:
# #             y=dict1[j]
# #             list1.append(y)
# #         return list1

# # arr = [37,12,28,9,100,56,80,5,12]

# # myobj = Solution()

# # print(myobj.arrayRankTransform())


# # arr = [37,12,28,9,100,56,80,5,12]
# # print(arr)

# # b = sorted(set(arr))
# # print(b)

# # arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
# # sorted_arr = sorted(arr)
# # # sorted_arr.reverse()
# # print(sorted_arr)
# # print(arr)

# # lima = []
# # for index1, item1 in enumerate(arr):
# #     for index2, item2 in enumerate(sorted_arr):
# #         if sorted_arr == arr:
# #             lima.append(1)
# #             break
# #         elif item2 == item1:
# #             lima.append(index2+1)
# #             break

# # print(lima)


# # 217. Contains Duplicate




# # # nums = [1, 2, 3, 4, 6, 7, 8]
# # # is_unique = False

# # # for index, value in enumerate(nums):
# # #     if nums.count(value) > 1:
# # #         is_unique = True
# # #         break

        
# # # print(is_unique)

# class Solution:
#     def __init__(self,nums):
#         self.nums = nums
#     def containsDuplicate(self):
#         is_unique = False
#         for index, value in enumerate(self.nums):
#             if self.nums.count(value) > 1:
#                 is_unique = True
#                 break
#         return is_unique

# nums = [1, 2, 3, 4, 6, 7, 8]
# # nums = [1, 2, 3, 4, 6, 7, 8, 3, 3]
# myobj = Solution(nums)

# print(myobj.containsDuplicate())

# # # mylis = [1,2,3,4,5,6,7,8,9,10]



# # # print(mylis)

# # # for i in range(1,len(mylis),2):
# # #     mylis.remove(mylis[i])

# # # print(mylis)

# # # check = True

# # # for i in range(1,1000):
# # #     for j in range(1,1000):
# # #         for k in range(1,1000):
# # #             if i<j<k:
# # #                 if i*i+j*j == k*k:
# # #                     if i+j+k==1000:
# # #                         print(i,j,k)
           

# # # c = []

# # # for ind1,val1 in enumerate(c):
# # #     for ind2,val2 in enumerate(c):
# # #         if val1%val2 == 0:
# # #             break
# # #     else:
# # #         c.append(val1)
# # #         if ind1 == 10001:


# # # print(c)
# # # b = [2,3,7,1,8,4,6,9]
# # # c=[]
# # # for ind1,el1 in enumerate(b):
# # #     for ind2,el2 in enumerate(b):
# # #         if el1>el2:
# # #             b.remove(el1[ind1])
# # #             c.append(el1)

# # # # print(c)
# # # i = 2
# # # j = 1
# # # while i<=10001:
# # #     i+=1
# # #     j+=1
# # #     if i%j == 0:
# # #         break
# # # else:
# # #     print(i, "Sadedir")  



# # n = int(input("my number: "))


# # for i in range(2,3):
# #     if n%2==0 or n%2==1:
# #         print (n%2)




# # Task 1
# # Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# # Note that you must do this in-place without making a copy of the array.

 

# # Example 1:

# # Input: nums = [0,1,0,3,12]
# # Output: [1,3,12,0,0]
# # Example 2:

# # Input: nums = [0]
# # Output: [0]
# # """

# # # class Solution(object):
# # #     def moveZeroes(self, nums):
# # #         """
# # #         :type nums: List[int]
# # #         :rtype: None Do not return anything, modify nums in-place instead.
# # #         """


# # #         for elem in nums:
# # #             if elem == 0:
# # #                 nums.remove(elem)
# # #                 nums.append(elem)
            
# # #         return nums



# # # obj = Solution()
# # # print(obj.moveZeroes([0,1,0,3,12]))
# # # print(obj.moveZeroes([0]))



# # """
# # Task 2
# # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# # Notice that the solution set must not contain duplicate triplets.

 

# # Example 1:

# # Input: nums = [-1,0,1,2,-1,-4]
# # Output: [[-1,-1,2],[-1,0,1]]
# # Explanation: 
# # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# # The distinct triplets are [-1,0,1] and [-1,-1,2].
# # Notice that the order of the output and the order of the triplets does not matter.
# # Example 2:

# # Input: nums = [0,1,1]
# # Output: []
# # Explanation: The only possible triplet does not sum up to 0.
# # Example 3:

# # Input: nums = [0,0,0]
# # Output: [[0,0,0]]
# # Explanation: The only possible triplet sums up to 0.
# # """


# # # class Solution(object):
# # #     def threeSum(self, nums):
# # #         """
# # #         :type nums: List[int]
# # #         :rtype: List[List[int]]
# # #         """
# # #         result = []

# # #         for i in range(len(nums)):
# # #             for j in range(i+1, len(nums)):
# # #                 for k in range(j+1, len(nums)):
# # #                     if nums[i] + nums[j] + nums[k] == 0:
# # #                         data = [nums[i], nums[j], nums[k]]

# # #                         check = True
# # #                         for d in result:
# # #                             if sorted(d) == sorted(data):
# # #                                 check = False
# # #                                 break

# # #                         if check: result.append(data)        
# # #         return result



# # # obj = Solution()
# # # print(obj.threeSum([-1,0,1,2,-1,-4]))



# # """
# # Task 3
# # Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# # Return the sum of the three integers.

# # You may assume that each input would have exactly one solution.

 

# # Example 1:

# # Input: nums = [-1,2,1,-4], target = 1
# # Output: 2
# # Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# # Example 2:

# # Input: nums = [0,0,0], target = 1
# # Output: 0
# # Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# # """


# # # class Solution(object):
# # #     def threeSumClosest(self, nums, target):
# # #         """
# # #         :type nums: List[int]
# # #         :type target: int
# # #         :rtype: int
# # #         """
# # #         result = []
# # #         check = None

# # #         for i in range(len(nums)):
# # #             for j in range(i+1, len(nums)):
# # #                 for k in range(j+1, len(nums)):
# # #                     number = nums[i] + nums[j] + nums[k]
# # #                     new_val = abs(target-number)
# # #                     if not check:
# # #                         check = new_val
# # #                         result = [number]
# # #                     else:
# # #                         if check > new_val:
# # #                             check = new_val
# # #                             result = [number]
# # #                         elif check == new_val:
# # #                             result.append(new_val)

# # #         return result 


# # # obj = Solution()

# # # print(obj.threeSumClosest(nums = [-1,2,1,-4], target = 1))


# # """
# # Task 1
# # Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# # Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

# # Example 1:

# # Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# # Output: [2,2,2,1,4,3,3,9,6,7,19]
# # Example 2:

# # Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# # Output: [22,28,8,6,17,44]
# # """


# # # class Solution(object):
# # #     def relativeSortArray(self, arr1, arr2):
# # #         """
# # #         :type arr1: List[int]
# # #         :type arr2: List[int]
# # #         :rtype: List[int]
# # #         """
        
# # #         result = []; second = []

# # #         for i in arr2:
# # #             for j in arr1:
# # #                 if j == i:
# # #                     result.append(j)
                
# # #                 if not j in arr2 and not j in second:
# # #                     second.append(j)
        
# # #         return result + sorted(second)



# # # obj = Solution()

# # # print(obj.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
# # # print(obj.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))



# # """
# # Task 2
# # Given a pattern and a string s, find if s follows the same pattern.

# # Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# # Example 1:

# # Input: pattern = "abba", s = "dog cat cat dog"
# # Output: true
# # Example 2:

# # Input: pattern = "abba", s = "dog cat cat fish"
# # Output: false
# # Example 3:

# # Input: pattern = "aaaa", s = "dog cat cat dog"
# # Output: false
# # """


# # # class Solution(object):
# # #     def wordPattern(self, pattern, s):
# # #         """
# # #         :type pattern: str
# # #         :type s: str
# # #         :rtype: bool
# # #         """
        
# # #         check_dict = {}

# # #         s_list = s.split()
# # #         pattern_list = [i for i in pattern]

# # #         for index, value in enumerate(pattern_list):
# # #             if not value in check_dict.keys():
# # #                 check_dict[value] = s_list[index]
# # #             else:
# # #                 if check_dict[value] != s_list[index]:
# # #                     return False
        
# # #         return True



# # # obj = Solution()

# # # print(obj.wordPattern(pattern = "abba", s = "dog cat cat dog"))
# # # print(obj.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
# # # print(obj.wordPattern(pattern = "abba", s = "dog cat cat fish"))



# # """
# # Task 3
# # Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

# # Example 1:

# # Input: nums = [2,3,4,6]
# # Output: 8
# # Explanation: There are 8 valid tuples:
# # (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# # (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# # Example 2:

# # Input: nums = [1,2,4,5,10]
# # Output: 16
# # Explanation: There are 16 valid tuples:
# # (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# # (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# # (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# # (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
# # """


# # class Solution(object):
# #     def tupleSameProduct(self, nums):
# #         """
# #         :type nums: List[int]
# #         :rtype: int
# #         """
# #         result = []
        



# # obj = Solution()
# # print(obj.tupleSameProduct(nums = [2,3,4,6]))
# # print(obj.tupleSameProduct(nums = [1,2,4,5,10]))



# # """
# # Task 1
# # Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# # Return the answer in an array.

 

# # Example 1:

# # Input: nums = [8,1,2,2,3]
# # Output: [4,0,1,1,3]
# # Explanation: 
# # For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# # For nums[1]=1 does not exist any smaller number than it.
# # For nums[2]=2 there exist one smaller number than it (1). 
# # For nums[3]=2 there exist one smaller number than it (1). 
# # For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# # Example 2:

# # Input: nums = [6,5,4,8]
# # Output: [2,1,0,3]
# # Example 3:

# # Input: nums = [7,7,7,7]
# # Output: [0,0,0,0]
# # """


# # # class Solution(object):
# # #     def smallerNumbersThanCurrent(self, nums):
# # #         """
# # #         :type nums: List[int]
# # #         :rtype: List[int]
# # #         """
# # #         result = []

# # #         for i in nums:
# # #             count = 0
# # #             for j in nums:
# # #                 if i > j:
# # #                     count += 1
            
# # #             result.append(count)
        
# # #         return result

# # # obj = Solution()
# # # print(obj.smallerNumbersThanCurrent(nums=[8,1,2,2,3]))
# # # print(obj.smallerNumbersThanCurrent(nums=[6,5,4,8]))
# # # print(obj.smallerNumbersThanCurrent(nums=[7,7,7,7]))

# # """
# # Task 2
# # You are given an integer array nums where the largest integer is unique.

# # Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

# # Example 1:

# # Input: nums = [3,6,1,0]
# # Output: 1
# # Explanation: 6 is the largest integer.
# # For every other number in the array x, 6 is at least twice as big as x.
# # The index of value 6 is 1, so we return 1.
# # Example 2:

# # Input: nums = [1,2,3,4]
# # Output: -1
# # Explanation: 4 is less than twice the value of 3, so we return -1.
# # """

# # # class Solution(object):
# # #     def dominantIndex(self, nums):
# # #         """
# # #         :type nums: List[int]
# # #         :rtype: int
# # #         """
        
# # #         for i1, i in enumerate(nums):
# # #             check = True
# # #             for j1, j in enumerate(nums):
# # #                 if i1 == j1:
# # #                     continue
                
# # #                 if i < j*2:
# # #                     check = False
# # #                     break
            
# # #             if check: return i1
        
# # #         return -1


# # # obj = Solution()
# # # print(obj.dominantIndex(nums=[6,6,1,0]))



# # """
# # Task 3
# # You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# # The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# # The 1st place athlete's rank is "Gold Medal".
# # The 2nd place athlete's rank is "Silver Medal".
# # The 3rd place athlete's rank is "Bronze Medal".
# # For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# # Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

# # Example 1:

# # Input: score = [5,4,3,2,1]
# # Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# # Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# # Example 2:

# # Input: score = [10,3,8,9,4]
# # Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# # Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
# # """


# # class Solution(object):
# #     def findRelativeRanks(self, score):
# #         """
# #         :type score: List[int]
# #         :rtype: List[str]
# #         """
# #         sorted_score = sorted(score)
# #         print(sorted_score)
# #         order = {
# #             sorted_score[0]: "5",
# #             sorted_score[1]: "4",
# #             sorted_score[2]: "Bronze Medal",
# #             sorted_score[3]: "Silver Medal",
# #             sorted_score[4]: "Gold Medal",
# #         }

# #         return [order.get(i) for i in score]

    

# # obj = Solution()

# # print(obj.findRelativeRanks(score = [5,4,3,2,1]))
# # print(obj.findRelativeRanks(score = [10,3,8,9,4]))
# n=471
# k=3
# while k>0:
#     l=[]
#     maks = ''
#     minn = ''
#     for i in str(n):
#         l.append(i)
#     for j in sorted(l):
#         minn += j
#     for p in sorted(l)[::-1]:
#         maks += p
#     n=int(maks) - int(minn)
#     k=k-1
# print(n)

# n=int(input('Eded: '))

# for i in range(2, n):
#     if n%i==0:
#         print('Guzgu sade deyil')
#         break
# else:
#     k=str(n)[::-1]
#     k=int(k)
#     for i in range(2, k):
#         if k%i==0:
#             print('deyil')
#             break
#     else:
#         print('Bu ededler guzgu sadedir')
    
# n=13
# m=20
# cem, say = 0, 0

# for i in range(n, m+1):
#     for j in range(2, i):
#         if i%j==0:
#             break
#     else:
#         cem+=j
#         say+=1
# print(cem/say)


# sifre = input('Daxil edin: ')
# olmazlar = 'əğöüıçş'
 
# for i in sifre:
#     if i in olmazlar:
#         print(sifre.index(i), 'Duzgun deyil')
#         break
# else:
#     print('duzgundur')


# l=[2, 5, 1, 8]

# k=[]

# for i in l:
#     say=0

#     for j in l:
#         if i>j:
#             say=say+1
#     k.append(say)

# print(k)
            
# l=[1, 4, 2, 7, 5,3]

# for i in l:
#     if i==sorted(l)[::-1][0]:
#         print(i)
#         l[l.index(i)] = 'Gold Medal'
#     elif i==sorted(l)[::-1][1]:
#         l[l.index(i)] = 'Silver Medal'
#     elif i==sorted(l)[::-1][2]:
#         l[l.index(i)] = 'Bronz Medal'
#     else:
#         l[l.index(i)] = sorted(l)[::-1].index(i)
# print(l)
    
    
    
# money = [500, 200, 100, 50, 20, 10, 5, 1]

# n=int(input('Pulu daxil edin: '))

# for i in money:
#     if n//i>0:
#         print(i, '*', n//i )
#         n=n%i
    

# """
# 18.	 Müstəvi üzərində olan bir robot (0, 0) nöqtəsindən hərəkətə başlayır. 
# İstiqamətləri bir string şəklində göstərilir. Keçərli hərəkətlər: Sol(L),
#  sağ(R), yuxarı(U), aşağı(D). Bunlara görə hərəkət sırası verilən bir robotun hərəkəti 
#  tamaladıqdan sonra başlanğıc nöqtəsində olubolmadığını tapan bir funksiya yazın. 
#  Məsələn, UD- true, RUD- false
# """


# def Koordinat(n):
#     x=0
#     y=0
#     for i in n:
#         if i=='R' or i=='r':
#             x+=1
#         elif i=='L' or i=='l':
#             x-=1
#         elif i=='U' or i=='u':
#             y+=1
#         else:
#             y-=1
#     if x==0 and y==0:
#         print('Ud', x, y)
#     else:
#         print('Rud', x, y)

# Koordinat(input('Koordinat'))



# def Sade(k):
#     n=3
#     while k>1:
#         for i in range(2, n):
#             if n%i==0:
#                 break
#         else:
#             print(n)
#             k=k-1
#         n=n+1

# Sade(int(input('Eded: ')))




# def bolen(k):
#     for i in range(2, k):
#         if k//i==k%i:
#             print(i)
# bolen(int(input('Eded: ')))




# def ikilik(k):
#     cavab = ''
#     while k>0:
#         if k%2==0:
#             cavab+=str(0)
#         elif k==1:
#             cavab+=str(1)
#         else:
#             cavab+=str(1)
        
#         k=k//2
#     print(cavab[::-1])

# ikilik(int(input('Eded')))




# def liste(k, n):
#     for i in k:
#         for j in k:
#             if i+j==n:
#                 print(k.index(i), k.index(j))
#     else:
#         print('yoxdur')
        
# liste([3, 5, 2, 7, 8], 10)




# mat = [[1,1,0,0,0], [1,1,1,1,0], [1, 0, 0, 0, 0], [1, 1, 0,0,0], [1,1,1,1,1]]

# l=[]
# k=[]
# p=[]
# for i in mat:
#     cem=0
#     for j in i:
#         cem+=j
#     l.append(cem)
#     p.append(cem)
    
# maks=l[0]
# while len(l)>0:
#     for i in l:
#         if i>maks:
#             maks=i
#         k.append(p.index(i))
        
#         l.remove(i)

# print(k)




# l=[37, 12, 28, 9, 100, 56, 80, 5, 12]
# k=sorted(set(l))
# num = []
# for i in l:
#     say=0
#     for j in k:
#         if i>j:    
#             say+=1
#     count = say+1
#     num.append(count)
# print(num)


# for a in range(1, 1000):
#     for b in range(1, 1000):
#         if a**2+b**2==(1000-a-b)**2:
#             print(a, b, 1000-a-b)


# n=int(input('EDed: '))

# for i in range(2, n):
#     if n%i==0:
#         print('Sade deyil')
#         break
# else:
#         print('Sadedir')

    

# n=int(input('Say: '))
# k=2

# while n>0:
#     for i in range (2, k):
#         if k%i==0:
#             break
#     else:
#         n=n-1

#     k=k+1
    
# print(k-1)
    
    
# n=int(input('Eded: '))

# count=0

# while n>0:
#     if n%2==1 or n==1:
#         count+=1
        
#     n=n//2

# print(count)




# ######################################################
# def Ortalama(n):
#     cem=0
#     say=0
#     for i in n:
#         cem+=i
#         say+=1
    
#     return cem/say


# def Hasil(n):
#     hasil=1
#     for i in n:
#         hasil*=i
    
#     return hasil

# def Toplam(n):
#     cem=0
#     for i in n:
#         cem+=i
        
#     return cem

# def Maksimum(n):
#     maks=n[0]
#     for i in n:
#         if i>maks:
#             maks=i
    
#     return maks

# def Minimum(n):
#     minn=n[0]
#     for i in n:
#         if i<minn:
#             minn=i
            
#     return minn

# class Operation:
#     def __init__(self, lst):
#         self.lst = lst

#     def showResult(self):
#         result = {
#             'ortalama': Ortalama(self.lst),
#             'hasil': Hasil(self.lst),
#             'toplam': Toplam(self.lst),
#             'max': Maksimum(self.lst),
#             'min': Minimum(self.lst)
#         }
#         return result

# operation = Operation([3, 5, 2, 7, 9, 4])
# result = operation.showResult()
# print(result)

# ##################################

# db = [{"username": "fhuseyn", "password": "admin123"}, {"username": "admin", "password": "hello#admin123"}]
# def register():
#     username = input("Username: ")
#     password = input("Password: ")

#     if len(username) > 8 and len(password) > 6 and password[0].isupper() and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
#         user = {"username": username, "password": password}
#         db.append(user)
#         print("Qeydiyyat oldu")
#     else:
#         print('Melumatlarda sehvlik var.')

# register()


# def login():
#     username = input("Username: ")
#     password = input("Password: ")

#     for user in db:
#         if user["username"] == username and user["password"] == password:
#             print("Xos geldiniz!")
#             return

#     print("Melumatlar yanlisdir!")

# login()





# ########################################################################

# n=int(input('Eded: '))

# say=0

# while n>1:
#     if n%2==0:
#         n=n//2
#     else:
#         n=n+1
    
#     say=say+1
    
# print(say)

# ########################################################################

# gun_1='EKB'
# gun_2='BEK'
# gun_3='KBE'
# gun_4='EKB'

# n=int(input('EDED: '))

# if n%4==1:
#     print('EKB')
# elif n%4==2:
#     print('BEK')
# elif n%4==3:
#     print('KBE')
# else:
#     print('EKB')


# import math

# n=6.5

# result = math.floor(n)
# #result = int(float(n))
# print(result)

# ###########################################################################

# def Kvadrat_kok(x):
#     if x == 0 or x == 1:
#         return x
    
#     x = 1
#     y = x // 2
    
#     while x <= y:
#         mid = (x + y) // 2
#         kvadrat = mid * mid
        
#         if kvadrat == x:
#             return mid
#         elif kvadrat < x:
#             x = mid + 1
#         else:
#             right = mid - 1
    
#     return right



# Kvadrat_kok(int(input("Eded:")))

# ###########################################################################
# def AddimSayi(n):
#     if n == 0 or n == 1:
#         return 1
    
#     l = [0] * (n + 1)
#     l[0] = 1
#     l[1] = 1

#     for i in range(2, n + 1):
#         l[i] = l[i - 1] + l[i - 2]
#     return l[n]

# AddimSayi(int(input('Eded: ')))

# ###############################################################################
# def Happy(n):
#     yoxlama = set()
    
#     while n != 1:
#         if n in yoxlama:
#             return False
#         yoxlama.add(n)
#         n = sum(int(i) ** 2 for i in str(n))
    
#     return 'Happy'

# Happy(12)
# #####################################################################
# c= []
# b = int(input("my number is: "))
# for i in range(0,b):
#     for j in range(0,b):
#         if i==j:
#             if i*j<=b:
#                 c.append(i)
                
# print(max(c))
# ##################################################
# n=int(input('Eded: '))
# n1, n2 = 1, 1
# say=0

# while say<n:
#     n3=n1+n2
#     n1, n2 = n2, n3
#     say=say+1

# print(n1)


# #####################################################

# n=input('Qiymet: ').split(' ')
# n=list(map(int, n))
# m=int(input('Pulunuz: '))
# k=[]
# for i in n:
#     for j in n:
#         if n.index(i)==n.index(j):
#             continue
#         elif i+j<m:
#             k.append([i, j, m-i-j])
# if len(k)==0:
#     print('Pulumuz catmir')

# else:
#     minn=k[0][2]
#     for i in k:
#         if i[2]<minn:
#             minn=i[2]
    
#     print(minn)
# print(k)
    
# def leftover_money(prices, money):
#     min_price = float('inf')  

#     for i in range(len(prices)):
#         for j in range(i + 1, len(prices)):
#             remaining_money = money - prices[i] - prices[j]
#             if remaining_money > 0 and remaining_money < min_price:
#                 min_price = remaining_money

#     if min_price == float('inf'):
#         return money
#     else:
#         return min_price



# prices = [1, 2, 2]
# money = 4
# print(leftover_money(prices, money))
# #######################################################


# ###############################################
# k=[4,1,4,0,3,5]
# l=set([])

# while len(k)>0:
    
#     k=sorted(k)
#     print(k)
#     l.add((k[0]+k[-1])/2)
    
#     k.pop(0)
#     k.pop(-1)

# print(len(l))
# print(l)
# ####################################################


# k=['Saday', 'Nicat', 'Eli', 'Seymur']
# l=[1.67, 1.85, 1.70, 1.65]
# s=sorted(l)[::-1]
# p=[]

# for i in s:
#     for j in l:
#         if i==j:
#             x=l.index(j)
#             p.append(k[x])

# print(p)
            

# #################################################

# def splitNum(num):
#         copy = [int(x) for x in str(num)]
#         copy.sort()
#         num1 = 0
#         num2 = 0
#         for i in range(0,len(copy)):
#             if i %2 == 0:
#                 num1 = num1*10 + copy[i]
#                 print(num1)
#             elif i %2 !=0:
#                 num2 = num2*10 + copy[i]
#                 print(num2)
#         return num1 + num2
# splitNum(42353)




# 1646. Get Maximum in Generated Array

# You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# Return the maximum integer in the array nums​​​.

# class Solution:
#     def __init__(self,n):
#         self.n = n
#     def MyMax(self):
#         nums=[]
#         for i in range(n+1):
#             nums.append(0)

        
#         for i in range(n+1):
#             if i == 0 or i ==1:
#                 nums[i] = i
#             elif i%2 !=0:
#                 nums[i]=nums[i//2]+nums[(i//2)+1]
#             elif i%2 ==0:
#                 nums[i] = nums[int(i/2)]
#         return max(nums)

# n=7
# myobj = Solution(n)

# print(myobj.MyMax())

# def calc_for_range(n):
#     return n + calc_for_range(n-1) if n > 1 else 0


# func1 = calc_for_range(4)

# print(func1)e

# class Solution:
#     def __init__(self, nums, k):
#         self.k = k
#         self.nums = nums
#     def goodIndices(self):
#         l = []
#         for i in range(k,len(self.nums)-k):
#             if self.nums[k-2]>=self.nums[k-1] and self.nums[k+1]<self.nums[k+2]:
#                 l.append(self.nums.index(self.nums[i]))
#             self.k=self.k+k
#         return l

# nums = [2,1,1,1,3,4,1]
# k = 2

# myobj = Solution(nums,k)

# print(myobj.goodIndices())



# 1.	Tək sətirdə n sayda boşluqla ayrılmış ədəd daxil edilir. Ən böyük və ən kiçiyin cəmini ekrana yazdırın. (max ve minn istifade etmeden)

# n = input("my numbers: ")
# d = []
# for ind,val in enumerate(n):
#     if val.isdigit():
#         d.append(val)

# print(d)

# # minus = d[0]
# # maxus = d[0]
# # for i in d:
# #     if i>maxus:
# #         maxus=i
# #     elif i<minus:
# #         minus =i

# # print(int(minus)+int(maxus))





# # 2.Tək sətirdə n sayda boşluqla ayrılmış ədəd daxil edilir. 
# # İndeksi 3-ə qalıqsız bölünən müsbət ədədlərin sayını və cəmini boşluqla ayrılmış şəkildə ekrana yazdırın.
# a= 0
# b=''
# inds=[]
# sums=[]
# for ind,val in enumerate(d):
#     if ind%3 == 0 and ind!=0:
#         inds.append(int(val))
#         a +=int(val)
#         # print(a)
# b+=str(a)

# # print(inds)

# # print(b[0]+''+b[1])
# print(str(len(inds))+' '+b)




# 3.	İki söz daxil edilir və 2-ci sözün 1-ci sözün hərflərindən əmələ gəlib gəlmədiyi yoxlanılır. 


# d = {'alacam'}
# b = {'alcaam'}



# if b.issubset(d):
#     print(True)
# else:
#      print(False)




# 4.	2-lik say sistemində daxil edilən ədədin 10-luq sistemdəki qarşılığını ekrana yazdırın.

# c=[]
# num2 = '11001'
# for i in range(0,len(num2)):
#     b = int(num2[i])*2**(len(num2)-1-i)
#     c.append(b)
# print(c)
# print(sum(c))


# d = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# a=[2,3,4,5,6,7,8,9]
# odd = []
# even = []
# for ind1,val1 in enumerate(d):
#     for ind2,val2 in enumerate(a):
#         if val1!=val2 and val1>val2:
#             if val1%val2!=0:
#                 odd.append(val1)
                
#             elif val1%val2 == 0:
#                 even.append(val1)
# print(odd)
# print(even)



# 54. Spiral Matrix

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# c = []
# b = []


# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# new_matrix = []
# for i in range(1):
#         b = matrix[i]+[matrix[i+1][-1]]+matrix[i+2][::-1]
#         d = set(matrix[1])-set([matrix[1][-1]])
#         new_matrix = b+list(d)
    

# print(new_matrix)

# class Solution:
#       def __init__(self,matrix):
#              self.matrix = matrix

#       def spiralOrder(self):
#              new_matrix = []
#              if len(matrix)>2:
#                 for i in range(1):
#                     b = matrix[i]+[matrix[i+1][-1]]+matrix[i+2][::-1]
#                     d = set(matrix[1])-set([matrix[1][-1]])
#                     new_matrix = b+list(d)
#                 return new_matrix
#              else:
#                 return matrix[i]
      

# matrix = [[1]]

# # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# myobj = Solution(matrix)
# print(myobj.spiralOrder())



# 67. Add Binary

# Input: a = "11", b = "1"
# Output: "100"
             
# Input: a = "1010", b = "1011"
# Output: "10101"

# a = "11"
# b = "1"
# c= 0
# d= 0
# for i in range(len(a)):
#    c += int(a[i])*(2**((len(a)-1)-i))
# for i in range(len(b)):
#    d += int(b[i])*(2**((len(b)-1)-i))


# print(c)
# # print(d)
# n = 20
# i = -5
# while i<n:

#    if n!=1:
#       if n%2==0 or n%2==1:
#          print(int(n%2),end='')
#    else:
#       print(int(n))
#    n=n//2
#    i=i+1



          
# 345. Reverse Vowels of a String

# Input: s = "hello"
# Output: "holle"

# Input: s = "leetcode"
# Output: "leotcede"

# v = ['a','e','o','u','i']
# s = 'hello'
# # s = "leetcode"
# c = []
# d = {}

# for i in s:
#         c.append(i)

                        
# # print(c)                        
                
# for ind,val in enumerate(c):
#         if val in v:
#                 d[ind] = val

# reversed_d = list(reversed(d.values()))

# print(reversed_d)

# for val in d.values():
#        if val == c:
#                print(c)

# print(c)
                 


        
# 118. Pascal's Triangle


# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# b = []

# while len(b)<6:
#     b.append([1])
    
# print(b)




# 242. Valid Anagram

# s = "anagram"
# t = "nagaram"
# for i in s:
#     if not i in t or s.count(i)!= t.count(i):
#         print(False)
#         break
# else:
#     print(True)




# class Solution:
#     def __init__(self,s,t):
#         self.s = s
#         self.t = t
#     def isAnagram(self):
        
#         if len(self.s)!=len(self.t):
#                   return False
          
#         count = {}
#         for char in s:
#             count[char] = count.get(char, 0) + 1
        
#         for char in t:
#             if char not in count or count[char] == 0:
#                 return False
#             count[char] -= 1
        
#         return True
    
# s = "accc"
# t = "ccac"

   
# myobj = Solution(s,t)

# print(myobj.isAnagram())            



# 13. Roman to Integer

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000



# d = {'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}
# s='mcm'
# a=0
# c=[]
# for i in s:
#     if i in d:
#         c.append(s.count(i)*d[i])

# print(c)
# if len(c)>2:
#    for i in range(len(c)-1):
#          if c[i]>c[i+1] and c[i]!=c[i+2] and c[i+1]>c[i+2]:
#              print(c[i]+c[i+1])
#              c.remove(c[i])
#              c.remove(c[i+1])
#              if len(c)<2:
#                  break
#          elif c[i]>c[i+1] and c[i]==c[i+2]:
#              print(c[i])
#              print(c[i+2]-c[i+1])
#              c.remove(c[i])
#              c.remove(c[i+1])
#              c.remove(c[i+2])
#          elif c[i]<c[i+1]:
#              print(c[i+1]-c[i])
#              c.remove(c[i])
#              c.remove(c[i+1])
             
             
# else:
#    print(c[i])


# 9. Palindrome Number


# class Solution:
#     def __init__(self,x):
#         self.x = x
    
#     def isPalindrome(self):
#         c = []
#         for i in str(self.x):
#             c.append((i))
#         if c[::-1]==c:
#             return True
#         else:
#             return False
# x =-202
# myobj = Solution(x)

# print(myobj.isPalindrome())




# 14. Longest Common Prefix

# for ind1,val1 in enumerate(c[0]):
#     for i in range(len(strs)):
#         if  val1 != strs[i][ind1]:
#             break
#     else:
#         j+=val1

# print(j)


# class Solution:
#      def __init__(self,strs):
#           self.strs = strs
#      def longestCommonPrefix(self):     
#         b = []
#         c = []
#         for i in range(len(strs)):
#             b.append(len(strs[i]))
#         a = min(b)

#         j = ''
#         for i in strs:
#             if len(i) == a:
#                 c.append(i)
#                 strs.remove(i)
#                 break
#         found_difference = True
#         for ind1, val1 in enumerate(c[0]):
#             for i in range(len(strs)):
#                 if val1 != strs[i][ind1]:
#                     found_difference = False
#                     break
#                 if not found_difference:
#                     break
#             else:
#                 j += val1

#         return j

# strs = ['car','cir']
# strs = ["flower","flow","flight"]
# strs = ['a','a','b']

# myojb = Solution(strs)
# print(myojb.longestCommonPrefix())



# 121. Best Time to Buy and Sell Stock

# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# a = []
# for i in range(len(prices)):
#     for j in range(i+1,len(prices)):
#             a.append(prices[j]-prices[i])

# for d in range(len(a)):
#       if a[d]>0:
#             print(max(a))
#             break
# else:
#       print(0)

# print((a))

# class Solution:
#       def __init__(self,prices):
#             self.prices = prices

#       def maxProfit(self):
#             a = []
#             check = True
#             for i in range(len(prices)):
#                 for j in range(i+1,len(prices)):
#                     a.append(prices[j]-prices[i])

#             for d in range(len(a)):
#                 if a[d]>0:
#                     check
#                     break
#             else:
#                  check = False
            
#             if check:
#                  a = max(a)
#             else:
#                  a = 0
#             return a


# # prices = [7,6,4,3,1]
# prices = [7,1,5,3,6,4]

# myobj = Solution(prices)       
# print(myobj.maxProfit())     


# class Solution:
#     def __init__(self, prices):
#         self.prices = prices

#     def maxProfit(self):

#         max_profit = 0
#         min_price = self.prices[0]

#         for price in self.prices[1:]:
#             if price < min_price:
#                 min_price = price
#             else:
#                 profit = price - min_price
#                 if profit > max_profit:
#                     max_profit = profit

#         return max_profit


# prices = [7, 1, 5, 3, 6, 4]
# prices = [7,6,4,3,1]

# myobj = Solution(prices)
# print(myobj.maxProfit())



# 88. Merge Sorted Array

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# if not nums2:
#     print(nums1)
# elif not nums1:
#     print(nums2)
# else:
#     if m>n:
#         for i in range(n,m+n):
#             nums1[i] = nums2[i-m]
#             print(nums1)
#     elif n>m:
#         for i in range(m,m+n):
#             nums2[i] = nums1[i]
#             print(nums2)
#     else:





# class Solution:
#     def __init__(self,nums1, m, nums2, n):
#         self.nums1 = nums1
#         self.m = m
#         self.nums2 = nums2
#         self.n = n
    
#     def merge(self):
#         if nums2:
#             for i in range(n,m+n):
#                 nums1[i] = nums2[i-m]

#         return sorted(nums1)



# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# # nums1 = [1,2,3,0,0,0]
# # m = 3
# # nums2 = [2,5,6]
# # n = 3
# # nums1 = [0]
# # m = 0
# # nums2 = [1]
# # n = 1

# myobj = Solution(nums1, m, nums2, n)

# print(myobj.merge())



# if nums2:
#     for i in range(n,m+n):
#         nums1[i] = nums2[i-m]
# sorted_nums = sorted(nums1)

# print(sorted_nums)


# 70. Climbing Stairs



# class Solution:
#     def __init__(self,n):
#         self.n = n
#     def climbStairs(self):
#         m=0
#         j=0
#         k=1
#         for i in range(n):
#             m=j+k
#             j=k
#             k=m
#         return m    
# n=6

# myobj = Solution(n)
# print(myobj.climbStairs())



# 169. Majority Element
# nums = [3,2,3]
# nums = [3,3,4]
# nums = [2,2,1,1,1,2,2]
# c= 0
# check = True
# for i in set(nums):
#     if nums.count(i)> len(nums)/2:
#         c=i
# print(c)    


# 1351. Count Negative Numbers in a Sorted Matrix


# class Solution:
#     def __init__(self,grid):
#         self.grid = grid
#     def countNegatives(self):
#         minlist = []
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]<0:
#                     minlist.append(grid[i][j])

#         if not minlist:
#             return 0
#         else:
#             return len(minlist)
        
# # grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# grid = [[3,2],[1,0]]

# myobj = Solution(grid)
# print(myobj.countNegatives())




# 744. Find Smallest Letter Greater Than Target


# letters = ["c","f","j"]
# target = 'a'

# # letters = ["c","f","j"]
# # target = "c"

# # letters = ["x","x","y","y"]
# # target = "z"
# for i in range(len(letters)):
#     if letters[i]>target and letters[i]!=target:
#         print(min(letters[i]))
#         break
# else:
#     print(letters[0])




# 3. Longest Substring Without Repeating Characters


# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# s = "dbdbae"
# f = s[0]

# if len(set(s)) == 1:
#     print('1')
# else:
#     for i in range(1,len(s)):
#         if f in s[i:len(s)]:
#             f=s[0:i]
# if len(f)==1:
#     print(len(set(s)))-1
# else:
#     print(f)


# s= 'bbbbb'
# s = "pwwkewawe"
# print(set(s))

# d = []
# print(len(set(s)))


# for i in range(len(s)):
#     if i+1 <= len(s)-1:
#          if s[i] == s[i+1]:
#             continue
#          else:
#            d.append(s[i])

# print(d)


# 859. Buddy Strings
# s = "aaaaaabc"
# s1 = []
# for i in s:
#     s1.append(i)
# # print(s1)

# goal = "aaaaaacb"
# goal1 = [] 
# for i in goal:
#     goal1.append(i)
# # print(goal1)
# check = True
# for ind1,val1 in enumerate(s1):
#     for ind2,val2 in enumerate(goal1):
#         if ind1!=ind2:
#             s1[ind1]=val2
#             if goal1 != s1:
#                 s1[ind1] = val1
#             else:
#                 if ind2-ind1 ==1:
#                     print(True)




# list1 = [1,2,4]
# list2 = [1,3,4]

# a = []
# b = 0
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i] > b or list2[j]>b:
#             a.append(list[])


#  605. Can Place Flowers
# flowerbed =  [1,0]

# flowerbed = [1,0,0,0,1]
# n = 1
# check = True
# if n>0:
#         if flowerbed.count(0)/flowerbed.count(1)>n:
#             if flowerbed.count(0)-flowerbed.count(1)>=1:
#                 check = True
#             else:
#                 check = False
#         else:
#              check = False

# else:
#     check = True

# print(check)
# class Solution:
#     def __init__(self,flowerbed, n):
#         self.flowerbed = flowerbed
#         self.n = n
#     def canPlaceFlowers(self):
#         check = True
#         if n>0:
#                 if flowerbed.count(0)/flowerbed.count(1)>n:
#                     if flowerbed.count(0)-flowerbed.count(1)>=1:
#                         check = True
#                     else:
#                         check = False
#                 else:
#                     check = False

#         else:
#             check = True

#         return check

# flowerbed = [1,0,0,0,1]
# n = 1
# myobj = Solution(flowerbed, n)

# print(myobj.canPlaceFlowers())



# 35. Search Insert Position

# nums = [1,3,5,6]
# target = 4

# for ind, val in enumerate(nums):
#     if target == val:
#         print(ind)
#         break
# else:
#     nums.append(target)
#     a = sorted(nums)
#     for ind,val in enumerate(a):
#         if val == target:
#             print(ind)


# 36. Valid Sudoku
# a= []

# board = [["5","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]
# for i in range(len(board)):
#     for ind1,val1 in enumerate(board[i]):
#            for ind2,val2 in enumerate(board[i]):
#                 if board[i][ind1].isalnum():
#                     a.append(val1)
#                     if board[i][ind1]!=board[i][ind2]:
#                             a.append(val1)
#     else:
#         print(False)
#     print(a)
#     print(True)
#     a.clear()
    # if (len(set(a))) == len(a):
    #             print(True)
    #             a.clear()
        
    # else:
    #      print(False)                # if len(set(board[i]))== len(board[i]):
                #         if board[i][ind]!=board[i+1][ind]:
                #             print(True)
    #         a.append(board[i][ind])
    # for d in range(len(a)):
    #     if len(set(a))==len(a):
    #         print(set(a))
    #         print(a)
    #         a.clear()
# for i in range(len(board)):
#     for j in range(len(board[i])):
#         if set(board[i])==board[i]:
#             print(True)


# 55. Jump Game


# nums = [3,2,1,0,4]
# nums = [1]
# nums = [2,0]
# nums = [1,2,3]
# for ind,val in enumerate(nums):
#     if 1<ind+val<len(nums) and len(nums)>1:
#         if nums[ind+val]==nums[-1]:
#             print(True)
#     elif val>len(nums)-1 or val ==0:
#         print(True)




# d= []

# footsteps = ['r','r','r','r','l','l','l','l','r','r']
# w=1
# for i in footsteps:
#     if i=='r':
#         w=w+1
#         d.append(w)
#     elif i=='l':
#         w=w-1
#         d.append(w)
#     else:
#         w=w+0
#         d.append(w)

# print(max(d))



# 28. Find the Index of the First Occurrence in a String

# haystack = "sadbutsad"
# needle = "sad"

# class Solution:
#     def strStr(self, haystack, needle):
        
#         if needle in haystack:
#             return (haystack.find(needle))
#         else:
#             return -1
        
# myobj= Solution()
# print(myobj.strStr("sadbutsad","but"))



# 2. Add Two Numbers

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
# out = []
# Output: [8,9,9,9,0,0,0,1]


# string1 = ''
# string2 = ''
# c = []


# for i in l1:
#     string1+=str(i)

# for j in l2:
#     string2+=str(j)


# summary = int(string1)+int(string2)

# summary=str(summary)


# for ind,val in enumerate(summary):
#     c.append(int(val))

# c.reverse()
# print(c)


# class Solution:
#     def addTwoNumbers(self, l1, l2):      
#         string1 = ''
#         string2 = ''
#         c = []
#         for i in l1:
#             string1+=str(i)

#         for j in l2:
#             string2+=str(j)

#         summary = int(string1)+int(string2)

#         summary=str(summary)


#         for ind,val in enumerate(summary):
#             c.append(int(val))

#         c.reverse()

#         return c


# myobj = Solution()

# print(myobj.addTwoNumbers(l1 = [9,9,9,9,9,9,9],l2 = [9,9,9,9]))


# 5. Longest Palindromic Substring

# # Example 1:
# s = "babad"
# Output= "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# s = "acdbbn"
# # # Output= "bb"
# # d=[]
# d=[]
# f=[]
# for i in s:
#     d.append(i)
# for j in d:
#     f.append(j)

# c=d[0]
# t= False 

# for i in range(1,len(d)):
#     c+=d[i]
#     if c==c[::-1]:
#         t=True
#         print(c)

# else:
#     if t==False:   

#         c=d[0]
#         for i in range(1,len(d)):
#                 if len(d)>2:
#                     c+=d[i]
#                     # print(c)
#                     if c!=c[::-1]:
#                         d.reverse()
#                         d.pop()
#                         d.reverse()
#                         print(d)
#                     else:
#                         print(c)
#             # else:        
        #     print(f[0])
        

# class Solution:
#     def longestPalindrome(self,s):
#         # d=[]
#         # for i in s:
#         #     d.append(i)
      
#         # c=d[0]
#         # t= True 

#         # for i in range(1,len(d)-1):
#         #     c+=d[i]
#         #     if c==c[::-1]:
#         #         t=True
#         #         return c

#         # else:   
#         #     t=False

#         #     if t==False:
#         #         d.pop()
#         #         c=d[0]
#         #         for i in range(1,len(d)-1):
#         #                 c+=d[i]
#         #                 if c!=c[::-1]:
#         #                     t=False
#         #         else:
#         #             if c:
#         #                 return c
#         #             else:
#         #                 return s[0]
                
# myobj= Solution()
# print(myobj.longestPalindrome("abba"))


#hackerrank

# n=int(input())
# # n = int(input("your number: "))

# arr = map(int, input().split())

# # print(n,arr)
# # print(list(arr)[1])
# d= max(list(arr))

# # list(arr).remove(d)
# # print(list(arr))

# for j in list(arr):
    # print(j)
        #  if list(arr)[i]!=j and list(arr)[i]!=d:
        #     if list(arr)[i]>j:
        #         b=list(arr)[i]
        #         print(b)






# 7. Reverse Integer

# x = -123
# c= []


# for i in str(x):
#     c+=i

# if '-' in c:
#     c.remove('-')
#     c.append('-')

# c.reverse()
# d=''
# # print(c)
# for j in c:
#     d+=j

# d=int(d)
# if -2**31<=d<=2**31:
#     print(d)  
# else:
#     print(0)





# 8. String to Integer (atoi)

# s = "42"
# s = "   -42"
# # s = "4193 with words"
# d=''
# for i in s:
#     if i.isnumeric() or '-' in i:
#         d+=i
# d=int(d)

# print(d)



# 19. Remove Nth Node From End of List


# head = [1,2,3,4,5]
# n = 2

# print(head[-2])

# head = [1]
# n = 1

# head.remove(head[-n])
# print(head)
# head.remove(head[-n])
# print(head)

# print(head[-1])

# head = [1,2]
# n = 1

# head.remove(head[-n])
# print(head)

# head.remove(-n)

# print(head)



# 26. Remove Duplicates from Sorted Array


# nums=[0,0,1,1,1,2,2,3,3,4]
# nums=[1,1,1,1,1,1]
# nums=[1,1,2]

# exceptedNums = []
# for i in nums:
#     exceptedNums.append(i)
#     if exceptedNums.count(i)>1:
#         exceptedNums.remove(i)

# nums.clear()

# for j in exceptedNums:
#     nums.append(j)

# print(len(nums))



# 27. Remove Element


# nums = [3,2,2,3]
# val = 3

# # Output, nums =2, [2,2,_,_]

# # nums = [0,1,2,2,3,0,4,2]
# # val = 2

# # Output, nums= 5, [0,1,4,0,3,_,_,_]

# for j in range(len(nums)):
#     for i in nums:
#         if val == i:
#             nums.remove(i)

# print(nums)


# 283. Move Zeroes

# nums = [0,1,0,3,12]

# d=[]
# for j in range(len(nums)):
#     for i in nums:
#         if i==0:
#             nums.remove(i)
#             d.append(i)

# for i in d:
#     nums.append(i)


# print(d)
# print(nums)



# 2460. Apply Operations to an Array

# nums = [1,2,2,1,1,0]
# Output: [1,4,2,0,0,0]


# class Solution:
#     def applyOperations(self, nums):

#         zeros=[]
#         for i in range(len(nums)):
#             if i<=len(nums)-2:
#                 if nums[i]==nums[i+1]:
#                     nums[i]=nums[i]*2
#                     nums[i+1]=0

#         for i in range(len(nums)):
#             for j in nums:
#                 if 0==j:
#                     zeros.append(0)
#                     nums.remove(0)

#         for d in zeros:
#             nums.append(d)

#         return nums


# myobj= Solution()

# print(myobj.applyOperations(nums = [1694,399,832,1758,0,412,0,206,272,0,0,0,0,0]
# ))


# 2150. Find All Lonely Numbers in the Array

# nums = [9,6,5,8]
# nums = [1,2,4,8]
# nums = [75,35,59,66,69,53,37,16,60,98,11,33,3,85,59,65,59,44,34,89,72,47]
# # nums = [1,3,5,3]

# c=False

# d=[]
# b=[]
# # for i in range(len(nums)):
# #     if nums.count(nums[i])==1:
# #         d.append(nums[i])

# for i in range(len(nums)):
#     if  not nums[i]+1 in nums and not nums[i]-1 in nums and not nums.count(nums[i])>1:
#             c=True
#     else:
#         b.append(nums[i])

# for i in b:
#     if i in nums:
#         nums.remove(i) 

# # for i in range(len(nums)):
# #     if nums.count(nums[i])==1:
# #         d.append(nums[i])

# print(nums)
# nums = d        
# print(nums)            


# import pandas as pd

# d = {"student_id":[32,217,779,849],"name":["Piper",None,"Georgia","Willow"],"age":[5,19,20,14]}

# df = pd.DataFrame(data=d)
# c=[]

# for i in d.keys():
#     for j in range(len(d["student_id"])):
#         # print(d[i][j])
#         if d[i][j]==None:
#             c.append(j)

# for i in d.keys():    
#     for t in c:
#         del d[i][t]


# # print(c)
# print(df)

# k=5
# z=0
# nums = [0,4]
# # nums = [6,3,3,2]
# nums= sorted(nums)
# print(nums)
# min=0
# max=0
# for i in range(k):
#     for j in range(len(nums)):
#         if j<len(nums):
#             nums[j]=nums[j]+k
#             nums[j+1]=nums[j]+z
#             if nums[j]>0:
#                 d=nums[j]*nums[j+1]
            



# nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# nums = [[1,2,3],[4,5,6]]
# nums =[[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
# nums = [[25,44,47,42,43,10],[40,10,8,30,5,23],[36,10]]
# d= []
# c=[]

# for i in nums:
#     d.extend(i)



# for ind,val in enumerate(d):
#     if d.count(val)==len(nums):
#         c.append(val)
#         if c.count(val)>1:
#             c.remove(val)

        

# nums = c
# print(nums)
# # 
# for i in range(len(d)):
#     if d.count(d[i])!=len(nums):
#         d.remove(d[i])
      

# print(d)

# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         if nums.count(nums[i][j])==3:
#             print(nums[i][j])




# num = "6777133339"
# # num = "42352338"
# # num = "101010"
# c=''
# d=[]
# for i in range(len(num)):
#     if i<len(num)-2:
#         if num[i]==num[i+1]==num[i+2]:
#             c+=num[i]
#             c+=num[i+1]
#             c+=num[i+2]
#             if len(c)==3:
#                 d.append(c)
#         else:
#             c=''



# if d:
#     print(max(d))
# else:
#     d=""
#     print(d)



# nums = [2,3,4,3,4]
# nums = [4,5,6]
# nums=[31,32,31,32,33]               
# ans= [1,-1,0]

# for i in nums:
#     for j in nums:
#         if i!=j:
#             if  not i-j in ans:
#                 nums.remove(i)
#                 print(nums)
#                 break
#     else:
#         f=False

# print(nums)



# for i in range(len(nums)):
#     if i<len(nums)-2:
#         if nums[i+1]-nums[i]==1:
#             if nums[i+2]-nums[i-1]==-1:
#                 f = True

#             else:
#                 nums.remove(nums[i])






# nums = [3,-1,-5,2,5,-9]
# # nums = [-4,-5,-4]
# while len(nums)>0:
#     n=nums[0]
#     d=0
#     for j in nums:
#         if j!=n:
#             print(n*j)
#             n=n*j
#             if n>d:
#                 d=n
#     if len(nums)>2:        
#         nums.remove(nums[1])
        
    # print(d)



#HackerRank

#################################SOLVED######################################


#Sample Task
# n = int(input("your limit is: "))

# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         print ("FizzBuzz")
#     elif i%3==0 and i%5!=0:
#         print("Fizz")
#     elif i%3!=0 and i%5==0:
#         print("Buzz")
#     else:
#         print(i)

# #################################SOLVED######################################


# #2.Python:String Transformation HackerRank


# #################################SOLVED######################################


# sentence = "CoOL dog"
# sentence = "BA CC Df"

# d= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# f = []

# j= sentence.split(' ')

# print(j)
# for i in range(len(j)):
#     f.append([])
#     for z in range(len(j[i])):
#         f[i]+=j[i][z]


            

# for i in range(len(f)):
#     for z in range(len(f[i])):
#         if z!=0:
#             for ind1,val1 in enumerate(d):
#                 if f[i][z].lower()==val1:
#                     if ind1>d.index((f[i][z-1]).lower()):
#                         f[i][z]=f[i][z].upper()

#                     elif ind1<d.index((f[i][z-1]).lower()):
#                         f[i][z]=f[i][z].lower()


# a=''
# for i in range(len(f)):
#     if i!=0:
#         a+=' '
#     for z in range(len(f[i])):
#         a+=f[i][z]

# print(f)
# print(a)

#################################SOLVED######################################


            





#Vowel Substring HackerRank

# s="caberqiitefg"
# z=[]

# for i in s:
#        z.append(i)

# vowels = {'a','e','i','o','u'}
# f=''
# k=5
# max = 0
# coun = 0

# m=[]
# vowc=[]

# for i in range(len(z)):
#        if len(z)>=k:
#         for i in vowels:
#             if i in z[0:k]:
#                 coun+=z[0:k].count(i)
#                 #  m.append(z[0:k])
#                 print(coun)
#                 print(z[0:k])
#                 z.remove(z[0])
                
#         coun=0
                    


# print(m)
# print(max)
# print(max)             


#2680. Maximum OR        



# a=0
# b=0
# d=[]


# print(32|1|2)
# print(8|4|2)
# print(8|1|8)


# a=0
# b=0
# d=[]

# for ind1,val1 in enumerate(nums):
#     a=(val1*2)*k
#     # print(a)
#     b=sum(nums)-val1
#     # print(b)
#     d.append(a|b)
#     b=0

# print(max(d))

# class Solution:

#     def __init__(self,nums,k):
#          self.nums=nums
#          self.k=k

#     def maximumOr(self):
#         a=0
#         b=0
#         d=[]

#         for ind1,val1 in enumerate(nums):
#                 a=val1*(2**k)
#                 # print(a)
#                 b=sum(nums)-val1
#                 # print(b)
#                 d.append(a|b)
#                 b=0

#         return max(d)


# nums=[98,54,6,34,66,63,52,39,62,46,75,28,65,18,37,18,97,13,80,33,69,91,78,19,40]
k = 1      
nums = [12,9]
# myobj= Solution(nums,k)

# print(myobj.maximumOr())
 
# print(392 | 1183)



# a=0
# b=0
# c=0
# d=[]

# for ind1,val1 in enumerate(nums):
#     a=val1*(2**k)
#     for i in range(len(nums)):
#         if i!=ind1:
#             c=a|val1
#             print(c)
#             c=0



# print(max(d))



# houses = [1,2,3,4]
# heaters = [1,4]
# c=[]

# houses = [1,2,3]
# heaters = [2]


# houses = [1,5]
# heaters = [2]

# for ind1,val1 in enumerate(houses):
#         if val1 not in heaters:
#             c.append(val1)

# a=(max(heaters)-max(c))
# b=(min(c)-min(heaters))

# if a<0:
#       a=a*-1
# elif b<0:
#       b=b*-1

# print(a)



# b=['0100','1110','0010']
# f=False
# c=0
# for ind1,val1 in enumerate(b):
#     for ind2,val2 in enumerate(b):
#             if val1!=val2:
#                 for j in range(len(val1)):
#                     for d in range(len(val2)):
#                         if j==d and val1[j]!=val2[d]: 
#                                         f=True
#                 c+=1

# print(c)


# nums = [4,14,2]
# d=[]


# for i in nums:
#     binary_digits = []
#     while i > 0:
#         binary_digits.append(str(i % 2))
#         i //= 2

#     binary_digits.reverse()
#     d.append(binary_digits)


# for i in d:
#     if len(i)<4:

#         for j in range(4-len(i)):
#             i.reverse()
#             i+='0'
#             i.reverse()

# g=[]
# z=''

# for i in d:
#     for j in range(len(i)):
#         z+=i[j]
#     g.append([z])
#     z=''

# h=[]
# for i in g:
#     h.extend(i)
# print(h)

# f=False
# c=0
# for ind1,val1 in enumerate(h):
#     for ind2,val2 in enumerate(h):
#             if val1!=val2:
#                 for j in range(len(val1)):
#                     for d in range(len(val2)):
#                         if j==d and val1[j]!=val2[d]: 
#                                         f=True
#                 c+=1

# print(c)



# 315. Count of Smaller Numbers After Self
# nums = [5,2,6,1]
# nums = [-1]
# nums = [-1,-1]
# c=0
# d=[]
# f=False
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]>nums[j]:
#             f=True
#             c+=1
#     d.append(c)
#     c=0

    
# print(d)
            


# 342. Power of Four     ########SOLVED##########

# n=15

# while n>1:
#     n=n/4

#     print(n)

# if n==1:
#     print(True)
# else:
#     print(False)

########SOLVED##########




# nums = [1,2,3,4,5]
# nums = [5,4,3,2,1]
# nums = [2,1,5,0,4,6]
# normal=[]

# for i in range(len(nums)):
#         if i<len(nums)-2:
#                 if nums[i]<nums[i+1]<nums[i+2]:
#                     normal.append(True)
#                     print(nums[i],nums[i+1],nums[i+2])
#                 else:
#                     print(False)
        
# if normal:
#       print(True)

# class Solution:
#     def increasingTriplet(self, nums):
#         normal=[]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if i<len(nums)-2:
#                             if nums[i]<nums[j]<nums[k]:
#                                 normal.append(True)

#         if normal:
#             return(True)
#         else:
#               return(False)
                        

# # nums = [1,2,3,4,5]
# # nums = [5,4,3,2,1]
# # nums = [2,1,5,0,4,6]
# nums=[20,100,10,12,5,13]


# myobj= Solution()
# print(myobj.increasingTriplet(nums))


# min_val = float('inf')
# second_min_val = float('inf')

# nums = [2,1,5,0,4,6]
# nums = [20, 100, 10, 12, 5, 13]
# # nums = [5,4,3,2,1]



# for num in nums:
#     if num <= min_val:
#         min_val = num
#         print(min_val,"min")
#     elif num <= second_min_val:
#         second_min_val = num
#         print(second_min_val,"second min")

#     else:
#         print(True)



# 326. Power of Three

# n=0

# while n>1:
#     n=n/3

# if n!=1:
#     print(False)
# else:
#     print(True)



# 2024. Maximize the Confusion of an Exam

# answerKey = "TTFF"
# answerKey = "TFFT"
# # answerKey = "TTFTTFTT"
# answerKey1=[]
# for i in answerKey:
#     answerKey1.append(i)

# j=['']

# f=set(answerKey1)
# z=(list(f))

# how=0

# for i in z:
#     t=answerKey1.count(i)
#     if t>how:
#         how=t
#         j[0]=i


# k=1

# q=[]

# for i in range(len(answerKey1)):
#     if j[0]!=answerKey1[i]:
#         q.append(answerKey1[i])


# p=set(q)
# v=list(p)

# if v and v[0] in answerKey1:
#     for i in range(k):
#         b=answerKey1.index(v[0])
#         answerKey1[b]=j[0]



# print(answerKey1)
# n=1
# m=1

# for i in range(len(answerKey1) - 1): 
#     if answerKey1[i] == answerKey1[i + 1]:
#         n += 1
#         m = max(n, m)
#     else:
#         n = 1


#####################################################################1991. Find the Middle Index in Array (Easy)


# class Solution:
#     def findMiddleIndex(self, nums):
#             for i in range(0,len(nums)):
#                 if sum(nums[:i])==sum(nums[i+1:]):
#                     return i            
#             else:
#                 return -1
        

####################



# a=''
# digits = [4,3,2,1]
# for i in digits:
#     a+=str(i)

# b=int(a)+1
# tot=[]

# print(b)

# for i in str(b):
#     tot.append(int(i))
# print(tot)


##########################################33#####498. Diagonal Traverse
# from collections import defaultdict

# matrix = [[1,2,3],[4,5,6],[7,8,9]]


# d= defaultdict(list)
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         d[i+j].append(matrix[i][j])


# res=[]

# for key,val in d.items():
#     if key%2==0:
#         res.extend(d[key][::-1])
#     else:
#         res.extend(d[key])

# print(res)


####################################################2024#############################################################################################################
####################################################2024#############################################################################################################
####################################################2024#############################################################################################################
####################################################2024#############################################################################################################
####################################################2024#############################################################################################################
####################################################2024#############################################################################################################
####################################################2024#############################################################################################################
####################################################2024#############################################################################################################



########################################################## 54. Spiral Matrix


# class Solution:
#     def spiralOrder(self, matrix):
#         if not matrix:
#             return []

#         top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
#         result = []
        
#         while left < right and top < bottom:
#             for i in range(left, right):
#                 result.append(matrix[top][i])
#             top += 1
            
#             for i in range(top, bottom):
#                 result.append(matrix[i][right-1])
#             right -= 1
            
#             if not (left<right and top<bottom):
#                 break

#             for i in range(right-1,left-1,-1):
#                 result.append(matrix[bottom-1][i])
#             bottom-= 1

#             for i in range(bottom-1,top-1,-1):
#                 result.append(matrix[i][left])
#             left+=1


#         return result
    


#################################################240. Search a 2D Matrix II


# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 5

