class Day30:
    '''
        Time Complexity: O(N)
        Space Complexity: O(N)
    '''
    @staticmethod
    def get_trapped_rain_capacity(walls):
        if len(walls) == 1:
            return 0
        stack = [(0, walls[0])]
        index = 1
        memo = [-1] * len(walls)
        while index < len(walls):
            top = stack[-1]
            if walls[index] < top[1]:
                stack.append((index, walls[index]))
            else:
                while len(stack) and stack[-1][1] <= walls[index]:
                    memo[stack[-1][0]] = index
                    stack.pop(-1)
                stack.append((index, walls[index]))
            index+=1
        index = 0
        res = 0
        while index < len(walls):
            if memo[index] != -1:
                target = memo[index]
                if target == index + 1:
                    index+=1
                    continue
                curr_index_height = walls[index]
                while index < target:
                    res += min(walls[target],curr_index_height)-walls[index]
                    index+=1
            else:
                index+=1
        return res

if __name__ == '__main__':
    day_30 = Day30()
    assert  day_30.get_trapped_rain_capacity([10,9,8,7,6,8,7,6,5,8]) == 9
    assert  day_30.get_trapped_rain_capacity([5,4,3,2,1]) == 0
    assert  day_30.get_trapped_rain_capacity([1,2,3,4,5]) == 0
    assert day_30.get_trapped_rain_capacity([2, 1, 2]) == 1
    assert day_30.get_trapped_rain_capacity([3, 0, 1, 3, 0, 5]) == 8


