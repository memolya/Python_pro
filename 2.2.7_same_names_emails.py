def check_same_names():

    # Ввод существующих ящиков
    existing_mails_num = int(input())
    existing_mails = []

    for _ in range(existing_mails_num):
        existing_mail = input()
        existing_mails.append(existing_mail)

    # Ввод имен новых сотрудников
    new_employees_num = int(input())
    new_employees = []

    for _ in range(new_employees_num):
        new_employee_name = input()
        new_employees.append(new_employee_name)

    # Чистим почты от @beegeek.bzz

        # Функция map применяет указанную функцию (lambda) ко всем элементам списка.
        # lambda вызывает метод .replace() для каждого элемента списка.
        # x — параметр функции. В данном случае x принимает значение каждого элемента из списка existing_mails.
        # : — разделяет параметры функции и её тело.
        # x.replace('@beegeek.bzz', '') — тело функции. Оно описывает, что должно быть возвращено:
        # Для строки x, метод .replace('@beegeek.bzz', '') заменяет подстроку @beegeek.bzz на пустую строку (''), удаляя её.
        # map применяет эту lambda функцию к каждому элементу списка emails.
    cleaned_emails = sorted(list(map(lambda x: x.replace('@beegeek.bzz', ''), existing_mails)))

    # Проверяем, есть ли имя в списке существующих почт
    for name in new_employees:
        counter = 0  # Счетчик тезок в списке почтовых ящиков, обнуляется после проверки каждого имени
        for email in cleaned_emails:
            # Если нет - продолжаем цикл
            if email not in name:
                counter += 0
            # Если нашли - прекращаем
            else:
                counter += 1
                break

        if counter == 0:
            new_email = f'{name}@beegeek.bzz'
            print(new_email)
            existing_mails.append(new_email)
            # Добавляем очищенный имейл в список для проверки следующих имен
            cleaned_emails.append(new_email.replace('@beegeek.bzz', ''))

        else:
            for _ in range(1, 20):
                new_email = f'{name}{_}@beegeek.bzz'

                if new_email not in existing_mails:
                    print(new_email)
                    existing_mails.append(new_email)
                    cleaned_emails.append(new_email.replace('@beegeek.bzz', ''))
                    break
                # Перебираем индексы, пока не найдем незанятый
                else:
                    continue

check_same_names()
