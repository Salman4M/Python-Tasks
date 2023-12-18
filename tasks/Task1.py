''' 1) Userdən bir input (username) götürün və həmin inputun böyük/kiçik hərflərdən ibarət olub olamdığını yoxlayın

2) Userdən bir input (email) götürün və içində "@" olub olmadığını yoxlayın

3) sentence = "The quick brown fox jumps over the lazy dog". Userdən bir input (search) götürün və həmin inputun sentence içində nə qədər təkrarlandığını tapın

4) Userdən iki input götürün (name, surname) və həmin inputları sağ və sol boşluqlardan təmizləyin

5) word = "Coders Caravan". Aşağıdakı örnəkləri koda çevirin (İndeksləmə)
	* "Coders"
	* "Caravan"
	* "ders"
	* "navaraC sredoC"
	* "Cdr aaa"
	* "Crvn"
	* "vrCseo"

6) Userdən bir input (password) götürün və həmin inputun ilk elementinin rəqəmlə başlayıb başlamadığını yoxlayın

7) Userdən üç input götürün (word, text1, text2). word dəyişkənində text1 hissəsini text2 ilə dəyişin

Example: word="Coders Caravan"; text1="Coders"; text2="Azerbaijan"
	 Output: Coders Azerbaijan

8) Userdən bir input istəyin (cümlə şəklində olsun) və həmin inputdakı bütün sözlərin ilk hərfini böyüdün

9) Userdən bir input (password) götürün və həmin inputun elementlərinin ancaq hərf və rəqəmlərdən ibarət olub olmadığını yoxlayın

10) Userdən bir input istəyin (cümlə şəklində olsun) və həmin inputdakı bütün sözləri bir listin içində balaca hərflərlə göstərin

Example: sentence = "The quick brown fox jumps over the lazy dog"
	 Output: [ "the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
     '''

print("My username is Salman.m")

username = input("what is your name:")
print(username.islower())
print(username.isupper())
print("My email is salmanmammadli@hotmail.com")
email = input("what's your email adress:")
print(email.find("@"))
print(email.index("@"))


sentence = "The quick brown fox jumps over the lazy dog"
search = input("")
print(sentence.count(search))


name = input("my name is: ")

print(name)


surname = input("my surname is:")

print(surname)


print(name.strip())
print(surname.strip())

word = "Coders Caravan"

print(word[0:6]) #Coders
print(word[-7:]) # Caravan
print(word[2:6]) #ders
print(word[::-1]) # navaraC sredoC
print(word[::2]) #Cdr aaa
print(word[7::2]) #Crvn
print(word[11::-2]) #

password = input("My password is:")
print(password[0].isnumeric())



'''Example: word="Coders Caravan"; text1="Coders"; text2="Azerbaijan"
 Output: Coders Azerbaijan'''

word = input("my word is:")
text1= input("text1 is ")
text2 = input("text2 is ")

print(word)
print(text1)
print(text2)

print(word.replace(text1,text2))


sentence = input(" ")
print(sentence.title())


password = input("is it:  ")
print(password.isalnum())

sentence = input("")
x = sentence.lower()

print(x.split())