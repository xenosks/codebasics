def normalize_url(url):
    prefix = 'https://'
    if url[:8] == prefix:
        return url
    else:
        if url[:7] == 'http://':
            return prefix + url[7:]
        else:
            return prefix + url


def my_substr(string, length):
    result_string = ''
    index = 0
    while index < length:
        result_string = result_string + string[index]
        index = index + 1

    return result_string

