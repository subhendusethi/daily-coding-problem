class Day28:
    @staticmethod
    def encode(string):
        if not string:
            return string
        res = ""
        s_len = len(string)
        index = 0
        while index < s_len:
            curr_char, curr_count = string[index], 1
            while index + 1 < s_len and curr_char == string[index+1]:
                curr_count += 1
                index+=1
            res+= str(curr_count) + curr_char
            index+=1
        return res

    @staticmethod
    def decode(string):
        if not string:
            return string
        res = ""
        index = 0
        s_len = len(string)
        while index < s_len:
            count, curr_char = int(string[index]), string[index + 1]
            for _ in range(count):
                res+=curr_char
            index+=2
        return res


if __name__ == '__main__':
    day_28 = Day28()
    assert day_28.encode("AABBCCDD") == "2A2B2C2D"
    assert day_28.decode("2A2B2C2D") == "AABBCCDD"

    assert day_28.encode("A") == "1A"
    assert day_28.decode("1B") == "B"

    assert day_28.encode("AAAABBBCCDAA") == "4A3B2C1D2A"
    assert day_28.decode("4A3B2C1D2A") == "AAAABBBCCDAA"

    assert day_28.encode("SUBHENDU") == "1S1U1B1H1E1N1D1U"
    assert day_28.decode("1S1U1B1H1E1N1D1U") == "SUBHENDU"
