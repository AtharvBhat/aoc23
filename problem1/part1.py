def search_frist_number(input_str: str) -> str:
    for i in range(len(input_str)):
        if str.isdigit(input_str[i]):
            return input_str[i]


def search_second_number(input_str: str) -> str:
    for i in list(range(len(input_str)))[::-1]:
        if str.isdigit(input_str[i]):
            return input_str[i]


def extract_numbers(input_text: str) -> int:
    nums = []
    for input_str in input_text:
        num = int(search_frist_number(input_str) + search_second_number(input_str))
        nums.append(num)
    return nums


def main():
    with open("input1.txt", "r") as file:
        input_text = file.read()

    input_text = input_text.split("\n")
    print(sum(extract_numbers(input_text)))


if __name__ == "__main__":
    main()
