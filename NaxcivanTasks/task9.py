# nums = [3,2,3,5,6,4]

# dict={num:nums.count(num) for num in nums }
# print(dict)





# 506. Relative Ranks


#bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır. Biz isə onların topladığı xallara görə
#neçənci yeri tutduğunu print etməliyik. Misal üçün bizə xallar verilib. xallar = [5,3,4,2,1].
#Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq. yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']
#Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də o pozulmuş sıraya uyğun sıralanacaq və nəticə 
#düzgün olmayacaq.(taskı daha da asanlaşdırmaq üçün hərkəsin  xalı müxtəlif olacaq. Eyni xala sahib 2 şəxs olabilməz)

score = [8,3,4,5,1]

def Qualify(score:list):
    them=list(reversed(sorted(score)))
    medals=['Gold Medal','Silver Medal','Bronze Medal','4','5']
    mydict={val:medals[ind] for ind,val in enumerate(them)}

    return [mydict[i]for i in score]


print(Qualify(score))