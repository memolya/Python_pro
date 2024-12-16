def hide_card(card):
    card_number = card.replace(' ', '')
    card_number = '*'*12 + card_number[12:]
    return card_number

print(hide_card(card=input()))

# def hide_card(card):
#     return '*' * 12 + card.replace(' ', '')[-4:]