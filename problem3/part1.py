# noqa
from utils import check_left, check_right, check_above, check_below
from utils import check_top_left, check_top_right, check_bottom_left
from utils import check_bottom_right


def idx_check_valid(input_lines, row: int, col: int) -> bool:
    # checks if an index is adjacent to a symbol
    is_valid = False
    args = (input_lines, row, col)
    funs = [
        check_left,
        check_right,
        check_above,
        check_below,
        check_top_left,
        check_top_right,
        check_bottom_left,
        check_bottom_right,
    ]

    for fn in funs:
        is_valid |= fn(*args)

    return is_valid


def num_check_valid(input_lines, row: int, col: int) -> tuple[int, bool, int]:
    # given a start idx of a number, returns part number, if its valid and the last index of the number
    num = ""
    is_valid = False

    while col < len(input_lines[row]) and str.isdigit(input_lines[row][col]):
        num += input_lines[row][col]
        is_valid |= idx_check_valid(input_lines, row, col)
        col += 1

    last_idx = col
    return int(num), is_valid, last_idx


def main():
    with open("input.txt", "r") as file:
        input_text = file.read()

    input_lines = list(map(list, input_text.split("\n")))

    part_sum = 0

    skip_times = 0
    for row in range(len(input_lines)):
        for col in range(len(input_lines[row])):
            if skip_times > 0:
                skip_times -= 1
                continue
            if str.isdigit(input_lines[row][col]):
                part_number, is_valid, last_idx = num_check_valid(input_lines, row, col)
                skip_times += last_idx - col
                if is_valid:
                    part_sum += part_number

    print(f"part sum : {part_sum}")


if __name__ == "__main__":
    main()
