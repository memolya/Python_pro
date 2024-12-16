def repeated(numbers):
    repeated_nums = []
    unique_nums = []

    for num in numbers:
        count = numbers.count(num)
        if count > 1:
            repeated_nums.append(num)

    for num in repeated_nums:
        if num not in unique_nums:
            unique_nums.append(num)

    if not unique_nums: #проверка на пустой список уникальных номеров (повторов не было)
        return []       #Если список пуст, print(*[]) просто не выводит ничего, что является корректным поведением.
    else:
        result = sorted(map(int, unique_nums))
        return result


print(*repeated(numbers=input().split())) #возвращаем распакованный список