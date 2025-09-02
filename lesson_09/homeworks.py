def starts_with_by_the_time(text):
    splitted_sentences = text.split(". ")

    for sentence in splitted_sentences:
        if sentence.startswith("By the time"):
            return "Рядок починається з 'By the time'"

    return "Рядок не починається з 'By the time'"


def starts_by_title(text):
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
