# счетчик для нужного количества ураганов
early_hurricanes = 0

# цикл по датам в которые был ураган
for hurricane_date in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane_date.month < 6:
        early_hurricanes += 1

print(early_hurricanes)