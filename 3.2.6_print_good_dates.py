from datetime import date

def print_good_dates(dates):
    result = []
    # Если на ввод передан пустой список
    if not dates:
        return
    else:
        for i in dates:
            if i.year == 1992 and i.day + i.month == 29:
                result.append(i)

    # Если нет интересных дат - не выводить ничего
    if not result:
        return
    # Если интересные даты есть
    else:
        for res in sorted(result):
            print(res.strftime('%B %d, %Y'))


print_good_dates(dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)])