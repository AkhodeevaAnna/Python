from random import sample
count = int(input("Введите кол-во элементов последовательности: "))
N = int(input("Введите число для проверки его наличия в последовательности: "))
def Rand_list(a):
    list = sample (range(a*2), k = a)
    return list
def Find_N (b, list):
    if b in list:
        return "Yes"
    return "No"
list = Rand_list(count)
print(list)
print(Find_N(N, list))