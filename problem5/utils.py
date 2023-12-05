# flake8: noqa
class Map:
    def __init__(self, name: str, ranges: list[list[int]]) -> None:
        self.name = name
        self.ranges = ranges

    def map_location(self, input_location: int) -> int:
        for loc_range in self.ranges:
            dst_start, src_start, range_len = loc_range
            if input_location >= src_start and input_location <= src_start + range_len:
                return dst_start + (input_location - src_start)

        return input_location

    def map_location_range(self, start_range, range_len) -> list[list[int]]:
        map_ranges = []
        current_pointer = start_range
        remaining = range_len
        mapped = True

        while mapped and remaining:
            mapped = False
            for loc_range in self.ranges:
                dst_start, src_start, range_len = loc_range

                if (
                    current_pointer >= src_start
                    and current_pointer < src_start + range_len
                ):
                    mapped |= True
                    capacity = src_start + range_len - current_pointer
                    consumed = min(remaining, capacity)
                    map_ranges.append(
                        [dst_start + (current_pointer - src_start), consumed]
                    )
                    remaining -= consumed
                    current_pointer += consumed

        if remaining:
            map_ranges.append([current_pointer, remaining])
        return map_ranges


def parse_map(map_lines: list[str]) -> Map:
    name = map_lines[0].split(" ")[0]
    range_lambda = lambda x: list(map(int, x.strip().split(" ")))
    ranges = list(map(range_lambda, map_lines[1:]))
    return Map(name, ranges)


def parse_seeds(seed_line):
    seed_str = seed_line.split(":")[1]
    seeds = list(map(int, seed_str.strip().split(" ")))
    return seeds


def parse_input(input_text: str) -> tuple[list[int], list[Map]]:
    input_lines = input_text.split("\n")
    seeds = parse_seeds(input_lines[0])
    maps = []
    accumulate_lines = []
    for line in input_lines[2:]:
        if line:
            accumulate_lines.append(line)
        else:
            maps.append(parse_map(accumulate_lines))
            accumulate_lines = []
    maps.append(parse_map(accumulate_lines))

    return seeds, maps
