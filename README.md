
# [daily-coding-problem](https://www.dailycodingproblem.com/)

## Daily Coding Problem: Problem #1 [Easy]
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Solution: [Day 1](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_1/solution_day_1.py)


## Daily Coding Problem: Problem #2 [Hard]
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Solution: [Day 2](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_2/solution_day_2.py)

## Daily Coding Problem: Problem #3 [Medium]

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:

```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
Solution: [Day 3](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_3/solution_day_3.py)

## Daily Coding Problem: Problem #4 [Hard]


Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

Solution: [Day 4](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_4/solution_day_4.py)

## Daily Coding Problem: Problem #5 [Medium]

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement car and cdr.

Solution: [Day 5](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_5/solution_day_5.py)

## Daily Coding Problem: Problem #6 [Hard]

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.


Solution: [Day 6](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_6/solution_day_6.py)


## Daily Coding Problem: Problem #7 [Medium]

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

Solution: [Day 7](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_7/solution_day_7.py)


## Daily Coding Problem: Problem #8 [Easy]

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
```python
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```
Solution: [Day 8](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_8/solution_day_8.py)

## Daily Coding Problem: Problem #9 [Hard]

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
Solution O(N) Space Complexity: [Day 9](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_9/solution_day_9.py)
Solution O(1) Space Complexity: [Day 9](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_9/solution_day_9_efficient.py)


Daily Coding Problem: Problem #10 [Medium]
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

Solution: [Day 10](https://github.com/subhendusethi/daily-coding-problem/blob/master/day_10/solution_day_10.py)