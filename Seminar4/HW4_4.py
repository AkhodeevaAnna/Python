# * 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# in
# 0
# -1
# 4
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import randint
nums = input('Введите числа через пробел в одну строку: ').split()
def manych (n):
  mnch = ''
  for i in range(n, -1, -1):
    k = randint (- 9, 9)
    if n == 0:
      if k < 0:
        mnch = mnch[:len(mnch) - 3]
        mnch = mnch + ' - ' + str(abs(k))
      elif k > 0:
        mnch = mnch + str(k)
      else: # k == 0
        mnch = mnch[:len(mnch) - 3]
    elif n == 1:
      if k > 0:
        mnch = mnch + str(k) + '*x' + ' + '
      elif k < 0:
        mnch = mnch[:len(mnch) - 3]
        mnch = mnch + ' - ' + str(abs(k)) + '*x' + ' + '
    else:
      if k > 0:
        mnch = mnch + str(k) + '*x^' + str(n) + ' + '
      elif k < 0:
        mnch = mnch[:len(mnch) - 3]
        mnch = mnch + ' - ' + str(abs(k)) + '*x^' + str(n) + ' + '
    n -= 1
  mnch = mnch + ' = 0'
  return mnch
for j in nums:
  print(manych(int(j)))
for j in nums:
    with open ('file.txt','a') as data:
      data.write(manych(int(j)))
      data.write('\n')