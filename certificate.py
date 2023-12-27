
# sentence=input()

# b=[]


# for i in sentence:
#     b.append(i)


# for i in range(len(b)):
#     if b[i].islower()==True:
#         b[i]=b[i].upper()
#     elif b[i].isupper()==True:
#         b[i]=b[i].lower()


# c=''
# for i in b:
#     c+=i
# c=c.split(' ')
# c=list(reversed(c))


# for i in c:
#     print(i,end=' ')


# modified_sentence = ''
# for char in sentence:
#     if char.islower():
#         modified_sentence += char.upper()
#         print(modified_sentence)
#     elif char.isupper():
#         modified_sentence += char.lower()
#         print(modified_sentence)

#     else:
#         modified_sentence += char  
#         print(modified_sentence)

# words = modified_sentence.split()
# reversed_sentence = ' '.join(reversed(words))
# print(reversed_sentence)
#####################################################


# def upper_lower_reverse_order(sentence):
#     modified_sentence = ''
#     for char in sentence:
#         if char.islower():
#             modified_sentence += char.upper()
#         elif char.isupper():
#             modified_sentence += char.lower()
#         else:
#             modified_sentence += char  
#     words = modified_sentence.split()
#     reversed_sentence = ' '.join(reversed(words))
#     return reversed_sentence

# sentence = input()


# print(upper_lower_reverse_order(sentence))
    # print(reversed_sentence)



######################################################second



# class VendingMachine:
#     def __init__(self,num_items,item_price):
#         self.num_items=num_items
#         self.item_price=item_price

#     def buy(self,req_items,money):
#         if self.num_items < req_items:
#             raise ValueError("Not enough items in the machine")

#         elif money < req_items * self.item_price:
#             raise ValueError("Not enough coins")

#         self.num_items -= req_items
#         return money - (req_items * self.item_price)

# num_items, item_price = map(int, input().split())


# vending_machine = VendingMachine(num_items, item_price)



# n = int(input())

# for _ in range(n):
#     req_items, money = map(int, input().split())
#     try:
#         change = vending_machine.buy(req_items, money)
#         print(change)
#     except ValueError as z:
#         print(z)



####
# num_items,item_price=input().split()
# num_items,item_price=int(num_items),int(item_price)
# n=int(input())

# for i in range(n):
#     req_items,money=input().split()
#     req_items,money=int(req_items),int(money)
    
#     if num_items>=req_items and money<req_items*item_price:
#             raise ValueError("Not enough coins")
    
#     elif num_items<req_items and money>=req_items*item_price:
#             raise ValueError("Not enough items in the machine")

#     elif  num_items>=req_items and money>=req_items*item_price:
#         num_items-=req_items
#         money=money-item_price*req_items
#         print(money)


