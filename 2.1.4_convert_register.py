def convert(text):
    counter_lower = 0
    counter_upper = 0

    for symbol in text:
        if symbol.islower():
            counter_lower += 1
        elif symbol.isupper():
            counter_upper += 1

    if counter_lower > counter_upper or counter_lower == counter_upper:
        return text.lower()
    else:
        return text.upper()

# print(convert('pi31415!'))