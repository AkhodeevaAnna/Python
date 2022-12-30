from random import choices
n = int(input())
list_1 = [i for i in choices(range(n*2), k = n)]
list_2 = [list_1[j] for j in range(1, len(list_1)) if list_1[j] > list_1[j-1]]
print(list_1)
print(list_2)