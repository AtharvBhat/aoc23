from utils import Card

cards_dict: dict[str:Card] = {}
card_copies: dict[str:int] = {}


def insert_cards(card_id: int) -> None:
    insert_idx = card_id + 1
    copies = cards_dict[card_id].overlap
    for i in range(copies):
        card_copies[insert_idx] += card_copies[card_id]
        insert_idx += 1


def count_cards(cards_dict) -> int:
    count = 0
    for card_id in cards_dict:
        count += cards_dict[card_id]
    return count


def main():
    with open("input.txt", "r") as file:
        input_text = file.read()

    input_lines = input_text.split("\n")

    for line in input_lines:
        card = Card(line)
        cards_dict[card.card_id] = card
        card_copies[card.card_id] = 1

    for card_id in cards_dict:
        insert_cards(card_id)

    print(f"Total cards : {count_cards(card_copies)}")


if __name__ == "__main__":
    main()
