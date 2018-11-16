'''
This problem was asked by Google.
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

from itertools import zip_longest

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        cursor = self
        while cursor is not None:
            yield cursor
            cursor = cursor.next

    def __len__(self, ):
        return sum(1 for elelemnt in self)


def solve(left, right):
    visited = set(left)
    for cur_right in right:
        if cur_right in visited:
            return cur_right
    return None

def solve_better(left,right):
    visited = set()
    for (cur_left, cur_right) in zip_longest(left, right):
        if cur_left == cur_right:
            return cur_left
        if cur_left in visited:
            return cur_left
        if cur_right in visited:
            return cur_right
        if cur_left is not None:
            visited.add(cur_left)
        if cur_right is not None:
            visited.add(cur_right)
    return None

if __name__ == '__main__':
    foo = 3
