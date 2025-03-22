from datetime import datetime

time_input = input()
# Объекты time напрямую не поддерживают вычитание — только объекты datetime
time_obj = datetime.strptime(time_input, '%H:%M:%S')

# Начало суток — это 00:00:00 того же дня
midnight = time_obj.replace(hour=0, minute=0, second=0)

# Разница между введённым временем и началом суток
delta = time_obj - midnight

# Получаем количество секунд
print(int(delta.total_seconds()))