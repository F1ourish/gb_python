list = ['в', '5', 'часов', '07', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']

idx = 0

while idx < len(list):
    if list[idx].isdigit() == True:                      #Проверяю, число ли это вообще
        if int(list[idx]) // 10 > 0:                     #Проверяю, есть ли десятки
            var = f"'{list[idx]}'"
            list.remove(list[idx])
            list.insert(idx, var)
            idx += 1
        else:                                            #Если десятков нету, добавляю 0 до 2х знаков
            var = f"'{int(list[idx]):02}'"
            list.remove(list[idx])
            list.insert(idx, var)
            idx += 1

    elif list[idx].replace('+', '').isdigit() == True:  #Проверяю, есть ли в строке число с +
            var = "'+" + f"{int(list[idx]):02d}'"
            list.remove(list[idx])
            list.insert(idx, var)
            idx += 1

    elif list[idx].replace('-', '').isdigit() == True:  #Проверяю, есть ли в строке число с -, по факту эту проверку можно выполнять просто через int, т.к. отрицательные числа могут быть типа int, собственно дальше берётся модуль числа и вручную приписывается знак - :)
            var = "'-" + f"{abs(int(list[idx])):02d}'"
            list.remove(list[idx])
            list.insert(idx, var)
            idx += 1

    else:
        idx += 1

print(' '.join(list))