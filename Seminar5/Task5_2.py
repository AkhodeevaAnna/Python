from random import choices
n = int(input())
rand_list = choices(range(n*2), k = n)
print(rand_list)
res_list = []
new_list = []
for i in range(n):
    add_num = rand_list[i]
    new_list.append(add_num)
    for j in range(i,n):
        if rand_list[j] > add_num:
            add_num = rand_list[j]
            new_list.append(add_num)
    if len(new_list) > 1:
        res_list.append(new_list)
    new_list = []
print(res_list)