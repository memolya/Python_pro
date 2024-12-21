from datetime import date
def get_date_range(date1, date2):
    result = []
    if date1 > date2:
        return result
    else:
        for d in range(date1.toordinal(), date2.toordinal()+1):
            result.append(date.fromordinal(d))

    return result