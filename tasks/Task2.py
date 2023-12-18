'''1) Userden iki reqem isteyin ve hemin reqemleri asagidaki kimi muqayise edin:

	* Boyukdurmu
	* Kicikdirmi
	* Beraberdirmi
	* Beraber deyilmi (2 ferqli yolla)
	* idlerinin uzunlugu beraberdirmi
	* idlerinin ilk 4 reqemi beraberdirmi

2) Userden iki input (name1, name2) isteyin ve daha sonra asagidaki kimi muqayise edin:
	
	* name1-in ilk elementi ve name2-nin ilk elementi beraberdise ve ya name1-in son elementi ve name2-nin son elementi beraberdirse
	* (name1-in uzunlugu ve name2-nin uzulugu berabedrdise ve name1-in idsi name2-nin id-sinden boyuk beraberdise) ve ya name1 name2-e beraberdise (hem qiymet hem id olaraq)

3) Bir setirde iki deyisken tamamlayin (a, b) ve daha sonra bu deyiskenleri toplayib a-da yadda saxlayin (Qisa olaraq nece yazilirsa ele yazin)
'''
num1 = 20
num2 = 30
print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 != num2)
print(not num1 == num2)

num3 = 30
num4 = 30.0

x = (str(id(num3)))
print(len(x))

y = (str(id(num4)))
print(len(y))

print (x == y)


number1 = 853326577
number2 = 934325932

print(str(id(number1))[:4] == str(id(number2))[:4])


a = id(num3)
print(a[0:4])

name1 = input("name1 is: ")
name2 = input("name2 is: ")

print((name1[0]==name2[0]) or name1[-1] == name2[-1] )
print((len(name1)==len(name2) and (id(name1) >= id(name2)) or (name1==name2 and id(name1)==id(name2))))

a,b = "Baku ", "is beatiful city"
print(a)
print(b)
a += b

print(a)
