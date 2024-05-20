# 506. Relative Ranks


#bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır. Biz isə onların topladığı xallara görə
#neçənci yeri tutduğunu print etməliyik. Misal üçün bizə xallar verilib. xallar = [5,3,4,2,1].
#Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq. yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']
#Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də o pozulmuş sıraya uyğun sıralanacaq və nəticə 
#düzgün olmayacaq.(taskı daha da asanlaşdırmaq üçün hərkəsin  xalı müxtəlif olacaq. Eyni xala sahib 2 şəxs olabilməz)

# score = [8,3,4,5,1]

# def Qualify(score:list):
#     them=list(reversed(sorted(score)))
#     medals=['Gold Medal','Silver Medal','Bronze Medal','4','5']
#     mydict={val:medals[ind] for ind,val in enumerate(them)}

#     return [mydict[i]for i in score]


# print(Qualify(score))


# points = [1, 5, 4, 2, 6, 8, 3]

# sorted_points = sorted(points, reverse = True)
# result = [sorted_points.index(num) + 1 for num in points]
# print(result)




def Yer_Sıralaması(Points):
    Point_İndexes = [(xal, index) for index, xal in enumerate(Points)]
    Point_İndexes = sorted(Point_İndexes, reverse=True)
    Places = [''] * len(Points)
    for i, (xal, index) in enumerate(Point_İndexes):
        if i == 0:
            Places[index] = '1-ci'
        elif i == 1:
            Places[index] = '2-ci'
        elif i == 2:
            Places[index] = '3-cü'
        else:
            Places[index] = str(i + 1) + '-ci'
    return Places

Points = [3, 8, 4, 6, 1]
print(Yer_Sıralaması(Points))