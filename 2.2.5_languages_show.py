people = int(input())
all_languages = []
result = []

for person in range(1, people+1):
    languages = input()
    languages = languages.replace(',', ' ')
    languages_person = languages.split()

    for lang in languages_person:
        all_languages.append(lang)

for lang in all_languages:
    count = all_languages.count(lang)
    if count == people and lang not in result:
        result.append(lang)
        
if not result:
    print('Сериал снять не удастся')
else:
    result.sort()
    print(*result, sep = ', ')
