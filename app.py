import string
from collections import Counter

def analyze_text_file(file_path, top_n=10):
    word_counter = Counter()
    translator = str.maketrans('', '', string.punctuation)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.lower().translate(translator)
                words = cleaned_line.split()
                word_counter.update(words)

        print(f"\nОбщая статистика по словам ({len(word_counter)} уникальных слов):\n")
        for word, count in word_counter.most_common():
            print(f"{word}: {count}")

        print(f"\nТОП {top_n} самых частых слов:\n")
        for word, count in word_counter.most_common(top_n):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Ошибка при анализе файла: {e}")

file_path = 'your_text_file.txt'  
analyze_text_file(file_path)
