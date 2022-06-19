"""Outputs the item length and its indices"""

import my_python_modules as mpm


def item_and_its_indices(item):
    """Logs item and its indices"""
    for index, value in enumerate(item):
        print(f"index[{index}] = {value}")


def item_length(item):
    """Logs length of the given item"""
    if isinstance(item, str | list | dict):
        print(f"The length of the given item is {len(item)}\n")


def main():
    """Main function"""

    my_list = [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1_597,
        2_584,
        4_181,
        6_765,
    ]

    mpm.operate(item_and_its_indices, my_list)
    print()
    mpm.operate(item_length, my_list)

    string = "The Master and Margarita"

    mpm.operate(item_and_its_indices, string)
    print()
    mpm.operate(item_length, string)


if __name__ == "__main__":
    main()
