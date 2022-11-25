# 3. Напишите программу, которая будет на вход принимать
# число N и выводить числа от -N до N

N = int(input())
list = ""
if N >= 0:
    for i in range (-N, N+1):
        l = str(i) + ' '
        list = list + l
else:
    for i in range (-N, N-1, -1):
        l = str(i) + ' '
        list = list + l
    # M = N * (-1)
    # while M >= N:
    #     l = str(M) + ' '
    #     list = list + l
    #     M -= 1
print(list)