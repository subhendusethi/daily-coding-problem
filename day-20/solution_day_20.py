# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Day20(object):
    def __get_length(self, node):
        res = 0
        while node != None:
            res += 1
            node = node.next
        return res
    '''
        Time Complexity: O(N)
        Space Comlpexity: O(1)
    '''
    def get_intersection_node(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = self.__get_length(headA), self.__get_length(headB)
        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        elif lenA < lenB:
            for _ in range(lenB - lenA):
                headB = headB.next

        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA


if __name__ == '__main__':
    day_20 = Day20()
    node1 = ListNode(10, ListNode(5, ListNode(1)))
    node2 = ListNode(20, ListNode(15, node1))

    assert day_20.get_intersection_node(node1, node2) == node1
