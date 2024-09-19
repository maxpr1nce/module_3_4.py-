def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для результата
    root_word_lower = root_word.lower()  # Приводим корневое слово к нижнему регистру для сравнения

    for word in other_words:
        word_lower = word.lower()  # Приводим каждое слово к нижнему регистру для сравнения
        # Условие для добавления слова в список
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем слово в результирующий список

    return same_words  # Возвращаем список с подходящими словами

# Пример вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
