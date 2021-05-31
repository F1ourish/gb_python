from itertools import islice, zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '10В'
]

my_gen = (i for i in zip_longest(tutors, klasses))

print('Тип переменной my_gen после преобразования является генератором: ', type(my_gen))
print(*islice(my_gen, 8))
print('В генераторе закончились значения, он истощён: ', list(islice(my_gen, 3)))