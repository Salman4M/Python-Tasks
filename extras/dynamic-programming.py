def fibonacci(n):
    now=0
    previous=1
    b=0
    if n<=2:
        return 1
    else:
        for i in range(2,n):
            b=now+previous
            now=previous
            previous=b
        return fibonacci(n-1)+fibonacci(n-2)

n=7
print(fibonacci(n))



############### improving fibonacci logic by saving it in dictionary
'''memoization: In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs 
by storing the results of expensive function calls to pure functions and returning the cached result when the same inputs occur again.'''

# def fibonacci(n,memo={}):
#     now=0
#     previous=1
#     b=0

#     if n<=2:
#         return 1
#     else:
#         for i in range(2,n):
#             if n in memo:
#                 return memo[n]
#             b=now+previous
#             now=previous
#             previous=b
#     memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
#     return memo[n]

# n=50
# print(fibonacci(n))


########################################gridTraveler
#for example: it is given 2 cordinates for grid which first one is count of row second
# one is count of column. So you have to go bottom right of the grid by only using down 
#or right directions to get there. How many possible ways are there?
# Let's say gridTraveler(2,3)  .It means we have 2 rows and 3 columns. So when you go
#down you decrease number of rows. It looks like (1,3). If you go down again row equals 
# to 0 and it looks like (0,3) and it means 0 posibilities in this condition,
#Because you didn't make it to bottom right.But if you go to the right in (1,3)
# you decrease number of column and it looks like (1,2) and you still can go to down
# or right . if you go to down it will be (0,2) and it's not bottom right.So it is equal
# to zero. What if you got to right instead of down it will (1,1) and it equals to 1
#posibility which is bottom right. So you have to calculate sub cordinations before get
# result of given cordinates.


# def gridTraveler(m,n):
#         if m==1 and n==1:
#             return 1
#         elif m==0 or n==0:
#             return 0

# #gridTraveler(a,b)=gridTraveler(b,a)
#         return gridTraveler(n-1,m)+gridTraveler(n,m-1)

# n,m=2,3
# n,m=18,18


# print(gridTraveler(n,m))


############### improving gridTraveler logic by saving it in dictionary

#gridTraveler(a,b)=gridTraveler(b,a)

# def gridTraveler(m,n,memo={}):
#         key = str(m)+','+str(n)
#         if key in memo:
#              return memo[key]
#         if m==1 and n==1:
#             return 1
#         elif m==0 or n==0:
#             return 0
#         memo[key]= gridTraveler(n-1,m,memo)+gridTraveler(n,m-1,memo)

#         return memo[key]

# # n,m=2,3
# n,m=18,18

# print(gridTraveler(n,m))



############################Memoization Recipe
#1. Make it work
#-visualize the problem  as a tree
#-implement the tree by using recursion
#-test it
#2.Make it efficient
#-add a memo object
#-add a base case to return memo values
#-store return values into memo


# def canSum(targetSum,numbers,memo={}):
#     if targetSum in memo:
#           return memo[targetSum]
#     if targetSum>=0:
#         if targetSum==0:
#                 return True
#         for i in numbers:
#             remainder=targetSum-i      
#             if canSum(remainder,numbers)==True:
#                     memo[targetSum]=True
#                     return True
#     memo[targetSum]=False
#     return False
        

# targetSum=300
# numbers=[7,14]
    
          
# print(canSum(targetSum,numbers))


#now we want to bring combinations that can get targetSum.


######   *  -spread operator
# def HowSum(targetSum,numbers,memo={}):
#       if targetSum in memo:
#             return memo[targetSum]

#       if targetSum==0:
#             return []
#       if targetSum<0:
#             return None
      
#       for num in numbers:
#             remainder = targetSum-num
#             remainderResult=HowSum(remainder,numbers,memo)
#             if remainderResult!=None:
#                   memo[targetSum]= [*remainderResult,num]
#                   return memo[targetSum]

#       memo[targetSum]=None      
#       return memo[targetSum]
            
# targetSum=300
# numbers=[7,14]


# print(HowSum(targetSum,numbers))

      
########################################Best Sum
#this time we try finding shortest combination to get targetSum.




# def BestSum(targetSum,numbers):
#     shortestCombination=None
#     if targetSum==0:
#         return []
#     if targetSum<0:
#         return None
    
#     for num in numbers:
#         remainder=targetSum-num
#         remainderCombination= BestSum(remainder,numbers)
#         if remainderCombination!=None:
#             combination = [*remainderCombination,num]
#             if shortestCombination==None or len(shortestCombination)>len(combination):
#                 shortestCombination=combination


#     return shortestCombination



# print(BestSum(7,[5,3,4,7]))
# print(BestSum(8,[2,3,5]))
# print(BestSum(8,[1,4,5]))
# print(BestSum(100,[1,2,5,25]))





### by memoization

# def BestSum(targetSum,numbers,memo={}):
#     if targetSum in memo:
#         return memo[targetSum]
#     if targetSum==0:
#         return []
#     if targetSum<0:
#         return None
      
#     shortestCombination=None


