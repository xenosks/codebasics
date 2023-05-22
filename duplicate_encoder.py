def duplicate_encode(string):
    string = string.lower()  # Convert the string to lowercase to ignore capitalization
    new_string = ""

    for char in string:
        if string.count(char) > 1:
            new_string += ")"
        else:
            new_string += "("

    return new_string