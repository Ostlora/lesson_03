def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите циыфры через проблем, для завершения нажмите "!" - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == '!':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Ну и результат = {sum_res}')
    print(f'Итого =  {sum_res}')


my_sum()