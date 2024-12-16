# Ввод данных
n, X, Y, A, B = map(int, input("Введите n, X, Y, A, B через пробел: ").split())

# Формируем последовательность чисел от 1 до n
sequence = list(range(1, n + 1))

# Переворачиваем элементы с индексов X до Y (учитываем, что индексация в Python с 0)
sequence[X - 1:Y] = reversed(sequence[X - 1:Y])

# Переворачиваем элементы с индексов A до B
sequence[A - 1:B] = reversed(sequence[A - 1:B])

# Выводим итоговую последовательность
print(" ".join(map(str, sequence)))
