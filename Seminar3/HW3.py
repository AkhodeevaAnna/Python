# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011
number = int(input())
def Ten_to_two (n):
    list = []
    if n == 0:
        list.append(0)
    elif n >= 0:
        while n > 0:
            list.insert(0, n % 2)
            n //= 2
    else:
        n *= -1
        while n > 0:
            list.insert(0, n % 2)
            n //= 2
        while len(list) < 8:
            list.insert(0,0)
        for i in range (len(list)):
            if list[i] == 0:
                list[i] = 1
            elif list[i] == 1:
                list[i] = 0
        list [len(list) - 1] = 1
    return list
number_two = Ten_to_two(number)
print(number_two)