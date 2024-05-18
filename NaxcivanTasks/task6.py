import random
import math

import time






# def TakeNumbers():
#     mylist=[random.randrange(20,50) for i in range(5)]
#     newlist=[int(math.pow(i,2)) for i in mylist if i%2==0]
#     time.sleep(2)
#     return newlist

# print(TakeNumbers())



# def FindNumber():
#     choosenNumber=random.randint(1,40)
#     check=True
#     luck=6
#     while check:
#         yourNumber=int(input("guess the number: " ))
#         time.sleep(2)

#         if yourNumber==choosenNumber:
#             check=False
#             print('Congrats,You find the number!')
        
#         elif luck==0:
#             print(f'game over. Number was {choosenNumber}')
#             check=False

#         elif choosenNumber>yourNumber:
#             print("it's bigger number than you thought")

#         elif choosenNumber<yourNumber:

#             print("It's lower number than you thought")
        
#         luck-=1



# print(FindNumber())