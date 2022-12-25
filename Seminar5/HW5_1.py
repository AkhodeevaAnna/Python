# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect

from random import choices, sample
n = int(input())
while n < 1:
    n = int(input('Введите число > 0: '))
words = []
for i in range(n):
    # new_word = ''.join(choices('абв', k = 3))
    new_word = ''.join(sample('абв', k = 3))
    words.append(new_word)
print(' '.join(words))

def del_word(words_list, word):
    count = words_list.count(word)
    if count > 0:
        for i in range(count):
            words_list.remove(word)
        return ' '.join(words_list)
    return f'В тексте нет слова {word}'

word = input('Какое слово нужно удалить? ')
print(del_word(words, word))