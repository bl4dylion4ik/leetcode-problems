def multiply(num1: str, num2: str) -> str:
    num_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }

    first_num = 0
    for i in range(len(num1) - 1, -1, -1):
        first_num += num_map[num1[i]] * (10 ** (len(num1) - 1 - i))

    second_num = 0
    for i in range(len(num2) - 1, -1, -1):
        second_num += num_map[num2[i]] * (10 ** (len(num2) - 1 - i))

    return f'{first_num * second_num}'