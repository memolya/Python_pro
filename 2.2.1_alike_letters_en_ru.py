en = 'AaBCcEeHKMOoPpTXxy'
ru = 'АаВСсЕеНКМОоРрТХху'

letter_1, letter_2, letter_3 = input(), input(), input()
if letter_1 in en and letter_2 in en and letter_3 in en:    # Проверка каждой буквы (letter_1, letter_2, letter_3) должна быть независимой.
                                                            # Конструкция: if letter_1 and letter_2 and letter_3 in en:
                                                            # означает, что проверяется, являются ли letter_1 и letter_2 истинными значениями, а затем только проверяется, содержится ли letter_3 в строке en.
    print('en')
elif letter_1 in ru and letter_2 in ru and letter_3 in ru:
    print('ru')
else:
    print('mix')

