
def remove_vowels(word):
    vowels=['A','a','E','e','U','u','I','i','Ə','ə','Ü','ü','Ö','ö','O','o']
    nonVowels=[]
    for i in word:
        if not i in vowels and i.isalpha():
            nonVowels.append(i)

    return set(nonVowels)


# myword='sSalam Əli'
# print(remove_vowels(myword))



