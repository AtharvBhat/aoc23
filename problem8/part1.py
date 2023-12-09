nodes = {}


def parse_nodes(line: str) -> tuple[str, tuple[str, str]]:
    node = line.split("=")[0].strip()

    left = line.split("=")[1].strip().split(",")[0][1:].strip()
    right = line.split("=")[1].strip().split(",")[1][:-1].strip()

    return node, (left, right)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_text = file.read()

    instructions = list(input_text.split("\n")[0])

    for line in input_text.split("\n")[2:]:
        node, directions = parse_nodes(line)
        nodes[node] = dict(zip(("L", "R"), directions))

    steps = 0
    current_node = "AAA"

    while current_node != "ZZZ":
        for instruction in instructions:
            next_node = nodes[current_node][instruction]
            steps += 1
            current_node = next_node

    print(f"Num steps: {steps}")
