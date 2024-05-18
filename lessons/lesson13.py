"""
Task 1
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


# class Solution:

#     def __init__(self, nums):
#         self.nums = nums
    

#     def find_average(self):
#         return len(self.nums)/2
    

#     def majorityElement(self):
#         nums_set = set(self.nums) # --> {1, 2}

#         for i in nums_set:
#             if self.nums.count(i) > self.find_average():
#                 return i
#         return "None of them"



# obj1 = Solution(nums=[2,2,1,1,1,2,2])
# print(obj1.majorityElement())


# nums=[2,2,1,1,1,2,2]
# print(nums.count(2))


"""
Task 2:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""



class Solution:

    def containsNearbyDuplicate(self, nums, target):
        duplitace_numbers = [i for i in set(nums) if nums.count(i) > 1]
        for elem in duplitace_numbers:
            for i in range(len(nums)):
                # if i == len(nums)-1:
                #     continue

                try:
                    first_index = nums.index(elem, i)
                except:
                    continue

                try:
                    second_index = nums.index(elem, i+1)
                except:
                    continue

                if second_index - first_index == k:
                    return True
        return False



nums = [1,2,3,1]; k = 3
nums = [1,0,1,1]; k = 1
nums = [1,2,3,1,2,3]; k = 2

obj = Solution()

print(obj.containsNearbyDuplicate(nums=nums, target=k))