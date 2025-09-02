def starts_with_by_the_time(text):
    """
    Перевіряє, чи починається хоча б одне речення в тексті з "By the time".

    Параметри:
    text (str): рядок, який перевіряємо

    Повертає:
    str: повідомлення про наявність речення, що починається з "By the time"
    """
    # Розбиваємо текст на речення
    splitted_sentences = text.split(". ")

    # Перевіряємо кожне речення
    for sentence in splitted_sentences:
        if sentence.startswith("By the time"):
            return "Рядок починається з 'By the time'"

    # Якщо жодне речення не починається з "By the time"
    return "Рядок не починається з 'By the time'"


def starts_by_title(text):
    """
    Виводить скільки слів у тексті починається з Великої літери

    Параметри:
    text (str): рядок, який перевіряємо

    Повертає:
    int: кількість слів, що починаються з великої літери
    """

    count = 0
    for word in text:
        if word[0].isupper():
            count += 1
    return count


def sentence_in_order_lower_case(text, i):
    splitted_sentences = text.split(". ")
    try:
        return splitted_sentences[i].lower()
    except IndexError:
        return None

def reverse(raw_string):
    reversed_str = ""
    for char in reversed(raw_string):
        reversed_str = reversed_str + char

    return reversed_str


def longest_word(words_list):
    longest = words_list[0]
    for word in words_list:
        if len(word) > len(longest):
            longest = word

    return longest
