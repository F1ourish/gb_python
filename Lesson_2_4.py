list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

idx = 0

while idx < len(list):
    hello = list[idx].split(' ').pop()
    print("Привет, ", hello.title(), "!")
    idx += 1