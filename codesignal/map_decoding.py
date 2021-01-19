from functools import lru_cache


def map_decoding(message: str) -> int:
    if message is None:
        return 0
    count, length = 0, len(message)

    if length == 0:
        return 1

    @lru_cache(None)
    def code(index: int):
        if index <= length - 1 and message[index] == '0':
            return 0
        if index >= length - 1:
            return 1
        temp_1, temp_2 = 0, 0

        if index < length - 1:
            # counting every digit 1 - 9 as code
            if message[index + 1] != '0':
                # print("code_1:", message[index], message[index+1])
                temp_1 = code(index + 1)

            # 2 digits as code 10 - 26
            if message[index] == '1' or (message[index] == '2' and ord(message[index + 1]) - ord('0') <= 6):
                # print("code_2:", message[index] + message[index+1])
                temp_2 = code(index + 2)

        return (temp_1 + temp_2) % (10 ** 9 + 7)

    return code(0)
