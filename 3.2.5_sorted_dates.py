from datetime import date

dates_amount = int(input())
dates_original = []

# Прием дат в ISO формате
for _ in range(dates_amount):
    dat = input()
    dat = date.fromisoformat(dat)
    dates_original.append(dat)

# Сортировка в порядке неубывания
dates_sorted = sorted(dates_original)

# Вывод дат в формате DD/MM/YYYY
for item in dates_sorted:
    print(item.strftime('%d/%m/%Y'))
