# noqa
import numpy as np

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


def search_numbers(input_str: str) -> str:
    nums = []
    indices = []
    for i in range(len(input_str)):
        if str.isdigit(input_str[i]):
            nums.append(input_str[i])
            indices.append(i)

    min_idx = np.argmin(indices)
    max_idx = np.argmax(indices)

    return [nums[min_idx], nums[max_idx]], [indices[min_idx], indices[max_idx]]


def search_numbers_str(input_str: str) -> str:
    nums = []
    indices = []
    for num in digits.keys():
        if num in input_str:
            num_indices = [
                i for i in range(len(input_str)) if input_str.startswith(num, i)
            ]
            indices += num_indices
            nums += [digits[num]] * len(num_indices)

    if not nums:
        return [], []

    min_idx = np.argmin(indices)
    max_idx = np.argmax(indices)

    return [nums[min_idx], nums[max_idx]], [indices[min_idx], indices[max_idx]]


def extract_numbers(input_text: str) -> int:
    nums = []
    for input_str in input_text:
        int_nums, int_idx = search_numbers(input_str)
        str_nums, str_idx = search_numbers_str(input_str)

        comb_nums = int_nums + str_nums
        comb_idx = int_idx + str_idx

        min_idx = np.argmin(comb_idx)
        max_idx = np.argmax(comb_idx)

        num = int(comb_nums[min_idx] + comb_nums[max_idx])
        nums.append(num)

    return nums


def main():
    with open("input1.txt", "r") as file:
        input_text = file.read()

    input_text = input_text.split("\n")
    print(sum(extract_numbers(input_text)))


if __name__ == "__main__":
    main()
