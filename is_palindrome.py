def is_palindrome(word):
    right_word = word.lower()
    reversed_word = right_word[::-1]
    return right_word == reversed_word


def is_not_palindrome(word):
    return not is_palindrome(word)
