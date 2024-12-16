from collections import Counter
def filter_anagrams(word, words):
    word_counter = Counter(word)  # Считаем буквы в исходном слове
    list_anagrams = []

    for wd in words:
        wd_set = set(wd)
        if Counter(wd) == word_counter:
            list_anagrams.append(wd)
    return list_anagrams

print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))