# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

path_d = input(('Введите путь к файлу с декодированным текстом: '))
path_c = input(('Придумайте название файла для сохранения кодированного текста (name.txt): '))
data_1 = open (path_d, 'r')
for line in data_1:
    list_1 = list(line)
    list_1.append(0)
    list_2 = []
    while list_1 != [0]:
        count = 1
        test = list_1[0]
        i = 0
        while list_1[i] == list_1[i+1]:
            if list_1[i] == test:
                count += 1
            i+=1
        list_2.append(str(count))
        list_2.append(test)
        del list_1[:i+1]
    with open (path_c,'a') as data_2:
        data_2.write(''.join(list_2))

data_1.close()
