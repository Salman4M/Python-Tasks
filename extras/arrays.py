# #########################33  Introduction to 2D Array

# Similar to a one-dimensional array, a two-dimensional array also consists of a sequence of elements. But the elements can be laid out in a rectangular grid rather than a line.


# def print_array(a):
#     for row in a:
#         for elem in row:
#             print(elem, end=" ")
#         print()

# if __name__ == "__main__":
#     print("Example I:")
#     a = [[0 for _ in range(5)] for _ in range(2)]
#     print_array(a)

#     print("\nExample II:")
#     b = [[1, 2, 3] + [0] * 2]
#     print_array(b)

#     print("\nExample III:")
#     c = [[1, 2, 3, 4, 5, 6, 7]]
#     print_array(c)

#     print("\nExample IV:")
#     d = [[1, 2, 3, 4], [5, 6] + [0] * 3, [7] + [0] * 4]
#     print_array(d)



###############################################498. Diagonal Traverse

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




