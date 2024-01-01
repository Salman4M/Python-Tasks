### Tasks
"""
1) Bir text qebul eden funksiya yazin ve bu funksiya textin icindeki en son sozun uzunlugunu qaytarmalidir

    Ex.1: word = "Coders Azerbaijan" ---> Output: Azerbaijan, 10
    Ex.2: word = "   Fly me to   the moon   " --> Output: moon, 4
    Ex.3: word = "  " --> Output: "", 0

    
2) Bir nece elementli list yaradin ve daha sonra update_list adinda bir funksiya yaradin 
Bu funksiya 3 parametr qebul edecek: start, end, elements. Funksiyanin meqsedi start ve end
arasindaki elementleri elements ile deyismekdir
Note: start ve endin default qiymetleri None olmalidir

    mylist = [10, 20, "salam", "coders", 70.8, 67]
    Ex.1: end=2, elements="python" 
        --> Output: ["python", "salam", "coders", 70.8, 67]
    
    Ex.2: start=3, elements=["django", "api"]
        --> Output: [10, 20, "salam", "django", "api"]
    
    Ex.3: start=2, end=4, elements=("baki", "sumqayit")
        --> Output: [10, 20, "baki", "sumqayit", 70.8, 67]

3) Bir list ve string qebul eden funksiya yazmaq lazimdi ve asagidaki numunelere 
    uygun olmalidir

    Ex.1:  dictionary = ["cat","bat","rat"], 
           sentence = "the cattle was rattled by the battery"
        Output: --> "the cat war rat by the bat"
    
    Ex.2: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
        Output: --> "a a b c"
"""


# Task1
# word1 = "Coders Azerbaijan"
# word2 = "   Fly me to   the moon   "
# word3 = "  "

# def find_length_of_last_word(text):
#     return len(text.strip().split()[-1]) if text.strip() != "" else 0


# print(find_length_of_last_word(word1))
# print(find_length_of_last_word(word2))
# print(find_length_of_last_word(word3))


# Task2

# mylist = [10, 20, "salam", "coders", 70.8, 67]


# def replace_elements(elements, start=None, end=None):
#     mylist[start:end] = [elements] if type(elements) in [str, int, float] else list(elements)
#     return mylist


# print(replace_elements(elements="python", end=2))
# print(replace_elements(elements=["django", "api"], end=2))
# print(replace_elements(elements=("baki", "sumqayit"), end=4, start=2))



# Task 3

# dictionary = ["cat","bat","rat"]
# sentence = "the cattle was rattled by the battery"


# def replace_words(sentence, dictionary):
#     for elem in dictionary:
#         for text in sentence.strip().split():
#             if text.startswith(elem):
#                 sentence = sentence.replace(text, elem)
    
#     return sentence


# print(replace_words(sentence, dictionary))




# Task4

str1 = "3+4"  # --> 7
str2 = "9 +    7/3" # --> 11


def calculate_operation(text):
    text = text.replace(" ", "")
    operation_list = ["*", "/", "+", "-"]

    for op in operation_list:
        if op in text:
            index_ = text.find(op)
            first_, last_ = index_-1, index_+1
            if op == "*": result = int(int(text[first_]) * int(text[last_]))
            elif op == "/": result = int(int(text[first_]) / int(text[last_]))
            elif op == "+": result = int(int(text[first_]) + int(text[last_]))
            elif op == "-": result = int(int(text[first_]) - int(text[last_]))
            text = text.replace(f"{text[first_]}{op}{text[last_]}", str(result))
            break

    # if "*" in text:
    #     index_ = text.find("*")
    #     first_, last_ = index_-1, index_+1
    #     result = int(int(text[first_]) * int(text[last_]))
    #     text = text.replace(f"{text[first_]}*{text[last_]}", str(result))
    # elif "/" in text:
    #     index_ = text.find("/")
    #     first_, last_ = index_-1, index_+1
    #     result = int(int(text[first_]) / int(text[last_]))
    #     text = text.replace(f"{text[first_]}/{text[last_]}", str(result))
    # elif "+" in text:
    #     index_ = text.find("+")
    #     first_, last_ = index_-1, index_+1
    #     result = int(int(text[first_]) + int(text[last_]))
    #     text = text.replace(f"{text[first_]}+{text[last_]}", str(result))
    # elif "-" in text:
    #     index_ = text.find("-")
    #     first_, last_ = index_-1, index_+1
    #     result = int(int(text[first_]) - int(text[last_]))
    #     text = text.replace(f"{text[first_]}-{text[last_]}", str(result))
    
    return text if text.isdigit() else calculate_operation(text)


print(calculate_operation(str1), 'asdjasjid')
print(calculate_operation(str2), 'asdjasjid')