from collections import Counter

card_points = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

bids = {}


def get_hand_points(hand) -> int:
    cards = list(hand)
    count = Counter(cards)
    match len(count):
        case 1:
            return 7

        case 2:
            if count.most_common()[0][1] == 4:
                return 6
            else:
                return 5

        case 3:
            if count.most_common()[0][1] == 3:
                return 4
            else:
                return 3

        case 4:
            return 2
        case _:
            return 1


def solve_tie(hand1, hand2) -> int:
    # return True if hand 1 and 2 need to be swapped
    for card1, card2 in zip(hand1, hand2):
        if card_points[card1] > card_points[card2]:
            return False
        if card_points[card1] < card_points[card2]:
            return True
    return False


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_text = file.read()

    hands = []
    points = []
    for line in input_text.split("\n"):
        hand, bid = line.split(" ")[0], int(line.split(" ")[-1])
        bids[hand] = bid
        hands.append(hand)
        points.append(get_hand_points(hand))

    hands = sorted(hands, key=lambda x: get_hand_points(x), reverse=True)
    points = sorted(points, reverse=True)
    swapped = True

    while swapped:
        swapped = False
        # solve ties
        a_ptr = 0
        b_ptr = 1
        while b_ptr < len(hands):
            if points[a_ptr] == points[b_ptr]:
                if solve_tie(hands[a_ptr], hands[b_ptr]):
                    swapped |= True
                    hands[a_ptr], hands[b_ptr] = hands[b_ptr], hands[a_ptr]
            a_ptr += 1
            b_ptr += 1

    # calculate winnings
    winnings = 0
    for i in range(len(hands)):
        winnings += (len(hands) - i) * bids[hands[i]]

    print(f"Winnings: {winnings}")
