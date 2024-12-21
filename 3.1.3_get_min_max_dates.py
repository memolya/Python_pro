from datetime import date
def get_min_max(dates):
    # кортеж для результата
    result = []
    # вывод min и max дат
    if dates:
        result.append(min(dates))
        result.append(max(dates))
        # список в кортеж
        result_tuple = tuple(result)
        return result_tuple
    # вывод пустого кортежа, если список дат пустой
    else:
        return tuple(result)