def spell(*words):

    list_all = []
    for word in words:
        list_all.append(f'{word[0].lower()} : {len(word)}')

    result_dict = {}

    for item in list_all:
        key, value = item.split(':')
        key = key.strip()
        value = int(value.strip())

        if key in result_dict:
            result_dict[key] = max(result_dict[key], value)  # Сохраняем максимальное значение
                                                             # result_dict[key]: Текущее значение, которое уже хранится в словаре под ключом key.
                                                             # value: Новое значение, которое нужно сравнить с текущим.
        else:
            result_dict[key] = value

    return result_dict

words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))