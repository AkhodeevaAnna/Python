# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]

N = int(input())
def simple_mn (N):
  m = 2
  list = []
  while N > 1:
    while N % m == 0:
      N = N / m
      list.append(m)
    m+=1
  return list
print(simple_mn(N))