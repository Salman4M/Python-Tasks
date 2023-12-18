# 1.	İstifadəcidən 10 ilə 99 arasında bir ədəd alın və rəqəmlərini print etdirn.
# input: 89         output:8 9
# mynumb = input()
# for i in mynumb:
#     print(i, end =" ")

# 2.	Istifadeciden eded alin,ededin  bolenlerini print etdirin.
# input: 6  	output:1 2 3 6
# input: 25 	output: 1 5 25
# input: 20    output: 1 2 4 5 10

# numbs = int(input("my number: "))
# for i in range(1,numbs):
#    if numbs % i   == 0:
#       print(i)


# 3. Bir n ədədi daxil edilir və 1-dən n-ə qədər olan ədədləri aşağıdakı formada print etdirin.
#  İnput:
# 3
# Output:
# 123

# n = int(input("n is: "))

# for i in range(1,n+1):
#     print(i,end = " ")


# 4. m natural ədədi n ədədinin o zaman bərabər böləni adlanır ki, n-nin m-ə bölünməsindən alınan tam və qalıq bərabər olsun.
#  Daxil edilmiş n natural ədədinə görə onun bərabər bölənlərini ekrana yazdirin.
# İnput: 20                        Output: 9 19
# m/n = x(x)
# (n*x)+x = m

# n = int(input("our n is: "))

# for i in range(n,0,-1):
#     if int(n % i) == int(n / i):
#         print(i)

   


# 5. Ashagidaki neticeni nested for ile ekrana yazdirin.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1,6):
#         for j in range(i):
#             print(i, end=" ")
#         print("")

# 6. Ashagidaki neticeni nested for ile ekrana yazdirin.
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end = " ")
#     print("")


# 7.Ashagidaki neticeni nested for ile ekrana yazdirin.
# A
# B C
# D E F
# G H I J
# K L M N O

# my_list = ["A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O']
# # for i in range(0,6):
# #     for j in my_list[i]:
# #         print(j, end = " ")
# #     print("")

# for i in my_list:
#     for j in my_list:
#         print(i,end = " ")
    
#     print("")
# 8.Istifadeciden eded alin,aldiginiz ededin sayi qeder onluq mertebelere yukseltsin
# 1
# 10
# 100
# 1000
# 


# # 9. 1 ile 100 arasindaki tek ededlerin cemini tapin.
# a = 0

# for i in range(1,101,2):
#     print(i)


# for i in range(1,101):
#     if i%2 !=0:
#         a+=i
#         print(a)

# 10. 1 ile 100 arasinda sade ededleri ekrana yazdirin.
 
a = range(100,1,-1)
for i in range (1,100):
    for b in a:
      if i % b == 0:
         print


# 11. 1-dən 100-ə qədər ədədlərdən 5-ə bölünənləri print etdirin.(while istifade edin)

# 12. 100-dən 1-ə qədər ədədləri print etdirin

# 13. 100 ve 200 arasinda hem 2-ye hemde 3-e tam bolunen ededleeri

# for i in range(100,201):
#     if i%2==0 and i%3==0:
#         print(i)
# 14. İstifadəçi 2 ədəd daxil etsin və bu 2 ədəd arasındaki sadə ədədlərin cəmini tapın.
# 15.Tutaq k, n=13 istifadəçi 13 daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə tapdığını print etsin.
# num = 20
# my_num = int(input("my number is: "))
# cehd = 0

# while True:
#     my_num
#     cehd+=1
#     if num == my_num:
#         print("Congrats" + cehd + "You find it in 5 times")
#     break

