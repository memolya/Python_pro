def index_of_nearest(numbers, number):
    if not numbers:
        return -1  # Если список пуст, возвращаем -1

    # Вычисляем модуль разницы для каждого элемента и находим минимальную
    differences = [abs(x - number) for x in numbers]
    # print(differences) - список из разниц оригинальных чисел с переданным числом, новые числа на тех же местах, что и старые
    min_difference = min(differences)

    # Находим индекс первого элемента с минимальной разницей
    return differences.index(min_difference) #Метод list.index() возвращает индекс первого вхождения минимальной разницы

# Тесты:
print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0))  # Ожидаемый результат: 3

