# ******* Split у нас делит по пробелам до \n и создаёт list из элементов, поэтому мы легко можем обратиться
# к каждому из них по номеру элемента и вывести нужную нам инфу

with open("nginx_logs.txt", "r", encoding="utf-8") as file:
    content = ((el.split()[0], el.split()[5][1:], el.split()[6]) for el in file)
    for i in content:
        print(i)

# ******* Со спамером не разобрался, нужно создавать словарь и считать сколько раз встречается ключ, которым является
# ip, до реализации не дошёл, поэтому сразу перешёл к разбору домашнего задания и прорабатывал код уже с урока.
# Пришлось также продублировать код с урока с созданием файла логов для более удобной работы.

with open("parsed_logs.txt", "w", encoding="utf-8") as file1:
    with open("nginx_logs.txt", "r", encoding="utf-8") as file2:
        content = (f"{line.split()[0]} {line.split()[5][1:]} {line.split()[6]}" for line in file2)
        for i in content:
            print(i, file=file1)

import collections

with open("nginx_logs.txt", "r", encoding="utf-8") as file:
    spam_det = collections.Counter()

    for i in file:
        i = i.split()[0]
        spam_det[i] += 1

    ip, count = spam_det.most_common(1)[0][0], spam_det.most_common(1)[0][1]
    print(f"Spammer {ip} - {count} times")