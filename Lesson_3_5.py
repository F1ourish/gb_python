# На этом задании я сильно завис, пришлось всё-таки смотреть разбор, правда в коде, который был на уроке, min от 3х
# списков работает неверно, он всегда считает значение первого списка nouns как минимальное, хотя должен быть
# adjectives в моём случае (насколько я понял, он сравнивает построково списки и где самая короткая строка, тот список
# для него является min), поэтому я изменил этот код

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "свеча"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "утром", "вечером"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(var, repeat=False):
    """
    Функция возвращает случайные шутки, сформированные из трех случайных слов, взятых из трёх списков
    (по одному из каждого)
    :param var: количество шуток
    :param repeat: флаг уникальности шуток
    :return: список сгенерированных шуток
    """
    nouns1, adverbs1, adjectives1 = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []
    minimal_list = []
    if len(nouns1) < len(adverbs1) and len (nouns1) < len(adjectives1):
        minimal_list = nouns1
    elif len(adverbs1) < len(nouns1) and len(adverbs1) < len(adjectives1):
        minimal_list = adverbs1
    elif len(adjectives1) < len(nouns1) and len(adjectives1) < len(adverbs1):
        minimal_list = adjectives1

    while var and len(minimal_list):
        num = random.randrange(len(minimal_list))
        if repeat:
            jokes.append(f"{nouns1.pop(num)} {adverbs1.pop(num)} {adjectives1.pop(num)}")
        else:
            jokes.append(f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}")
        var -= 1
    return jokes

print(get_jokes(int(input("Введите количество шуток для генерации: "))))
# print(get_jokes(10))
