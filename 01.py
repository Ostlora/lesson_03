def my_funс():
    try:
        arg_1 = int(input("введите первое число "))
        arg_2 = int(input("введите второе число "))
        res = arg_1 / arg_2
    except ValueError:
        print('Нужно вводить только цифры')
    except ZeroDivisionError:
        return 'Грешно делить на ноль'
    else:
        print('Все хорошо')
        return res

print(f'Ну и результат = {my_funс()}')
