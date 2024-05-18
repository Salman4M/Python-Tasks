# Input
# name = input("Adinizi daxil edin: ") # --> name = "Fuad"

# print(name)


# age = input()

# print(age)


# name = "Fuad"
# name1 = 'Fuad'
# name2 = """Fuad"""
# name3 = '''Fuad'''


# number1 = 10 # -->  integer

# number2 = 10.0 # --> float
# number3 = 70.6


# number4 = 3 + 2j
# print(type(number4))

# bool1 = True
# bool2 = False



# # String methods


word = "Coders"

# 1) Upper method

# print(word.upper())


# # 2) Lower method

# print(word.lower())


# # 3) Isupper, islower methods

# word2 = word.upper()
# word3 = word.lower()

# print(word2.isupper())
# print(word3.isupper())
# print(word.upper().isupper())

# print(word.islower())
# print(word3.islower())


# # 4) Capitalize

text = "hello world"

# print(text.capitalize())


# # 5) title method

# print(text.title())



# 6) isalpha, isdigit or isnumeric, isalnum


# text1 = "salam"
# text2 = "123"
# text3 = "salam123"
# text4 = "salam123!"
# text5= "3.4"


### isalpha

# print(text1.isalpha())
# print(text2.isalpha())
# print(text3.isalpha())
# print(text4.isalpha())


### isnumeric

# print(text1.isnumeric())
# print(text2.isnumeric())
# print(text3.isnumeric())
# print(text4.isnumeric())
# print(text5.isnumeric())



### isalnum

# print(text1.isalnum())
# print(text2.isalnum())
# print(text3.isalnum())
# print(text4.isalnum())

### isdigit
# print(text1.isdigit())
# print(text2.isdigit())
# print(text3.isdigit())
# print(text4.isdigit())
# print(text5.isdigit())


'''The isdigit() method accepts only decimals, subscripts (X2), and superscripts(x2). 
The isnumeric() function supports Digits, Vulgar Fractions (3/4 , 2/5), Subscripts, Superscripts, Roman Numerals, and Currency Numerators.'''

# startswith, endswith

# print("Text: ", text)
# print(text.startswith("hello"))
# print(text.startswith("h"))
# print(text.startswith("hell"))
# print(text.startswith("helo"))


# # print(text.endswith('world'))
# # print(text.endswith('wor'))
# # print(text.endswith('ld'))


# # Indexing

# print("word: ", word)

# Coders

# index 0: --> C <-- index: -6
# index 1: --> o <-- index: -5
# index 2: --> d <-- index: -4
# index 3: --> e <-- index: -3
# index 4: --> r <-- index: -2
# index 5: --> s <-- index: -1

# print("0-ci index: ", word[0])
# print("3-cu index: ", word[3])
# print("-2-cu index: ", word[-2])


# # word[start: end: step]


# print("word[2:4] -->", word[2:4])
# print("word[:4] -->", word[:4])
# print("word[2:] -->", word[2:])
# print("word[:] -->", word[:])



# print("word[4:1:-1] --> ", word[4:1:-1])
# print("word[:2:-1] --> ", word[:2:-1])
# print("word[4::-1] --> ", word[4::-1])
# print("word[::-1] --> ", word[::-1])


# print("word[::2] -->", word[::2])
# print("word[::-2] -->", word[::-2])




# # index, find
#both of them do the same thing, but there is not the value we are looking for index brings error, find brings -1 in the response.

# print(word.index("C"))
# print(word.index("d"))
# print(word.index("c"))


# print(word.find("C"))
# print(word.find("d"))
# print(word.find("c"))



# # len


# print(len(word))


# strip, rtsrip, lstrip

# input1 = input("Bisey daxil edin: ")

# print(len(input1))


# updated_input = input1.strip()

# print(updated_input)
# print(len(updated_input))


# updated_input = input1.rstrip()

# print(updated_input)
# print(len(updated_input))


# updated_input = input1.lstrip()

# print(updated_input)
# print(len(updated_input))




# count

soz = "Salam Necesen"
# soz2 = "Salam Necesen Necesen"


# print(soz.count("a"))
# print(soz.count("A"))
# print(soz.count("d"))


# # replace

# print(soz.replace("Necesen", "Dunya"))
# print(soz.replace("World", "Dunya"))


# print(soz2.replace("Necesen", "Dunya"))
# print(soz2.replace("World", "Dunya"))



# # split


word100 = "Coders Azerbaijan AzerSalam"


# print(word100.split())
# print(word100.split("Azer"))



# # 1-ci yol

name = "Fuad"
surname = "Huseynov"

# print("Salam", name)



# 2-ci yol (Kohne usul)

result = "Salam %s %s" %(name, surname)

print(result)


# 3-cu yol (format methodu)


result = "Salam {} {}".format(name, surname)
result = "Salam {n} {sn}".format(sn=name, n=surname)

print(result)


# 4-cu yol (f-stringler)


result = f"Salam {name} {surname}"
# result = f"Salam {12+13} {surname}"
op1 = f"{12} + {13} = {12+13}"

print(result)
print(op1)