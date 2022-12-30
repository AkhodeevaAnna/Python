# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import choices
n = int(input())
def creat_list(n):
  numbers = choices(range(n*2), k = n)
  return numbers
def creat_list_of_uniq(numbers):
  n = len (numbers)
  uniq = []
  count = 0
  for i in range (n):
    p = numbers[i]
    for j in numbers:
      if j==p:
        count+=1
    if count == 1:
      uniq.append(p)
    count = 0
  return uniq
numbers = creat_list(n)
print(numbers)
print(creat_list_of_uniq(numbers))