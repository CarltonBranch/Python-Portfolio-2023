"""               +-------------------------+
                  ¦ 34 ¦ 21 ¦ 32 ¦ 41 ¦ 25  ¦
                  +----+----+----+----+-----¦
                  ¦ 14 ¦ 42 ¦ 43 ¦ 14 ¦ 31  ¦
                  +----+----+----+----+-----¦
                  ¦ 54 ¦ 45 ¦ 52 ¦ 42 ¦ 23  ¦
                  +----+----+----+----+-----¦
                  ¦ 33 ¦ 15 ¦ 51 ¦ 31 ¦ 35  ¦
                  +----+----+----+----+-----¦
                  ¦ 21 ¦ 52 ¦ 33 ¦ 13 ¦ 23  ¦
                  +-------------------------+"""

# Do you like treasure hunts? In this problem you are to write a program to
# explore the above array for a treasure. The values in the array are clues.
# Each cell contains an integer between 11 and 55; for each value the ten's
# digit represents the row number and the unit's digit represents the column
# number of the cell containing the next clue. Starting in the upper left
# corner (at 1,1), use the clues to guide your search of the array.
# (The first three clues are 11, 34, 42).
# The treasure is a cell whose value is the same as its coordinates.
# Your program must first read in the treasure map data into a 5 by 5 array.
# Your program should output the cells it visits during its search,
# and a message indicating where you found the treasure.


def sum_digits(num):
    """Utility funciton to sum the first and second digit of each 2-digit clue

    Args:
        num (_type_): 2 digit clue

    Returns:
        _type_: int sum of the digit values
    """
    return (num % 10) + (num // 10)


def find_treasure(treasure_map, **kwargs):
    """Recursively search through the map using the clues to determine
    the next search location

    Args:
        treasure_map: 2d matrix to search, row position, column
        position, search_count to prevent stack overlow if treasure not
        found

    Returns:
        String: Cell where the sum of the two digits equals the
        sum of its coordinates
    """
    row = kwargs["row"]
    col = kwargs["col"]
    # determine the current cursor value (the matrix values are 1-indexed)
    cursor = treasure_map[row - 1][col - 1]

    # search_count is only present during recursive searches
    if "search_count" in kwargs:
        search_count = kwargs["search_count"]
    else:
        search_count = 1

    # determine the sum of the digits
    sum_cursor = sum_digits(cursor)
    # check if the sum of the cell position digits
    # equals the sum of the cell value digits

    if sum_cursor == row + col:
        return f'The treasure was found at position: ({kwargs["row"]}, {kwargs["col"]})'

    # search_count prevents stack overflow by enforcing a maximum number
    # of searches assuming no cycles
    if search_count == len(treasure_map) * len(treasure_map[0]):
        return "The treasure was not found!"
    else:
        print(f"Searched...{cursor}")
        search_count += 1
        return find_treasure(
            treasure_map, row=cursor // 10, col=cursor % 10, search_count=search_count
        )


target_map = [
    [34, 21, 32, 41, 25],
    [14, 42, 43, 14, 31],
    [54, 45, 52, 42, 23],
    [33, 15, 51, 31, 35],
    [21, 52, 33, 13, 23],
]

print(find_treasure(target_map, row=1, col=1))  # correct answer is 4,2
