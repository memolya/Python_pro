from datetime import date

def is_date_correct():
    # Собираем все результаты
    all_input = []

    while True:
        # Ввод даты
        dat = input()

        if dat == 'end':
            break

        try:
            # Разбиваем строку на день, месяц, год
            # дата подается в виде строки DD.MM.YYYY, порядок чисел не соответствует порядку
            # аргументов, ожидаемых функцией date().
            # Поэтому разбиваем строку на три части и явно указываем их соответствие

            day, month, year = map(int, dat.split('.'))

            # Проверяем, корректна ли дата
            # Функция date() принадлежит стандартной библиотеке Python datetime.
            # Она используется для создания объектов типа date, которые представляют дату без времени.
            # Эта функция проверяет, существует ли указанная дата в календаре.
            # Если дата некорректна (например, 32 января), будет выброшено исключение ValueError.
            # year, month, day - Это стандартный порядок аргументов для функции date() в Python.

            date(year, month, day)
            all_input.append('Корректная')
        except ValueError:
            all_input.append('Некорректная')

    # Выводим результаты
    for result in all_input:
        print(result)
    print(len([res for res in all_input if res == 'Корректная']))


# Запускаем функцию
is_date_correct()