# flake8: noqa
from utils import parse_input


def convert_seed_ranges(range_list: int) -> list[list[int]]:
    range_start = range_list[::2]
    range_len = range_list[1::2]

    return [[start, length] for start, length in zip(range_start, range_len)]


def main():
    with open("input.txt", "r") as file:
        input_text = file.read()

    seed_ranges, maps = parse_input(input_text)
    seed_ranges = convert_seed_ranges(seed_ranges)

    for loc_map in maps:
        map_out = []

        for seed_range in seed_ranges:
            map_out += loc_map.map_location_range(*seed_range)
        seed_ranges = map_out

    min_loc = None
    for out in map_out:
        if min_loc:
            min_loc = min(min_loc, out[0])
        else:
            min_loc = out[0]

    print(f"Min loc : {min_loc}")


if __name__ == "__main__":
    main()
