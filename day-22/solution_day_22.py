from typing import List

VectorStr = List[str]
'''
    Time Complexity: O(N*M) -- N length of sentence, M length of the dictionary.
    Space Complexity: O(N*M)
    
    Variant: https://leetcode.com/problems/word-break-ii/
'''
class Day22:
    @staticmethod
    def breakdown_ways(dictionary:VectorStr, sentence:str):
        if len(sentence) == 0 or len(dictionary) == 0:
            return []
        DP = {}

        def recur_breakdown(string, DP, dictionary):
            if len(string) == 0:
                return []
            if string in DP:
                return DP[string]
            for word in dictionary:
                curr_breakdown = []
                if string.startswith(word):
                    sub_str = string[len(word):]
                    curr_breakdown = recur_breakdown(sub_str, DP, dictionary)
                    if (len(curr_breakdown) == 0 and len(sub_str) == 0) \
                            or (len(curr_breakdown) != 0):
                        curr_breakdown.insert(0, word)
                        break
            DP[string] = curr_breakdown
            return DP[string]
        return recur_breakdown(sentence, DP, dictionary)

if  __name__ == '__main__':
    day_22 = Day22()
    assert day_22.breakdown_ways(['the', 'quick', 'brown', 'fox'], "thequickbrownfoxfoxbrownquickquick") \
           == ['the', 'quick', 'brown', 'fox', 'fox', 'brown', 'quick', 'quick']
    assert day_22.breakdown_ways(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond") \
           == ['bed', 'bath', 'and', 'beyond']
    assert day_22.breakdown_ways(['a','aa'], "aaa") \
           == ['a','a','a']
    assert day_22.breakdown_ways(['b','aa'], "aaa") \
           == []
    assert day_22.breakdown_ways([], "aaa") \
           == []