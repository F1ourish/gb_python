from json import dump
from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:

# ****** Собственно, сразу делаю проверку будем ли мы работать с файлами или выходить из скрипта с кодом 1 ******

        # if len(users.readlines()) > len(hobby.readlines()):
            with open("dict_user_hobby.json", "w", encoding="utf-8") as file:
                # Здесь пришлось подсмотреть в разбор ДЗ
                summary = zip_longest((" ".join(i.split(",")) for i in users), hobby, fillvalue=None)
                new_dict = {str(i[0]).strip(): (i[1].strip()) for i in summary}

                dump(new_dict, file, ensure_ascii=False, indent=4)
            print(new_dict)
        # else:
        #     exit(1)

# ****** Под звёздочкой не сделал, здесь чисто смотрел и разбирал как это работает ******

# from itertools import zip_longest
#
# with open("users.csv", "r", encoding="utf-8") as users:
#     with open("hobby.csv", "r", encoding="utf-8") as hobby:
#         summary = zip_longest(users, hobby, fillvalue=None)
#
#         with open("users_hobby.txt", "w", encoding="utf-8") as f:
#             for i in summary:
#                 print(f"{str(i[0]).strip()}: {i[1].strip()}", file=f)
