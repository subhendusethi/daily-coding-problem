import copy

class Day31:
    def __init__(self):
        self.DP = [[]]

    def get_edit_distance(self, string1, string2):
        l1 = len(string1)
        l2 = len(string2)
        self.DP = [[0 for i in range(l2+1)] for j in range(l1+1)]

        def helper(s1, s2, index1, index2):
            if self.DP[index1][index2]:
                return self.DP[index1][index2]

            if index1 == 0:
                res = index2
            elif index2 == 0:
                res = index1
            elif s1[index1-1] == s2[index2-1]:
                res = helper(s1, s2, index1 - 1, index2 - 1)
            else:
                res = 1 + min(helper(s1, s2, index1, index2 - 1), \
                              helper(s1, s2, index1 - 1, index2), \
                              helper(s1, s2, index1 - 1, index2 - 1))
            self.DP[index1][index2] = res
            return res

        res = helper(string1, string2, l1, l2)
        return self.DP[l1][l2]

if __name__ == '__main__':
    day_31 = Day31()
    assert day_31.get_edit_distance('kit', 'sis') == 2
    assert day_31.get_edit_distance('kitten', 'sitting') == 3
    assert day_31.get_edit_distance("", "") == 0
    assert day_31.get_edit_distance("a", "b") == 1
    assert day_31.get_edit_distance("abc", "") == 3
    assert day_31.get_edit_distance("abc", "abc") == 0
    assert day_31.get_edit_distance("kitten", "sitting") == 3
