y = input()

if y.count(' ') * 2 + 1 != len(y):
  print('Может быть ошибка')
y = y.split()

# **
def steppen(y):
  for i in range(len(y) -1 , -1, -1):
    if y[i] == '^':
      y[i-1] = int(y[i-1]) ** int(y[i+1])
      y[i] = 'z'
      y[i+1] = 'z'
  for i in range(y.count('z')):
    y.remove('z')
  return y

# * / // %
def one_oper(y):
  for i in range(len(y)):
    if y[i] == '*':
      y[i+1] = float(y[i-1]) * float(y[i+1])
      y[i] = 'z'
      y[i-1] = 'z'
    if y[i] == '/':
      y[i+1] = round(float(y[i-1]) / float(y[i+1]), 3)
      y[i] = 'z'
      y[i-1] = 'z'
    if y[i] == '//':
      y[i+1] = float(y[i-1]) // float(y[i+1])
      y[i] = 'z'
      y[i-1] = 'z'
    if y[i] == '%':
      y[i+1] = float(y[i-1]) % float(y[i+1])
      y[i] = 'z'
      y[i-1] = 'z'
  for i in range(y.count('z')):
    y.remove('z')
  return y

# + -
def two_oper(y):
  for i in range(len(y)):
    if y[i] == '+':
      y[i+1] = float(y[i-1]) + float(y[i+1])
      y[i] = 'z'
      y[i-1] = 'z'
    if y[i] == '-':
      y[i+1] = float(y[i-1]) - float(y[i+1])
      y[i] = 'z'
      y[i-1] = 'z'
  n = y.count('z')
  for i in range(n):
    y.remove('z')
  return y

print(y)

if y.count('('):
  i = 0
  new_y = []
  while i < len(y):
    if y[i] == '(':
      print(y[i])
      k = y.index(')')
      print(k)
      new_y = y[i+1:k]
      print(new_y)
      new_element = (two_oper(one_oper(steppen(new_y))))
      print(new_element)
      new_y = []
      y[i] = new_element[0]
      y = y[:i+1] + y[k+1:]
      print(y)
    i += 1
print(y)
print(one_oper(steppen(y)))
print(two_oper(one_oper(steppen(y))))