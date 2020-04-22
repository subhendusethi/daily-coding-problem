class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Day26:
    @staticmethod
    def remove_kth_last_node(start, K):
        index = 0
        curr_node = start
        while index < K:
            curr_node = curr_node.next
            index+=1
        iter = curr_node.next
        prev_node, start_node = None, start
        while iter:
            iter = iter.next
            prev_node = start_node
            start_node = start_node.next
        if prev_node:
            prev_node.next = start_node.next
            del start_node
            return start
        else:
            start_node = start.next
            del start
            return start_node
    @staticmethod
    def get_list(start):
        res = []
        while start:
            res.append(start.value)
            start = start.next
        return res

if __name__ == '__main__':
    day_26 = Day26()

    t1 = Node(1,Node(2, Node(3, Node(4, Node(5, None)))))
    mod_t1 = day_26.remove_kth_last_node(t1,2)
    print(day_26.get_list(mod_t1))
    assert day_26.get_list(mod_t1) == [1,2,4,5]

    t2 = Node(1,Node(2, Node(3, Node(4, Node(5, None)))))
    mod_t2 = day_26.remove_kth_last_node(t2,1)
    print(day_26.get_list(mod_t2))
    assert day_26.get_list(mod_t2) == [1,2,3,5]

    t3 = Node(1,Node(2, Node(3, Node(4, Node(5, None)))))
    mod_t3 = day_26.remove_kth_last_node(t3,4)
    assert day_26.get_list(mod_t3) == [2,3,4,5]


