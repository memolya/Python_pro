def max_group_length(n):
    groups = {}

    # Группируем числа по сумме их цифр
    for num in range(1, n + 1):
        digit_sum = sum(int(d) for d in str(num))  # Сумма цифр числа
        if digit_sum not in groups:     # Проверяется, есть ли уже ключ digit_sum в словаре groups.
                                        # Если такого ключа ещё нет, создаётся новая запись в словаре:

            groups[digit_sum] = []      # Это создаёт пустой список для хранения чисел, сумма цифр которых равна digit_sum.

        groups[digit_sum].append(num)   # В список, связанный с ключом digit_sum, добавляется текущее число num.
                                        # Если ключ уже существует, число просто добавляется в существующий список.

    # Находим максимальную длину группы
    max_length = max(len(group) for group in groups.values())

    return max_length


# Ввод числа n
n = int(input())
print(max_group_length(n))
