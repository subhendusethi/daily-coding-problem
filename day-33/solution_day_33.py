import heapq

class Day33:
    @staticmethod
    def get_running_medians(stream):
        if not stream:
            return None

        min_heap, max_heap = [], []

        res = []
        for x in stream:
            heapq.heappush(min_heap, x)
            if len(min_heap) > len(max_heap) + 1:
                min_heap_smallest = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -min_heap_smallest)

            if len(min_heap) == len(max_heap):
                median = (min_heap[0] - max_heap[0]) / 2
            else:
                median = min_heap[0]

            res.append(median)
        return res

if __name__ == '__main__':
    day_33 = Day33()
    assert not day_33.get_running_medians([])
    assert day_33.get_running_medians([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
    assert day_33.get_running_medians([1, 99]) == [1, 50]
