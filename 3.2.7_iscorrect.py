from datetime import date

def is_correct(day, month, year):
    # Корректная дата
    try:
        # Сначала год, потом месяц, потом день
        my_date = date(int(year), int(month), int(day))
        return True

    # перехватываем ошибку типа ValueError
    except ValueError:
        return False


print(is_correct(31, 12, 2021)) # True
#print(is_correct(31, 13, 2021)) # False