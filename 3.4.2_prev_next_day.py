from datetime import datetime, timedelta

date_input = input()

date_obj = datetime.strptime(date_input, '%d.%m.%Y').date()  # Преобразуем в объект date

prev_day = date_obj - timedelta(days=1)
next_day = date_obj + timedelta(days=1)

print(prev_day.strftime('%d.%m.%Y'), next_day.strftime('%d.%m.%Y'), sep='\n')
