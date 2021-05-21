def thesaurus(*args):
    names = {}
    args = sorted(args)
    for i in args:
        letter = i[0]
        if letter in names:
            names[letter] += [i]
        else:
            names[letter] = [i]

    return names

print(thesaurus("Иван", "Мария", "Петр", "Илья"))


# Здесь я решил уже посмотреть разбор дз, т.к. сдать до занятия не успел из-за работы и некоторых форсмажорных ситуаций,
# так что решил сразу для себя продублировать код и разобрать его работу
#
# def thesaurus(*args):
#     names = {}
#     for i in sorted(args):
#         if i[0] not in names:
#             names[i[0]] = list(filter(lambda el: el.startswith(i[0]), args))
#         print(names)
#
#
# print(thesaurus("Иван", "Мария", "Петр", "Илья"))


# def thesaurus_adv(*names):
#     names_dict = {}
#     for name in sorted(names):
#         n, s = name.split()
#         val = names_dict.setdefault(s[0], {n[0]: [name]})
#         n_val = val.setdefault(n[0], [name])
#         if name not in n_val:
#             n_val.append(name)
#     return names_dict
#
# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))