from my_python_modules import operate


def item_and_its_indices(item):
    """Logs item and its indices"""
    for index, value in enumerate(item):
        print(f"index[{index}] = {value}")


def item_length(item):
    """Logs length of the given item"""
    if isinstance(item, (str, list, dict)):
        print(f"The length of the given item is {len(item)}\n")

# Invokes higher order functions for the given type of item"""

my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
           144, 233, 377, 610, 987, 1_597, 2_584, 4_181, 6_765]

operate(item_and_its_indices, my_list)
operate(item_length, my_list)


string = "The Master and Margarita"

operate(item_and_its_indices, string)
operate(item_length, string)
