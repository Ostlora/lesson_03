def my_fun(x, y, z):
    t = min(x, y, z)
    res = (x + y + z) - t
    return res

print(f'Сумма наибольших двух аргументов - {my_fun(int(input("введите первое число -  ")), int(input("введите второе число - ")), int(input("введите третье число - ")))}')