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
        print(f"The length of the given {item.__class__.__name__} is {len(item)}\n")
    except TypeError as e:
        print(e)


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

    Thread(target=item_and_its_indices(my_list)).start()
    print()
    Thread(target=item_length(my_list)).start()

    given_string = "The Great Barrier Reef is visible from outer space."

    Thread(target=item_and_its_indices(given_string)).start()
    print()
    Thread(target=item_length(given_string)).start()


if __name__ == "__main__":
    execute_main()
