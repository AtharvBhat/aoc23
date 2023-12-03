def check_left(input_lines, row, col):
    return (
        (col > 0)
        and (not str.isdigit(input_lines[row][col - 1]))
        and (input_lines[row][col - 1] != ".")
    )


def check_right(input_lines, row, col):
    return (
        (col < len(input_lines[row]) - 1)
        and (not str.isdigit(input_lines[row][col + 1]))
        and (input_lines[row][col + 1] != ".")
    )


def check_above(input_lines, row, col):
    return (
        (row > 0)
        and (not str.isdigit(input_lines[row - 1][col]))
        and (input_lines[row - 1][col] != ".")
    )


def check_below(input_lines, row, col):
    return (
        (row < len(input_lines) - 1)
        and (not str.isdigit(input_lines[row + 1][col]))
        and (input_lines[row + 1][col] != ".")
    )


def check_top_left(input_lines, row, col):
    return (
        (col > 0)
        and (row > 0)
        and (not str.isdigit(input_lines[row - 1][col - 1]))
        and (input_lines[row - 1][col - 1] != ".")
    )


def check_top_right(input_lines, row, col):
    return (
        (col < len(input_lines[row]) - 1)
        and (row > 0)
        and (not str.isdigit(input_lines[row - 1][col + 1]))
        and (input_lines[row - 1][col + 1] != ".")
    )


def check_bottom_left(input_lines, row, col):
    return (
        (col > 0)
        and (row < len(input_lines) - 1)
        and (not str.isdigit(input_lines[row + 1][col - 1]))
        and (input_lines[row + 1][col - 1] != ".")
    )


def check_bottom_right(input_lines, row, col):
    return (
        (col < len(input_lines[row]) - 1)
        and (row < len(input_lines) - 1)
        and (not str.isdigit(input_lines[row + 1][col + 1]))
        and (input_lines[row + 1][col + 1] != ".")
    )


def convert_coordinates_to_str(x, y):
    return f"{x[0]},{y[0]}"


def check_left_gear(input_lines, row, col):
    return (
        (col > 0)
        and (not str.isdigit(input_lines[row][col - 1]))
        and (input_lines[row][col - 1] == "*")
    ), convert_coordinates_to_str([row], [col - 1])


def check_right_gear(input_lines, row, col):
    return (
        (col < len(input_lines[row]) - 1)
        and (not str.isdigit(input_lines[row][col + 1]))
        and (input_lines[row][col + 1] == "*")
    ), convert_coordinates_to_str([row], [col + 1])


def check_above_gear(input_lines, row, col):
    return (
        (row > 0)
        and (not str.isdigit(input_lines[row - 1][col]))
        and (input_lines[row - 1][col] == "*")
    ), convert_coordinates_to_str([row - 1], [col])


def check_below_gear(input_lines, row, col):
    return (
        (row < len(input_lines) - 1)
        and (not str.isdigit(input_lines[row + 1][col]))
        and (input_lines[row + 1][col] == "*")
    ), convert_coordinates_to_str([row + 1], [col])


def check_top_left_gear(input_lines, row, col):
    return (
        (col > 0)
        and (row > 0)
        and (not str.isdigit(input_lines[row - 1][col - 1]))
        and (input_lines[row - 1][col - 1] == "*")
    ), convert_coordinates_to_str([row - 1], [col - 1])


def check_top_right_gear(input_lines, row, col):
    return (
        (col < len(input_lines[row]) - 1)
        and (row > 0)
        and (not str.isdigit(input_lines[row - 1][col + 1]))
        and (input_lines[row - 1][col + 1] == "*")
    ), convert_coordinates_to_str([row - 1], [col + 1])


def check_bottom_left_gear(input_lines, row, col):
    return (
        (col > 0)
        and (row < len(input_lines) - 1)
        and (not str.isdigit(input_lines[row + 1][col - 1]))
        and (input_lines[row + 1][col - 1] == "*")
    ), convert_coordinates_to_str([row + 1], [col - 1])


def check_bottom_right_gear(input_lines, row, col):
    return (
        (col < len(input_lines[row]) - 1)
        and (row < len(input_lines) - 1)
        and (not str.isdigit(input_lines[row + 1][col + 1]))
        and (input_lines[row + 1][col + 1] == "*")
    ), convert_coordinates_to_str([row + 1], [col + 1])
