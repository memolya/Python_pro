# Передаваемый в функцию кортеж легко составить по мнемоническому правилу: один, два, пять. Например:
#
# для слова «арбуз»: арбуз, арбуза, арбузов
# для слова «рубль»: рубль, рубля, рублей

def choose_plural(amount, declensions):
    amount_df = str(amount)[-1]
    amount_df_last_2 = str(amount)[-2:]

    if 11 <= int(amount_df_last_2) <= 19:   #если предпоследняя цифра - единица - действует правило падежа на "пять"
        return f'{amount} {declensions[2]}'
    else:
        if int(amount_df) == 1:
            return f'{amount} {declensions[0]}'
        elif 2 <= int(amount_df) <= 4:
            return f'{amount} {declensions[1]}'

        else:
            return f'{amount} {declensions[2]}'

print(choose_plural(1223123111, ('пример', 'примера', 'примеров')))