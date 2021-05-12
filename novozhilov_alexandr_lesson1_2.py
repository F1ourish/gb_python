num = []

idx = 0

while idx < 1_000:
    if idx % 2 != 0:
        num.append(idx ** 3)
    idx += 1

print("Список кубов нечётных чисел: ", num)

idx = 0
sum1 = 0
sum2 = 0

for idx in range(len(num)):
    var1 = num[idx]
    var2 = num[idx] + 17
    multi1 = 0
    multi2 = 0
    while var1 > 0 or var2 > 0:
        multi1 += var1 % 10
        var1 //= 10
        multi2 += var2 % 10
        var2 //= 10
    if multi1 % 7 == 0:
        sum1 += num[idx]
    elif multi2 % 7 ==0:
        sum2 += num[idx] + 17

print("Сумма всех чисел, сумма цифр которых кратна 7: ", sum1, ". Сумма всех чисел, сумма цифр которых кратна 7 после прибавки к ним 17: ", sum2)


