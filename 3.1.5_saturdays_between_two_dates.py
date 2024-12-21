from datetime import date

def saturdays_between_two_dates(date1, date2):
    # Счетчик суббот
    counter_saturdays = 0

    # Упорядочиваем даты
    start, end = min(date1, date2), max(date1, date2)

    # Перебираем даты от start до end включительно
    for ordinal in range(start.toordinal(), end.toordinal()+1):
        current_date = date.fromordinal(ordinal)
        if current_date.weekday() == 5:
            counter_saturdays += 1

    return counter_saturdays

print(saturdays_between_two_dates(date1 = date(2021, 11, 1), date2 = date(2021, 11, 22)))