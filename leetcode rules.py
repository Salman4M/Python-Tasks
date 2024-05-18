# def printArray(a):
#     for row in a:
#         for element in row:
#             print(element, end=" ")
#         print()

# if __name__ == "__main__":
#     print("Example I:")
#     a = [[0] * 5 for _ in range(2)]
#     printArray(a)

#     print("Example II:")
#     b = [[1, 2, 3] + [0] * 2]
#     printArray(b)

#     print("Example III:")
#     c = [[1, 2, 3, 4, 5, 6, 7]]
#     printArray(c)

#     print("Example IV:")
#     d = [[1, 2, 3, 4], [5, 6] + [0] * 3, [7] + [0] * 4]
#     printArray(d)


########################################Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# class Solution:
#     def findDiagonalOrder(self, mat):
#         from collections import defaultdict

#         d= defaultdict(list)
#         for i in range(len(mat)):
#             for j in range(len(mat[i])):
#                 d[i+j].append(mat[i][j])


#         res=[]

#         for key,val in d.items():
#             if key%2==0:
#                 res.extend(d[key][::-1])
#             else:
#                 res.extend(d[key])

#         return res,d

# mat = [[1,2,3],[4,5,6],[7,8,9]]

# myobj=Solution()
# print(myobj.findDiagonalOrder(mat))




####################################################################  Pascal's Triangle

a=[[1]]
n=5

for i in range(n-1):
    addZero=[0]+a[-1]+[0]
    row=[]
    for j in range(len(a[-1])+1):########+1 o deməkdir ki növbəti sıranı almaq üçün olduğumuzun sıranın uzunluğunundan bir vahid böyük ədədi də istifadə etməliyik
        row.append(addZero[j]+addZero[j+1])
    a.append(row)
print(a)


