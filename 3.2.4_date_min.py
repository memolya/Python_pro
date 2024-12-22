from datetime import date

# Ввод дат в формате ISO
date_1, date_2 = input(), input()

# Преобразование строки в дату
date_1 = date.fromisoformat(date_1)
date_2 = date.fromisoformat(date_2)

result = min(date_1, date_2)
# Вывод типа "04-05 (2021)"
print(result.strftime('%d-%m (%Y)'))