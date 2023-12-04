from utils import Card
from copy import deepcopy

cards_dict: dict[str: list[Card]] = {}


def insert_cards(card_id: int, copies: int):
    insert_idx = card_id + 1
    for i in range(copies):
        cards_dict[insert_idx].append(deepcopy(cards_dict[insert_idx][0]))
        insert_idx += 1


def count_cards(cards_dict):
    count = 0
    for card_id in cards_dict:
        count += len(cards_dict[card_id])
    return count


def main():
    with open("input.txt", "r") as file:
        input_text = file.read()

    input_lines = input_text.split("\n")

    for line in input_lines:
        card = Card(line)
        cards_dict[card.card_id] = [card]

    for card_id in cards_dict:
        for card in cards_dict[card_id]:
            insert_cards(card_id, card.overlap)

    print(f"Total cards : {count_cards(cards_dict)}")


if __name__ == "__main__":
    main()
