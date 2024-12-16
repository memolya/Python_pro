from collections import defaultdict


def convert_to_bytes(size, unit):
    """Конвертирует размер в байты"""
    units = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
    return size * units[unit]


def convert_from_bytes(size_in_bytes):
    """Переводит размер из байт в максимальные возможные единицы с округлением вниз"""
    if size_in_bytes >= 1024 ** 3:
        return round(size_in_bytes / 1024 ** 3), 'GB'
    elif size_in_bytes >= 1024 ** 2:
        return round(size_in_bytes / 1024 ** 2), 'MB'
    elif size_in_bytes >= 1024:
        return round(size_in_bytes / 1024), 'KB'
    else:
        return size_in_bytes, 'B'


def process_files(file_path):
    # Считываем файл
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Группировка по расширениям
    grouped_files = defaultdict(list)
    sizes = defaultdict(int)

    for line in lines:
        name, size, unit = line.rsplit(maxsplit=2)
        name, extension = name.rsplit('.', maxsplit=1)
        size = int(size)

        # Конвертируем размер в байты
        size_in_bytes = convert_to_bytes(size, unit)

        # Добавляем файл в соответствующую группу
        grouped_files[extension].append((name, size_in_bytes))

        # Суммируем общий размер
        sizes[extension] += size_in_bytes

    # Сортировка групп и файлов в группах
    sorted_extensions = sorted(grouped_files.keys())
    for extension in sorted_extensions:
        # Вывод файлов
        for name, _ in sorted(grouped_files[extension]):
            print(f"{name}.{extension}")

        print("----------")
        # Вычисление суммарного размера
        total_size, unit = convert_from_bytes(sizes[extension])
        print(f"Summary: {total_size} {unit}\n")


# Запуск
process_files('files.txt')

