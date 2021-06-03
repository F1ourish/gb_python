# ****** Эту задачу полностью пришлось смотреть разбор, самому доделать не получилось, дошёл до 3го цикла if и завис

from sys import  argv

with open("bakery.csv", "a", encoding="utf-8") as file_a:
    with open("bakery.csv", "r", encoding="utf-8") as file_r:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace('.', '').isdigit()]:
            if len(argv) == 3:
                print(*file_r.read().split()[int(argv[1]) - 1:int(argv[2])], sep='\n')
            if ',' in argv[1] or '.' in argv[1]:
                print(argv[1], file=file_a)
            else:
                print(*file_r.readlines()[int(argv[1]) - 1:], sep='')
        else:
            print(file_r.read())