#     for num in numbers:
#         remainder=targetSum-num
#         remainderCombination= BestSum(remainder,numbers,memo)
#         if remainderCombination!=None:
#             combination = [*remainderCombination,num]
#             if shortestCombination==None or len(shortestCombination)>len(combination):
#                 shortestCombination=combination


#     memo[targetSum]= shortestCombination
#     return memo[targetSum]



# print(BestSum(7,[5,3,4,7]))
# print(BestSum(8,[2,3,5]))
# print(BestSum(8,[1,4,5]))
# print(BestSum(100,[1,2,5,25]))




###############################################CanConstruct
# in this problem We have to make target word from given words in wordBank


# target = "abcdef"
# wordBank = ["ab","abc","cd","def","abcd"]


# for i in wordBank:
#     if target.startswith(i):
#         print(i)
#         target=target.replace(i,'')
#         if target=='':
#             print(True)

# def canConstruct(target,wordBank):
#    if target=='':
#       return True
   
#    for i in wordBank:
#         if target.startswith(i):
#             newword=target.replace(i,'')
#             if canConstruct(newword,wordBank)==True:
#                 return True
   
#    return False
            


# target = "abcdef"
# wordBank = ["ab","abc","cd","def","abcd"]

# print(canConstruct(target,wordBank))
# print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))



#by memoization

# def canConstruct(target,wordBank,memo={}):
#    if target in memo:
#        return memo[target]
#    if target=='':
#       return True
   
#    for i in wordBank:
#         if target.startswith(i):
#            newword=target.replace(i,'')
#            if canConstruct(newword,wordBank)==True:
#                 memo[target]=True
#                 return memo[target]
            
#    memo[target]=False
   
#    return memo[target]


# print(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))



################################Now  we count how many possibly ways to get target word

# def countConstruct(target,wordBank):
#    n=0
#    if target=='':
#       return True

#    for i in wordBank:
#         if target.startswith(i):
#             newword=target.replace(i,'')
#             if countConstruct(newword,wordBank)==True:
#                 n=n+1
                
#    if n==0:
#        return 0
#    else:
#        return n



# target = "abcdef"
# wordBank = ["ab","abc","cd","def","abcd"]

# print(countConstruct(target,wordBank))
# print(countConstruct("purple",["purp","p","ur","le","purpl"]))


# print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))



## by memoization

# def countConstruct(target,wordBank,memo={}):
#    if target in memo:
#        return memo[target]
#    n=0
#    if target=='':
#       return True

#    for i in wordBank:
#         if target.startswith(i):
#             newword=target.replace(i,'')
#             if countConstruct(newword,wordBank)==True:
#                 n=n+1
#                 memo[target]=countConstruct(newword,wordBank)
                
#    memo[target]=n

#    return memo[target]



# target = "abcdef"
# wordBank = ["ab","abc","cd","def","abcd"]

# print(countConstruct(target,wordBank))
# print(countConstruct("purple",["purp","p","ur","le","purpl"]))


# # print(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]))
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee","eeeeee"]))




#######################Bring back all the combinations that can create target word


# def all_construct(target, word_bank):
#     if target == '':
#         return [[]]
    
#     result = []

#     for word in word_bank:
#         if target.startswith(word):
#             suffix = target[len(word):]
#             suffix_ways = all_construct(suffix, word_bank)
#             target_ways = [ [word] + way for way in suffix_ways ]
#             result.extend(target_ways)
    
#     return result

# print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))


##by memoization

# def all_construct(target, word_bank,memo={}):
#     if target in memo:
#         return memo[target]
#     if target == '':
#         return [[]]
    
#     result = []

#     for word in word_bank:
#         if target.startswith(word):
#             suffix = target[len(word):]
#             suffix_ways = all_construct(suffix, word_bank)
#             target_ways = [ [word] + way for way in suffix_ways ]
#             result.extend(target_ways)    
    
#     memo[target]=result
#     return memo[target]

# print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))











######################################              TABULATION              ################################################


#fibonacci  by tabulation

# def fib(n):
#     if n <= 1:
#         return n
    
#     table = [0] * (n + 2)  # Because when we do i+2 it has to be equal or lower than n. so it has to be n+2 not n+1.
#     table[1] = 1
    
#     for i in range(n):
#         table[i + 1] += table[i]
#         table[i + 2] += table[i]
    
#     return table[n]
# #### you can return table and find out what is going on inside of table
# print(fib(6))
# print(fib(8))
# print(fib(55))




##################grid traveler by tabulation

# ### in this example let's say tables[i][j]=1 . So tables[i+1][j]+=tables[i][j] and tables[i][j+1]+=tables[i][j]
# def gridTraveler(m,n):
#     tables=[]
#     for i in range(n+1):
#         tables.append(list(map(int,[0]*(m+1))))
#     tables[1][1]=1

#     for i in range(n + 1):
#         for j in range(m + 1):
#             if i + 1 <= n:
#                 tables[i + 1][j] += tables[i][j]
#             if j + 1 <= m:
#                 tables[i][j + 1] += tables[i][j]

#     return tables[n][m]


# print(gridTraveler(3,3))

##in in the tabulation 
    
