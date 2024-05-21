# 506. Relative Ranks


#bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır. Biz isə onların topladığı xallara görə
#neçənci yeri tutduğunu print etməliyik. Misal üçün bizə xallar verilib. xallar = [5,3,4,2,1].
#Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq. yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']
#Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də o pozulmuş sıraya uyğun sıralanacaq və nəticə 
#düzgün olmayacaq.(taskı daha da asanlaşdırmaq üçün hərkəsin  xalı müxtəlif olacaq. Eyni xala sahib 2 şəxs olabilməz)

score = [8,3,4,5,1]

def Qualify(score:list):
    medals=['Gold Medal','Silver Medal','Bronze Medal','4','5']
    mydict={val:medals[ind] for ind,val in enumerate(sorted(score,reverse=True))}

    return [mydict[i]for i in score]


print(Qualify(score))


# points = [1, 5, 4, 2, 6, 8, 3]

# sorted_points = sorted(points, reverse = True)
# result = [sorted_points.index(num) + 1 for num in points]
# print(result)
