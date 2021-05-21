
# Вариант 1. Все возможные ключи и значения сразу записываются в словарь

def num_translate(k):
    my_dict = {"Zero": "Ноль", "One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять",
               "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять", "zero": "ноль",
               "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
               "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    print(my_dict.get(k))


num_translate(input("Введите число от 1 до 10 на английском: "))

# Вариант 2. Значения не дублируются для экономии памяти, ключ сверяется после приведения инпута в нижний регистр,
# если изначально его не удаётся найти

def num_translate_adv(n):
    my_dict1 = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
                "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if my_dict1.get(n) == None:
        n = n.lower()
        if my_dict1.get(n) == None:
            print(my_dict1.get(n))
        else:
            print(my_dict1[n].title())
    else: print(my_dict1[n])


num_translate_adv(input("Введите число от 1 до 10 на английском: "))
