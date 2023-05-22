def swap_name(string):
    name_list = string.split()
    if len(name_list) < 2:
        return string
    else:
        first_name = name_list[0]
        last_name = name_list[-1]
        name_list[0] = last_name
        name_list[-1] = first_name
        swapped_name = ' '.join(name_list)
        return swapped_name
