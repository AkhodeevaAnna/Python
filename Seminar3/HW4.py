# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import random
count = int(input())
while count < 1:
    count = int(input("Кол-во чисел в списке не может быть меньше 1, введите положительное число: "))

def Rand_list_float (count):
    list = []
    for i in range(count):
        number = round(random.uniform(0, count*10), 3)
        list.append(number)
    return list
def Cut_int (list):
    for i in range (len(list)):
        list[i] = round(list[i] % 1, 3)
    return list
def Find_max (list):
    max = list[0]
    for i in range (len(list)):
        if list[i] > max:
            max = list[i]
    return max
def Find_min (list):
    min = list[0]
    for i in range (len(list)):
        if list[i] < min:
            min = list[i]
    return min
list = Rand_list_float(count)
print(list)
new_list = Cut_int(list)
print(new_list)
max = Find_max(new_list)
min = Find_min(new_list)
print(f"Min = {min}, Max = {max}, Difference = {round(max - min, 3)}")