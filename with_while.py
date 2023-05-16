def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')


def print_numbers(last_number):
    # i сокращение от index (порядковый номер)
    # используется по общему соглашению во множестве языков
    # как счетчик цикла
    i = 1
    while i <= last_number:
        print(i)
        i = i + 1
    print('finished!')


def multiply_numbers_from_range(start, finish):
    i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i + 1
    return result


def join_numbers_from_range(start, end):
    i = start
    result = ''
    while i <= end:
        result = result + str(i)
        i = i + 1
    return result
