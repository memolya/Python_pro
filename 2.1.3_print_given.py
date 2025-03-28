def print_given(*args, **kwargs):   #При использовании **kwargs в определении функции все именованные аргументы, переданные в функцию, автоматически упаковываются в словарь.
                                    # Ключами в этом словаре становятся имена аргументов, а значениями — их соответствующие значения.
                                    #Один астериск (*) используется для передачи произвольного количества позиционных аргументов в функцию. Делает кортеж.
                                    # Два астериска (**) используются для передачи произвольного количества именованных аргументов. Делает словарь.
    if not args and not kwargs:     #Если в функцию ничего не передается, функция ничего не должна выводить.
        return
    else:
        for arg in args:    #При выводе сначала должны следовать все позиционные аргументы, затем — все именованные.
            print(f'{arg} {type(arg)}')

        for karg in sorted(kwargs.keys()):  #При выводе позиционные аргументы должны быть расположены в порядке их передачи,
                                            # именованные — в лексикографическом порядке имен переменных.
            print(f'{karg} {kwargs[karg]} {type(kwargs[karg])}') #можно сказать, что именованные аргументы (**kwargs) в Python работают как словарь, где:
                                                                 # Ключи — это имена аргументов.
                                                                 # Значения — это переданные значения для этих аргументов.
                                                                 # Когда функция принимает именованные аргументы с помощью **kwargs, все переданные аргументы упаковываются в словарь, с которым можно работать, как с любым другим объектом dict.

print_given(1, [1, 2, 3], 'three', two=2)