from my_python_modules import operate

"""Logs item and its indices with the integer and float thousand separator"""


def item_and_its_indices(item: any) -> any:
    for index, value in enumerate(item):
        if type(value) == int or type(value) == float:
            print(f"index[{index}] = {value:,}")
        else:
            print(f"index[{index}] = {value}")


"""Logs length of the given item"""


def item_length(item: any) -> any:
    if type(item) == str:
        print(f"The length of the given string is {len(item)}")
    if type(item) == list:
        print(f"The length of the given list is {len(item)}")
    if type(item) == dict:
        print(f"The length of the given dictionary is {len(item)}")


"""invokes higher order functions for the given type of item"""

my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
           144, 233, 377, 610, 987, 1_597, 2_584, 4_181, 6_765]

operate(item_and_its_indices, my_list)
operate(item_length, my_list)


string = "The Master and Margarita"

operate(item_and_its_indices, string)
operate(item_length, string)
