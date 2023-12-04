class Card:
    def __init__(self, line: str):
        self.card_id = self.parse_card_number(line)
        self.winning_numbers = self.parse_winning_numbers(line)
        self.drawn_numbers = self.parse_draw(line)

    def parse_card_number(self, line: str) -> int:
        card_id = int(line.split(":")[0].strip().split(" ")[-1])
        return card_id

    def parse_winning_numbers(self, line: str) -> list[int]:
        winning_numbers = line.split(":")[1].split("|")[0].strip().split(" ")
        winning_numbers = [x for x in winning_numbers if x]
        return list(map(int, winning_numbers))

    def parse_draw(self, line: str) -> list[int]:
        draw = line.split(":")[1].split("|")[1].strip().split(" ")
        draw = [x for x in draw if x]
        return list(map(int, draw))

    def calculate_overlap(self):
        overlap = 0
        for number in self.drawn_numbers:
            if number in self.winning_numbers:
                overlap += 1

        return overlap


def main():
    with open("input.txt", "r") as file:
        input_text = file.read()

    input_lines = input_text.split("\n")

    win_sum = 0
    for line in input_lines:
        card = Card(line)
        win_sum += (
            2 ** (card.calculate_overlap() - 1) if card.calculate_overlap() > 0 else 0
        )

    print(f"win sum : {win_sum}")


if __name__ == "__main__":
    main()
