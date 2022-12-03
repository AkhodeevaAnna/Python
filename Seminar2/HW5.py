# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random
n = int(input())
list = []
for i in range(n):
    list.append(i)
print(list)
for i in range(n):
    k = random.randrange(n)
    temp = list[i]
    list[i] = list[k]
    list[k] = temp
print(list)