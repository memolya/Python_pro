from datetime import datetime

# Считываем файл - Содержимое всего файла в переменной content
with open('diary.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Разбиваем содержимое файла по двойному переходу на строки
entries = content.split('\n\n')

# Функция для извлечения ключа для сортировки
# Из каждой строки извлекаем дату, которая находится в начале строки
# и переводим её в формат datetime

def extract_date(entry):
    first_line = entry.split('\n')[0]  # Берем первую строку записи
    date_part = first_line.strip()      # Убираем пробелы
    return datetime.strptime(date_part, '%d.%m.%Y; %H:%M')

# Сортируем записи по дате
sorted_entries = sorted(entries, key=extract_date)

# Печатаем отсортированный список записей
for entry in sorted_entries:
    print(entry)
    print()  # Добавляем пустую строку между записями
