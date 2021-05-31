# ******* 1е задание с yield *******

def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num


for i in odd_nums(int(input())):
    print(i)


# ******* 2е задание без yield *******

var = int(input())

print(*[num for num in range(1, var + 1, 2)])