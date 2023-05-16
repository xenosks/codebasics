def is_palindrome(word):
    right_word = word.lower()
    reversed_word = right_word[::-1]
    return right_word == reversed_word


def is_not_palindrome(word):
    return not is_palindrome(word)


def print_reversed_word_by_symbol(word):
    i = len(word) - 1
    while i >= 0:
        print(word[i])
        i = i - 1


def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string[index].upper() == char.upper():
            count = count + 1
        index = index + 1
    return count