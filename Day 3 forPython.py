# nums = [4,1,4,0,3,5]
# c = []
# for ind,val in enumerate(nums):
#     b =  (max(nums)+min(nums))/2
#     nums.remove(max(nums))
#     nums.remove(min(nums))
#     if len(nums)==2:
#         c.append(sum(nums)/2)
#     c.append(b)


# for ind1,val1 in enumerate(c):

#     if c.count(val1)>1:
#         c.remove(val1)
#         print(c)
#         print(len(c))
#     elif len(c)==1:
#         print(len(c))



# # names = ["Mary","John","Emma"]
# names = ["Alice","Bob","Michael","Salman"]
# # heights = [180,165,170]
# heights = [155,185,150,190]
# sorted_heights = sorted(heights)
# sorted_heights.reverse()
# print(sorted_heights)

# d= []
# for ind1,val1 in enumerate(sorted_heights):
#     for ind2,val2 in enumerate(heights):
#         if val2 == val1:
#                 d.append(names[ind2])

# print(d)

nums ='4325'
e = []
for ind1,val1 in enumerate(nums):
     for  ind2,val2 in enumerate(nums):
          if len(nums)>2:
            for ind3,val3 in enumerate(nums):
                    if len(nums)>3:
                        for ind4,val4 in enumerate(nums):
                            if val1!=val2 and val1!=val3 and val2!=val3 and val1!=val4 and val2!=val3 and val3!=val4 and val2!=val4:
                                d =  int(val1+val2)+int(val3+val4)
                                e.append(d)


print(min(e))


