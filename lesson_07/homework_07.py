# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def concatenation_func(num1, num2):
    return num1 + num2


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def arithmetic_average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse(raw_string):
    reversed_str = ""
    for char in reversed(raw_string):
        reversed_str = reversed_str + char

    return reversed_str


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(words_list):
    longest = words_list[0]
    for word in words_list:
        if len(word) > len(longest):
            longest = word

    return longest


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# task 7
def has_more_than_10_unique_chars(text):
    """
    Перевіряє, чи містить рядок більше 10 унікальних символів.

    Параметри:
    text (str): рядок для перевірки

    Повертає:
    bool: True, якщо унікальних символів більше 10, інакше False
    """
    unique_count = len(set(text))
    return unique_count > 10


# Отримуємо рядок від користувача
user_input = input("Введіть рядок: ")
print(has_more_than_10_unique_chars(user_input))


# task 8
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


# task 9
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


# task 10
def sentence_in_order_lower_case(text, i):
    """
    Виводить необхідне по порядку речення та перетворює його у нижній регістр.

    Параметри:
    text (str): рядок, який перевіряємо

    Повертає:
    str: викликане необхідне речення, написане нижнім регістром
    """

    splitted_sentences = text.split(". ")
    return splitted_sentences[i].lower()
