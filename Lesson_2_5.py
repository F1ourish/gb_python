prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

idx = 0
prices_formated = []

#Пункт A:
while idx < len(prices):
    if prices[idx] % 1 > 0:
        penny = int(prices[idx] * 100) % 100
        rub = int(prices[idx] // 1)
        var = f' {rub} руб. {penny:02d} коп.'.format(rub=rub, penny=penny)
        prices_formated.append(var)
        idx += 1
    else:
        var = f' {prices[idx]} руб. 00 коп.'
        prices_formated.append(var)
        idx += 1

idx += 1

print(','.join(prices_formated))

#Пункт B:
print('id до сортировки:', id(prices))
prices.sort()
print(prices)
print('id после сортировки:',id(prices))

#Пункт C:
prices_reversed = list(reversed(prices))
print(prices_reversed)

#Пункт D:
print(prices[25:31])

