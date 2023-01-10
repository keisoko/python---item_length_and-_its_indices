"""Outputs the item length and its indices"""

from threading import Thread


def item_and_its_indices(item):
    """Logs item and its indices"""
    for index, value in enumerate(item):
        if isinstance(value, int | float):
            print(f"index[{index}] = {value:,}")
        else:
            print(f"index[{index}] = {value}")


def item_length(item):
    """Logs length of the given item"""
    try:
        print(f"The length of the given {type(item).__name__} is {len(item)}\n")
    except TypeError as e:
        print(e)


def combined_execution(function_parameter):
    Thread(target=item_and_its_indices(function_parameter)).start()
    print()
    Thread(target=item_length(function_parameter)).start()


def execute_main():
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

    combined_execution(my_list)

    given_string = "The Great Barrier Reef is visible from outer space."

    combined_execution(given_string)


if __name__ == "__main__":
    execute_main()
