# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

N = int(input())
one = int(input())
two = int(input())
# list = []
if N >= 0:
    list = list(range(-N, N+1))
else:
    list = list(range(-N,N-1, -1))
# n = - N
# while n <= N:
#     list.append(n)
#     n += 1
print(list)
if 0 < one <= len(list) and 0 < two <= len(list):
    pr = list[one-1] * list[two-1]
    print(pr)
else:
    print("There are no values for these indexes!")