# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

import random
count = int(input())
while count < 0:
    count = int(input("Кол-во чисел в списке не может быть отрицательным, введите положительное число: "))

def Rand_list(count):
    list = random.sample (range(count*2), k = count)
    return list

def Product_of_couple_nums(list_0):
    list_1 = []
    l = len(list_0) // 2 # длиня для цикла
    l_1 = len(list_0) # длина для счета
    if len(list_0) % 2 == 0:
        for i in range(0, l):
            list_1.append(list_0[i] * list_0[l_1 - 1 - i])
    else:
        for j in range (l):
            list_1.append(list_0[j] * list_0[l_1 - 1 - j])
        list_1.append(list_0[l])
    return list_1

list_00 = Rand_list(count)
print(list_00)
list_11 = Product_of_couple_nums(list_00)
print(list_11)