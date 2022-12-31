names = input('Введите ФИ в формате ИФ, ИФ,... : ').split(', ')
keys = []
space = []
for i in names:
    space = str(i).split()
    keys.append(space[1][0])
    space = []
keys = sorted(keys)
dic = {}.fromkeys(keys, [])
for i in names:
    space = str(i).split()
    dic[space[1][0]] = dic[space[1][0]] + [i]
print(keys)
print(dic)