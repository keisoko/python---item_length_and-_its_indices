def flat_list_of_lists_sorted(my_list):
    my_list = [item for sublist in my_list for item in sublist]
    my_list.sort()
    return my_list


def flat_list_of_lists_unsorted(my_list):
    my_list = [item for sublist in my_list for item in sublist]
    return my_list


def operate(func, item):
    result = func(item)
    return result
