# noqa
from utils import check_left_gear, check_right_gear, check_above_gear
from utils import check_top_left_gear, check_top_right_gear
from utils import check_bottom_right_gear, check_bottom_left_gear
from utils import check_below_gear


def idx_check_valid(input_lines, row: int, col: int) -> bool:
    # checks if an index is adjacent to a symbol
    is_valid = False
    gear_loc = []
    args = (input_lines, row, col)
    funs = [
        check_left_gear,
        check_right_gear,
        check_above_gear,
        check_below_gear,
        check_top_left_gear,
        check_top_right_gear,
        check_bottom_left_gear,
        check_bottom_right_gear,
    ]

    for fn in funs:
        valid, loc = fn(*args)
        is_valid |= valid
        if valid:
            gear_loc.append(loc)

    return is_valid, set(gear_loc)


def num_check_valid(input_lines, row: int, col: int) -> tuple[int, bool, int]:
    # given a start idx of a number, returns part number, if its valid and the last index of the number
    num = ""
    is_valid = False
    gear_loc = []
    while col < len(input_lines[row]) and str.isdigit(input_lines[row][col]):
        num += input_lines[row][col]
        valid, loc = idx_check_valid(input_lines, row, col)
        is_valid |= valid
        gear_loc += list(loc)

        col += 1

    last_idx = col
    return int(num), is_valid, last_idx, set(gear_loc)


def main():
    with open("input.txt", "r") as file:
        input_text = file.read()

    input_lines = list(map(list, input_text.split("\n")))

    skip_times = 0
    valid_parts = {}
    for row in range(len(input_lines)):
        for col in range(len(input_lines[row])):
            if skip_times > 0:
                skip_times -= 1
                continue
            if str.isdigit(input_lines[row][col]):
                part_number, is_valid, last_idx, gear_location = num_check_valid(
                    input_lines, row, col
                )
                skip_times += last_idx - col
                if is_valid:
                    for gear in gear_location:
                        if gear in valid_parts:
                            valid_parts[gear].append(part_number)
                        else:
                            valid_parts[gear] = [part_number]

    gear_ratio_sum = 0
    for gear in valid_parts:
        if len(valid_parts[gear]) == 2:
            gear_ratio = valid_parts[gear][0] * valid_parts[gear][1]
            gear_ratio_sum += gear_ratio

    print(f"Gear ratio sum : {gear_ratio_sum}")


if __name__ == "__main__":
    main()
