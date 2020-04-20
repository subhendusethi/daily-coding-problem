import heapq
class Day21:
    '''
        Time Complexity: O(NLogN)
        Space Complexity: O(N)
    '''
    def get_required_classrooms(self,schedule):
        if len(schedule) == 0:
            return 0
        elif len(schedule) == 1:
            return 1
        else:
            schedule.sort(key = lambda x: x[0])
            alloc_store = [(schedule[0][1],1)]
            heapq.heapify(alloc_store)
            res = 1
            for segment in schedule[1:]:
                if len(alloc_store) == 0:
                    res += 1
                    continue
                min = heapq.heappop(alloc_store)
                if min[0] > segment[0]:
                    res+=1
                    heapq.heappush(alloc_store, min)
            return res
if __name__ == '__main__':
    day_21 = Day21()
    assert day_21.get_required_classrooms([]) == 0
    assert day_21.get_required_classrooms([(30, 75), (0, 50), (60, 150)]) == 2
    assert day_21.get_required_classrooms([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
    assert day_21.get_required_classrooms([(60, 150)]) == 1
    assert day_21.get_required_classrooms([(60, 150), (150, 170)]) == 1
    assert day_21.get_required_classrooms([(60, 150), (60, 150), (150, 170)]) == 2