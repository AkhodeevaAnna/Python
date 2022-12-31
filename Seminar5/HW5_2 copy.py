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

path_d = input(('Введите путь к файлу с кодированным текстом: '))
path_c = input(('Придумайте название файла для сохранения декодированного текста (name.txt): '))
data_1 = open (path_d, 'r')
for line in data_1:
    # list_1 = list(line)
    kof = ''
    line_2 = ''
    for i in line:
        if i.isdigit():
            kof += i
        else:
            line_2 += int(kof) * i
            kof = ''
    with open (path_c,'a') as data_2:
        data_2.write(''.join(line_2))

data_1.close()
