# Bir funksiya yazın və funksiyaya  list və ədəd göndərin və listin 2 elementinin cəmi həmin ədədə 
# bərabər olarsa funksiya həmin iki ədədin indeksini list formatında əgər belə elementlər yoxdursa -1 qaytarsın.
# İnput:
# [2, 8, 8, 12, 15]
# Output:
# [2, 3] 


class Checker:
    def __init__(self,mynumber):
        self.mylist=[]
        self.mynumber=mynumber

    def appendList(self,them):
        for i in them:
            self.mylist.append(i)
        return self.mylist
    
    def InList(self):
        right=1
        left=0
        while left<right:
            check=self.mylist[left]+self.mylist[right]
            if check==self.mynumber:
                return (left,right)
            
            if right==len(self.mylist)-1:
                left+=1
                right=left+1
            else:
                right+=1

            if left==len(self.result)-1:
                break
        
        return -1


obj=Checker(3)
obj.appendList([1,2,4,6,7])
print(obj.InList())