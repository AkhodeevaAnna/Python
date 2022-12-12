import random
n = int(input("Сколько сделать слов? "))
letters = input("Из чего сделать слова? ")
def Rand_str(n, letters):
    list = []
    for i in range(n):
        l = ''.join(random.choice(letters) for i in range(3))
        list.append(l)
    return list
list = Rand_str(n, letters)
print(list)
def Find_index2_str(f, list):
    if list.count(f) > 1:
        index_1 = list.index(f)
        return list.index(f, index_1 + 1)
    return -1
f = input("Что ищите? ")
print(Find_index2_str(f,list))




# def generate_random_string(length):
#     letters = 'xyz'
#     rand_string = ''.join(random.choice(letters) for i in range(length))
#     print("Random string of length", length, "is:", rand_string)


# generate_random_string(8)