def my_func(name, surname, date, city, email, tel):
    return '_'.join([name, surname, date, city, email, tel])

print(my_func(surname = 'Аноним', name = 'Илюша', tel = '891111111б', date = '1987', city = 'Париж', email = '404@mail.ru'))
