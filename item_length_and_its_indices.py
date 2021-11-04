from my_python_modules import operate



def item_and_its_indices(item):
    """Logs item and its indices"""
    for index, value in enumerate(item):
        print(f"index[{index}] = {value}")


"""Logs length of the given item"""


def item_length(item):
    if isinstance(item, str):
        print(f"The length of the given string is {len(item)}")
    elif isinstance(item, list):
        print(f"The length of the given list is {len(item)}")
    elif isinstance(item, dict):
        print(f"The length of the given dictionary is {len(item)}")


# Invokes higher order functions for the given type of item"""

my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
           144, 233, 377, 610, 987, 1_597, 2_584, 4_181, 6_765]

operate(item_and_its_indices, my_list)
operate(item_length, my_list)


string = "The Master and Margarita"

operate(item_and_its_indices, string)
operate(item_length, string)
