from datetime import datetime, timedelta

# функция принимает:
# booked_dates — список строковых дат, недоступных для бронирования.
# Элементом списка является либо одиночная дата, либо период (две даты через дефис).
#
# date_for_booking — одиночная строковая дата или период (две даты через дефис),
# на которую гость желает забронировать номер.
#
# Функция is_available_date() должна возвращать True, если дата или период date_for_booking
# полностью доступна для бронирования. В противном случае функция должна возвращать False.

def is_available_date(booked_dates, date_for_booking):
    # Пустой список для строчных забронированных дат
    booked_dates_result = []
    for dt in booked_dates:
        if '-' in dt:   # если дата с тире
            start_date_str, end_date_str = dt.split('-')
            start_date = datetime.strptime(start_date_str, '%d.%m.%Y')  # Преобразуем строки в дату
            end_date = datetime.strptime(end_date_str, '%d.%m.%Y')

            # Добавляем все даты из диапазона в список
            current_date = start_date
            while current_date <= end_date:
                booked_dates_result.append(current_date.strftime('%d.%m.%Y'))  # Форматируем дату обратно в строку
                current_date += timedelta(days=1)  # Переходим к следующей дате

        else:  # Если дата без тире
            booked_dates_result.append(dt)  # Добавляем дату в список

        # Проверяем, является ли date_for_booking строкой
    if isinstance(date_for_booking, str):
        date_for_booking = [date_for_booking]  # Преобразуем строку в список

    # Пустой список для строчных дат на бронирование
    date_for_booking_result = []
    for dt in date_for_booking:
        if '-' in dt:
            start_date_str, end_date_str = dt.split('-')
            start_date = datetime.strptime(start_date_str, '%d.%m.%Y')  # Преобразуем строки в дату)
            end_date = datetime.strptime(end_date_str, '%d.%m.%Y')

            # Добавляем все даты из диапазона в список
            current_date = start_date
            while current_date <= end_date:
                date_for_booking_result.append(current_date.strftime('%d.%m.%Y')) # Форматируем дату обратно в строку
                current_date += timedelta(days=1) # Переходим к следующей дате
        else: # Если дата без тире
            date_for_booking_result.append(dt) # Добавляем дату в список

    # Проверяем пересечение дат в двух списках
    if set(booked_dates_result) & set(date_for_booking_result):
        return False # Если даты пересеклись и бронь недоступна
    else:
        return True  # Если бронь доступна

print(is_available_date(booked_dates=['04.11.2021', '05.11.2021-09.11.2021'], date_for_booking='01.11.2021-04.11.2021'))

