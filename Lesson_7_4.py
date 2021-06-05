# import os
# import django
# import collections
#
# def dir_info():
#     dir_root = django.__path__[0]  # Файловая структура библиотеки django
#     files_django = collections.defaultdict(int)
#     for root, dirs, files in os.walk(dir_root):
#         for f in files:
#             size = 10 ** len(str(os.stat(os.path.join(root, f)).st_size))  # длина числа используется в качестве ключа
#             files_django[size] += 1  # Счётчик количества файлов
#
#         for size, num in sorted(files_django.items()):
#             print(f'{size}: {num}')
#
# dir_info()


# ***************************************** Интересная интересность ************************************************

import os
import json
import django


def dir_info():
    dir_root = django.__path__[0]
    files_django = {}
    for root, dirs, files in os.walk(dir_root):
        for f in files:
            size = 10 ** len(str(os.stat(os.path.join(root, f)).st_size))  # длина числа используется в качестве ключа
            ext = f.rsplit('.', maxsplit=1)[-1].lower()  # расширение файла
            if size in files_django:
                files_django[size][0] += 1  # Счётчик количества файлов
                if ext not in files_django[size][1]:  # если расширения нет, то добавляем
                    files_django[size][1].append(ext)
                else:
                    files_django[size] = [1, [ext]]

    result = {}
    for size, log in sorted(files_django.items()):  # сортируем и формируем кортеж
        result[size] = tuple(log)
        print(f'{size}: {tuple(log)}')

    folder = os.path.basename(os.getcwd()) + '_summary.json'  # получаем имя папки
    with open(folder, 'w', encoding='utf-8') as f:  # сохраняем в файл
        json.dump(result, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    dir_info()