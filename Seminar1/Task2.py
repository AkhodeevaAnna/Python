# list = list(input())
# print(list)
# max = list[0]
# for i in range(5):
#     if list[i] > max:
#         max = list[i]
# print(max)

print("Введите 5 чисел: ")
max = 0
for i in range(5):
    a = int((input()))
    if a > max:
        max = a
print("max = ", max)