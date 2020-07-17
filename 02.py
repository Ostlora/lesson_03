def my_func(name, surname, date, city, email, tel):
    surname = input("введите фамилию - ")
    name = input("введите имя - ")
    date = input("введите дату рождения - ")
    city = input("введите город проживания - ")
    email = input("введите email -  ")
    tel = input("введите телефон - ")
    return '_'.join([name, surname, date, city, email, tel])

print(my_func(surname = '', name = '', tel = '', date = '', city = '', email = ''))
