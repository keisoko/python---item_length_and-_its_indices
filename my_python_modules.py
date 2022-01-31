from pipe import traverse

def flat_list_of_lists_sorted(nested_list):
    return sorted(list(nested_list | traverse))


def flat_list_of_lists_unsorted(nested_list):
    return list(nested_list | traverse)


def operate(func, item):
    return func(item)
