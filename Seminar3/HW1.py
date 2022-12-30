# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8
import random
count = int(input())
while count < 0:
    count = int(input("Кол-во чисел в списке не может быть отрицательным, введите положительное число: "))
def Rand_list(count):
    list = random.sample (range(count*2), k = count)
    return list
def Sum_of_position(list, position):
    sum = 0
    for i in range(position, len(list), 2):
        sum += list[i]
    return sum
nums = Rand_list(count)
print(nums)
sum = Sum_of_position(nums, 0)
print(sum)