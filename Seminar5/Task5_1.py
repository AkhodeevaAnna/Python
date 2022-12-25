from random import randint

def rew (rew_list):
    for i in range(len(rew_list)):
        if rew_list[i] - 1 != rew_list[i-1]:
            if list_one[i] - 1 >= 0:
                return rew_list[i] - 1
    return -1

N = int(input())
while N < 1:
    N = int(input('Введите положительное число: '))
list_one = [i for i in range (N+1)]
print(list_one)

del list_one[randint(0,N-1)]
print(list_one)
print(rew(list_one))