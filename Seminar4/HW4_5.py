file_from = input(('Введите путь к файлу с декодированным текстом: '))
# file_to = input(('Придумайте название файла для сохранения кодированного текста (name.txt): '))
data_1 = open (file_from, 'r')
res_mnch = ''
for line in data_1:
    mnch = str(line)
    mnch = mnch[:len(mnch) - 5]
    if res_mnch == '':
        res_mnch = mnch
    elif mnch[1] == '-':
        res_mnch = res_mnch + mnch
    else:
        res_mnch = res_mnch + ' + ' + mnch
res_mnch = res_mnch + ' = 0'
print(res_mnch)
with open ('file_2.txt','a') as data_2:
     data_2.write(''.join(res_mnch))

data_1.close()