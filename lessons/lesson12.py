
"classlarda inheritance"


class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def makeSound(self):
        return "Nothing"


class Cat(Animal):
    ...

    def __init__(self, name, color, gender):
        super().__init__(name=name, color=color)
        self.gender = gender
    
    def makeSound(self):
        return f"{self.name}--{self.color}---{self.gender}---Miao"

animal=Animal('monkey','brown')
cat1=Cat(animal.name,animal.color,'it')

print(cat1.makeSound())

# cat1=Cat()
# class Wild:

#     def __init__(self, kill_count, area):
#         self.kill_count = kill_count
#         self.area = area


# class BengalCat(Cat, Wild):

#     def __init__(self, name, color, gender, kill_count, area, age=None):
#         super().__init__(name, color, gender)
#         self.kill_count = kill_count
#         self.area = area
#         self.age = age



# cat2 = BengalCat(name="Yuri", color="sari", gender="others", kill_count=30 , area="Samaxi", age=40)


# print(cat2.makeSound(), cat2.age)
# print(cat2.kill_count, cat2.area)



# def say_hello():
#     return "Hello World"


# func1 = say_hello()
# print(func1)


# say_hello = lambda x, y: x + y

# func1 = say_hello(x=10, y=30)

# print(func1)


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

"""
TASK 1:

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""



# class Solution:

#     def __init__(self, ransomNote, magazine):
#         self.ransomNote = ransomNote
#         self.magazine = magazine
    

#     def canConstruct(self):
#         set_note = set(self.ransomNote)
#         for elem in set_note:
#             if self.ransomNote.count(elem) > self.magazine.count(elem):
#                 return False
#         return True


# obj1 = Solution(ransomNote="ab", magazine="abb")
# # obj1 = Solution(ransomNote="aa", magazine="ab")
# # obj1 = Solution(ransomNote="a", magazine="b")
# print(obj1.canConstruct())


"""
Task2:


Ex.1: s="coders", t="derscou" --> "u"
Ex.2: s="python", t="pytlnoh" --> "l"
Ex.2: s="django", t="donajgr" --> "r"
"""


# class FindElem:

#     def __init__(self, t, s):
#         self.s = s
#         self.t = t
    

#     def find_additional_element(self):
#         # return set(self.t) - set(self.s)
#         for elem in self.t:
#             if self.s.count(elem) != self.t.count(elem):
#                 return elem
#         return True


# s="coders"; t="derscou"
# s="python"; t="pytpnoh"
# # s="django"; t="donajgr"

# obj1 = FindElem(s=s, t=t)

# print(obj1.find_additional_element())


"""
Task 3:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


# class Solution:

#     def __init__(self, num_list):
#         self.num_list = num_list
    

#     def get_new_list(self):
#         # result = ""
#         # for i in self.num_list:
#         #     result += i
#         return list(str(int("".join(str(i) for i in self.num_list)) + 1))


# num_list=[1,2,3]
# num_list=[4,2,3,1]
# num_list=[9]

# obj1 = Solution(num_list=num_list)

# print(obj1.get_new_list())