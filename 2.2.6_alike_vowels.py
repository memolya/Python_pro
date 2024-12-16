def find_similar_words(word, n, words):
    vowels = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'  # Гласные буквы русского языка

    # Функция для извлечения шаблона гласных и их позиций
    def get_vowel_pattern(word):
        return ''.join(['v' if char in vowels else '-' for char in word]).rstrip('-')
        # rstrip('-') удаляет лишние согласные после последней гласной

    # Получаем шаблон гласных для исходного слова
    word_pattern = get_vowel_pattern(word)

    # Находим слова с таким же шаблоном
    similar_words = []
    for w in words:
        if get_vowel_pattern(w) == word_pattern:
            similar_words.append(w)

    return similar_words


# Ввод данных
word = input()
n = int(input())
words = [input() for _ in range(n)]

# Вывод результата
result = find_similar_words(word, n, words)
print(*result, sep='\n')
