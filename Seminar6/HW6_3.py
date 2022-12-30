names = input().split()
keys = []
for i in names:
    keys.append(i [0])
keys = sorted(keys)
dic = {}.fromkeys(keys, [])
for i in names:
    dic[i[0]] = dic[i[0]] + [i]
print(keys)
print(dic)