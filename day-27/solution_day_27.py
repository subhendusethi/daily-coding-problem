class Day27:
    @staticmethod
    def check_valid_braces(string):
        stack = []

        char_map = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for char in string:
            if char in char_map:
                if not len(stack):
                    return False
                top = stack.pop(len(stack)-1)
                if char_map[char] != top:
                    return False
            else:
                stack.append(char)
        return False if len(stack) > 0 else True

if __name__ == '__main__':
    day_27 = Day27()
    assert day_27.check_valid_braces('([])[]({})')
    assert not day_27.check_valid_braces('([)]')
    assert not day_27.check_valid_braces('((()')
    assert day_27.check_valid_braces('[]{}(((())))')
    assert day_27.check_valid_braces('')
