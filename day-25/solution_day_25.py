class Day25:
    '''
        Time Complexity: O(2^N)
        Space Complexity: O(2^N)
    '''
    @staticmethod
    def match(regex, string):
        def helper(regex, string, last_char):
            if regex == string:
                return True
            if not regex and string:
                return False
            if regex == '*' and not string:
                return True
            if regex[0] not in ['.', '*']:
                return regex[0] == string[0] and helper(regex[1:], string[1:], string[0])
            else:
                if regex[0] == '*':
                    return (last_char == string[0] and helper(regex, string[1:], last_char)) \
                           or helper(regex[1:], string, string[0])
                elif regex[0] == '.':
                    return helper(regex[1:], string[1:], string[0])
        return helper(regex, string, None)


if __name__ == '__main__':
    day_25 = Day25()
    assert day_25.match('ch.*t', 'chaaat')
    assert day_25.match('ch.*t', 'chxt')
    assert not day_25.match('ch.*t', 'xhaaat')
    assert day_25.match('ra.', 'ray')
    assert day_25.match('ra.', 'ray')
    assert not day_25.match('ra.', 'raymond')
    assert day_25.match('.*at', 'ccat')
    assert not day_25.match('.*at', 'chats')
    assert day_25.match('.*.*.*', 'aaaaaaabbbbbbbbbbbbbsssssssssss')
    assert day_25.match('.', 'a')
    assert day_25.match('.*hercules*', 'ffffhercules')
    assert day_25.match('', '')
    assert not day_25.match('', 'abcd')

