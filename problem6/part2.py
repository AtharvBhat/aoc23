def parse_input(input_text: str) -> tuple[list[int], list[int]]:
    return list(
        map(
            lambda y: list(
                filter(lambda x: x, y.split(":")[1].strip().split(" ")),
            ),
            input_text.split("\n"),
        )
    )


def calculate_possibilities(time: int, distance: int) -> int:
    possibilities = 0
    min_time = time // 2
    while min_time * (time - min_time) > distance:
        possibilities += 1
        min_time -= 1

    possibilities *= 2
    if time % 2 == 0:
        possibilities -= 1
    return possibilities


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_text = file.read()

    times, distances = parse_input(input_text)
    time, distance = int("".join(times)), int("".join(distances))
    possibilities = calculate_possibilities(time, distance)

    print(f"margin : {possibilities}")
