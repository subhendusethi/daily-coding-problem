'''
    Similar : https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
'''
class Day34(object):
    def min_insertions(self, string):
        """
        :type s: str
        :rtype: int
        """
        self.string = string
        s_len = len(string)
        dp = [[None for _ in range(s_len)] for _ in range(s_len)]

        def helper(left, right, dp):
            if dp[left][right]:
                return dp[left][right]
            sl = self.string[left]
            sr = self.string[right]
            if left == right:
                res = (0, sl)
            elif left == right - 1:
                curr_string = self.string[left:right+1]
                res = (0, curr_string)  if sl == sr \
                    else (1, min(curr_string + sl, sr + curr_string))
            else:
                if sl == sr:
                    rec = helper(left + 1, right - 1, dp)
                    res = (rec[0], sl + rec[1] + sl)
                else:
                    l_recur = helper(left + 1, right, dp)
                    r_recur = helper(left, right - 1, dp)
                    lsl = sl + l_recur[1] + sl
                    rsr = sr + r_recur[1] + sr
                    if l_recur[0] < r_recur[0] or (l_recur[0] == r_recur[0] and lsl <= rsr):
                        res = (l_recur[0] + 1, lsl)
                    elif l_recur[0] > r_recur[0] or (l_recur[0] == r_recur[0] and lsl > rsr):
                        res = (r_recur[0] + 1, rsr)
            dp[left][right] = res
            return res
        return helper(0, s_len - 1, dp)[1]

if __name__ == '__main__':
    day_34 = Day34()
    assert day_34.min_insertions("zzazz") == "zzazz"
    assert day_34.min_insertions("google") == "elgoogle"
    assert day_34.min_insertions("race") == "ecarace"
    assert day_34.min_insertions("google") == "elgoogle"
    assert day_34.min_insertions("racecar") == "racecar"
    assert day_34.min_insertions("google") == "elgoogle"
    assert day_34.min_insertions("egoogle") == "elgoogle"
    assert day_34.min_insertions("elgoog") == "elgoogle"
    assert day_34.min_insertions("race") == "ecarace"