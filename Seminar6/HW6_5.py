from random import choices
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
N = int(input())
one = choices(nouns, k = N)
two = choices(adverbs, k = N)
three = choices(adjectives, k = N)
result = list(zip(one,two,three))
print(result)