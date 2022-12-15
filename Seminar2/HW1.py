# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27
num = input()
num_str = num
num = float(num) # для подсчета float части
n = num # для подсчета int части# для подсчета float части
if num < 0:
    num *= -1
    n *= -1
sum = 0
count = 0
while n // 1 > 0:
    n = n // 10
    count += 1
print(f"count: {count}")

if num // 1 == 0:
    power = len(num_str) - 2
else:
    power = len(num_str) - count - 1
print (f"power: {power}")

if power > 0:
    num = num * 10 ** power
    print(f"num: {num}")

while num > 0:
    sum += num % 10
    num //= 10
print(sum)