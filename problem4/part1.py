from utils import Card


def main():
    with open("input.txt", "r") as file:
        input_text = file.read()

    input_lines = input_text.split("\n")

    win_sum = 0
    for line in input_lines:
        card = Card(line)
        win_sum += 2 ** max((card.overlap - 1), 0)

    print(f"win sum : {win_sum}")


if __name__ == "__main__":
    main()
