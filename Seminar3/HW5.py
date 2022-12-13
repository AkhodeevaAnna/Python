# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5
n = int(input()) # кол-во индексов Фибоначчи
while n < 1:
    n = int(input("Введите число больше 1: "))
def Negafibonacci (n):
    list = [0]
    if n > 0:
        list.append(1)
        list.insert(0, 1)
        if n > 1:
            list.append(1)
            list.insert(0,-1)
            if n > 2:
                for i in range (1, n-1, 2):
                    l = len(list)
                    n_1 = list[l-1] + list[l-2]
                    list.append(n_1)
                    list.insert(0, n_1)
                    l = len(list)
                    n_2 = list[l-1] + list[l-2]
                    list.append(n_2)
                    list.insert(0, -n_2)
    if len(list) > n * 2 + 1:
        list.pop()
        list.pop(0)
    return list
print(Negafibonacci(n))