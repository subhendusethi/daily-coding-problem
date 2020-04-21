class TreeNode:
    def __init__(self, left, right, is_locked=False, is_operable=True, parent=None):
        self.left = left
        self.right = right
        self.is_locked = is_locked
        self.is_operable = is_operable
        self.parent = parent

    def check_locked(self):
        return self.is_locked

    def __ancestor_check(self):
        curr_node = self
        ancestor_check = True
        while curr_node.parent:
            curr_node = curr_node.parent
            if curr_node.is_locked:
                ancestor_check = False
                break
        return ancestor_check

    def __switch_ancestor_inoperable(self, switch_boolean):
        curr_node = self
        while curr_node.parent:
            curr_node = curr_node.parent
            curr_node.is_operable = switch_boolean

    def lock(self):
        if not self.is_operable:
            return False
        if self.__ancestor_check():
            self.is_locked = True
            self.__switch_ancestor_inoperable(False)
            return True
        return False

    def unlock(self):
        if not self.is_operable:
            return False
        if self.check_locked() and self.__ancestor_check():
            self.is_locked = False
            self.__switch_ancestor_inoperable(True)
            return True
        return False

if __name__ == '__main__':
    left = TreeNode(None, None)
    right = TreeNode(None, None)
    root = TreeNode(left, right)
    setattr(left, 'parent', root)
    setattr(right, 'parent', root)

    assert root.left == left
    assert root.right == right
    assert left.parent == root
    assert right.parent == root

    assert root.unlock() == False
    assert left.check_locked() == False
    assert left.lock() == True
    assert left.check_locked() == True
    assert root.lock() == False
    assert root.check_locked() == False
    assert right.lock() == True
    assert right.check_locked() == True
    assert left.unlock() == True
    assert right.unlock() == True
    assert left.check_locked() == False
    assert right.check_locked() == False
    assert root.lock() == True
    assert left.lock() == False
    assert right.lock() == False
