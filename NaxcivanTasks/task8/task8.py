# # 1) taskınız ilk olaraq bir texti faylı yaradıb içərisinə istədiyiniz bir cümlə yazırsınız .
# # 2) daha sonra həmin textin ilk sətrindəki bütün hərfləri böyük hərflərə çeviririk və bu sözləri başqa 
# # bir text faylı yaradıb onun içərisində yazırıq.


# file=open('NaxcivanTasks/task8/our.txt','r')
# # file.write
# # print(file.writable())

# # file=open('NaxcivanTasks/task8/our.txt','r')

# # print(file.read())

# # with open('NaxcivanTasks/task8/our.txt') as newfile:

# #     print(newfile)


# # with open("NaxcivanTasks/task8/our.txt") as my_file:
# #     print(my_file.read())

# with open("NaxcivanTasks/task8/our.txt", "w") as my_file:
#     my_file.write("Hello world ")
#     my_file.write("I hope you're doing well today ")
#     my_file.write("This is a text file")
#     my_file.write("Have a nice time")



# # with open("NaxcivanTasks/task8/our.txt","r") as my_file:
# #     for i in my_file:
# #         print(i)
#         # print(my_file.read())


# # with open("NaxcivanTasks/task8/our.txt",'a') as my_file:
# #     my_file.write('\ntrying append')

# # print(file.read())

# with open("NaxcivanTasks/task8/our.txt","r") as my_file:
#     words= ' '.join(word.capitalize() for word in my_file.read().split())

# with open("NaxcivanTasks/task8/newfile.txt","w") as my_file:
#     my_file.write(words)




# with open("NaxcivanTasks/task8/newfile.txt",'r') as my_file:
#     print(my_file.read())

# with open('NaxcivanTasks/task8/examplesss.txt', 'w') as file:
# 	file.write('This will overwrite existing content')
# 	file.seek(0) # Move the pointer to the beginning
# 	# content = file.read()
# 	# print(content)



# with open('NaxcivanTasks/task8/text.txt', 'w+', encoding='utf-8') as file:
#     file.write('salam azerbaycan, salam naxcivan, salam culfa\n')
#     file.write('salam backend, salam python, salam open\n')
#     file.seek(0)
#     print(file.read())
#     content = file.readline().upper() + file.read()


# with open('NaxcivanTasks/task8/text.txt', 'w+', encoding='utf-8') as file:   
#     file.write(content)
#     file.seek(0)
# with open('NaxcivanTasks/task8/folder.txt', 'w', encoding='utf-8') as new_file:
#     new_file.write(content)

# with open('NaxcivanTasks/task8/text.txt', 'r', encoding='utf-8') as new_file:
#     print(new_file.read())

# with open('NaxcivanTasks/task8/example.txt', 'r') as file:
# 	print(file.read())



with open("esas.txt","w+",encoding="UTF-8") as second:
    second.write('salam necesiniz')

with open("second.txt","w+",encoding="UTF-8") as second:
    esas=open("esas.txt","r",encoding="UTF-8")
    second.write(esas.readline().upper())
    esas.close()


