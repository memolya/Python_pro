def likes(names):
    multiple_like = ' оценили данную запись'

    if not names:
        return 'Никто не оценил данную запись'
    else:
        if len(names) == 1:
            return f'{names[0]} оценил(а) данную запись'
        elif len(names) == 2:
            return f'{names[0]} и {names[1]}' + multiple_like
        elif len(names) == 3:
            return f'{names[0]}, {names[1]} и {names[2]}' + multiple_like
        else:
            return f'{names[0]}, {names[1]} и {int(len(names)-2)} других' + multiple_like

print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))