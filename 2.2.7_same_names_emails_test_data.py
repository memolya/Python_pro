def check_same_names():
    existing_mails_num = 3
    existing_mails = ['ivan-petrov@beegeek.bzz', 'petr-ivanov@beegeek.bzz', 'ivan-petrov1@beegeek.bzz',
                      'ivan-ivanov@beegeek.bzz', 'ivan-ivanov1@beegeek.bzz', 'ivan-ivanov2@beegeek.bzz']
    new_employees_num = 2
    new_employees = ['ivan-ivanov', 'petr-petrov', 'petr-ivanov']

    # Функция map применяет указанную функцию (lambda) ко всем элементам списка.
    # lambda вызывает метод .replace() для каждого элемента списка.
    # x — параметр функции. В данном случае x принимает значение каждого элемента из списка existing_mails.
    # : — разделяет параметры функции и её тело.
    # x.replace('@beegeek.bzz', '') — тело функции. Оно описывает, что должно быть возвращено:
    # Для строки x, метод .replace('@beegeek.bzz', '') заменяет подстроку @beegeek.bzz на пустую строку (''), удаляя её.
    # map применяет эту lambda функцию к каждому элементу списка emails.
    cleaned_emails = list(map(lambda x: x.replace('@beegeek.bzz', ''), existing_mails))
    print(sorted(cleaned_emails))

    counter = 0 # Считаем кол-во попаданий тезок в списке почтовых ящиков
    for name in new_employees:
        for email in existing_mails:
            if name not in email:
                counter = 0
            else:
                counter += 1
        if counter == 0:
            new_employee_mail = f'{name}@beegeek.bzz'
            print(new_employee_mail)
            existing_mails.append(new_employee_mail)
        else:
            new_employee_mail = f'{name}{counter}@beegeek.bzz'
            print(new_employee_mail)
            existing_mails.append(new_employee_mail)

check_same_names()