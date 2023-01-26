"""
Write a program to search for the "saddle points" in a 5 by 5 array of
integers.

A saddle point is a cell whose
value is greater than or equal to any in its row,
and less than or equal to any in its column.

There may be more than one saddle point in the array.
Print out the coordinates of any saddle points your program finds.
Print out "No saddle points" if there are none.
"""


def process_row_max(row, column):
    """Reads a row of data and returns the maximum value and the coordinates of
    any duplicates in the row

    Args:
        row (_type_): horizontal collection of matrix elements
        column (_type_): captures the column position

    Returns:
        _type_: map of the max value and list of occurrences
    """
    max_val = max(row)
    max_indices = [(column, index) for index, val in enumerate(row) if val == max_val]
    return (max_val, max_indices)


def process_column_min(col, position):
    """Reads a logical row of vertical data and returns the minimum value and the coordinates of
    any duplicates in the row

    Args:
        row (_type_): vertical collection of matrix elements
        column (_type_): captures the position

    Returns:
        _type_: map of the min value and list of occurrences
    """
    min_val = min(col)
    min_indices = [(index, position) for index, val in enumerate(col) if val == min_val]
    return (min_val, min_indices)


def check_saddle_points(matrix):
    """Takes an n x n matrix and checks for any saddle points

    Args:
        matrix (_type_): 2d nested list of integer elements

    Returns:
        _type_: a list of saddle point coordinates, or an error string
        indicating no results found
    """
    saddle_points_list = []

    # find all the max values in each row
    max_vals_by_row = {}
    for index, row in enumerate(matrix):
        temp = process_row_max(row, index)
        if temp[0] in max_vals_by_row:
            max_vals_by_row[temp[0]] += temp[1]
        else:
            max_vals_by_row[temp[0]] = temp[1]

    # find all the max values in each column
    min_vals_by_col = {}
    for i, _ in enumerate(matrix):
        temp_list = []
        for j, _ in enumerate(matrix[i]):
            temp_list.append(matrix[j][i])
        result = process_column_min(temp_list, i)
        if result[0] in min_vals_by_col:
            min_vals_by_col[result[0]] += result[1]
        else:
            min_vals_by_col[result[0]] = result[1]

    for item in min_vals_by_col.items():
        if item[0] in max_vals_by_row:
            for min_coords in min_vals_by_col[item[0]]:
                for max_coords in max_vals_by_row[item[0]]:
                    if (
                        min_coords[0] == max_coords[0]
                        and min_coords[1] == max_coords[1]
                    ):
                        saddle_points_list.append(min_coords)
    if len(saddle_points_list) > 0:
        return saddle_points_list
    else:
        return "No saddle points"


# this matrix has one saddle point: 9 (1,1)
one_saddle_points_map = [[2, 10, 3], [1, 9, 1], [2, 10, 2]]


# this matrix has one saddle points: 5 (3,2)
one_saddle_points_map2 = [
    [10, 12, 7, 3, 12],
    [3, 10, 6, 2, 8],
    [18, 24, 17, 6, 10],
    [4, 2, 5, 4, 2],
    [1, 18, 22, 4, 15],
]

# this matrix has no saddle points
zero_saddle_points_map = [
    [2, 5, 6, 9],
    [8, 4, 12, 3],
    [6, 7, 3, 1],
    [12, 24, 2, 11],
]

print(check_saddle_points(zero_saddle_points_map))
