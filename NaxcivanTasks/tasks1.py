#### For loop , while ,if else statement

# 1). Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:


# list=[]
# for i in range(5):
#    inputs=input('your answer: ')
#    list.append(inputs)
# list.sort()

# print(list)


# 2). User hansi fiquru almaq isteyirse onu daxil edir. (duzbucaq, kvadrat ve ucbucaq).
# Eger bu iki fiqurdan hansinisa daxil ederse ondan fiqura gore terefleri istenilir. Daxil edilen tereflere gore fiqurun tipini cavab olaraq ekrana veririk.
# Meselen ucbucaqli yazdi inputda , daha sonra userden 3 teref istenilir.  3 terefide daxil etdikden sonra meselen 2 teref eynidirse beraberyanli 
# ucbucaq cavabini cixardir.

# sides=[]

# figure=input('type of figure: ')

# if figure=='dordbucaqli':
#    for i in range(4):
#         side=int(input(f'side {i+1}: '))
#         if side!=0:
#           sides.append(side)

#         else:
#            print("length or width can't be 0")
#            break
   
#    if len(set(sides))==1:
#       print('this is Kvadrat')
#    elif len(set(sides))==2:
#        print('this is Duzbucaqli')
#    elif len(set(sides))==4:
#       print("her hansi dordbucaq")
#    else:
#       print('cant be square')

# elif figure == 'ucbucaqli':
#    for i in range(3):
#       side=int(input(f'side {i+1}: '))
#       if side!=0:
#         sides.append(side)
#       else:
#         print("length of side can't be 0")
#         break

#    if len(set(sides))==1:
#        print('beraberterefli')

#    elif len(set(sides))==2:
#        print('beraberyanli')

#    else:
#        print('ucbucaq')

# else:
#    print('none of them ')
  


# 3.)Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
# tapdığını print etsin. while istifade edin

# num = int(input('choosen number: '))
# cehd = 0
# check=True
# while check:
#     wInput= int(input('guess the number: '))
#     cehd+=1
    
#     if num == wInput:
#         check=False
#         print(f'you find the number in {cehd} tries')


# # 4). 1 ile 100 arasinda sade ededleri print edin. (for loops)


# for i in range (2,50):
#    for b in range(2,i):
#         # print(i,b)
#       if i % b == 0:
#           break
#    else:
#        print(i)




# # #5)  Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir".    
# # Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü. 

# d='SDabahin xEyir hocam'
# a=d.lower()
# b=a.split()
# j={}

# for i in range(len(b)):
#     wordList=list(b[i])
#     wordList.sort()
#     print(wordList)
#     for j in range(len(d)):
#         if d[j].isupper() and d[j].lower() in wordList:
#             letter=d[j].lower()
#             wordList[wordList.index(letter)]=letter.upper()         
#     b[i]=''.join(wordList)

# print(b)





n = 13
i = 0
while True:
    k = int(input('RƏQƏM DAXİL EDİN: '))
    i += 1
    if k==13:
        print(f' SİZ {n} - Nİ {i} CƏHDDƏ TAPDINIZ.')
    elif(k < n):
        print(' ARTIRIN')
    elif (k > n):
        print('AZALDIN')







