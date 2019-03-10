'''
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program,
so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
'''

import typing

class Node:

    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None
        self.locked = False
        self.locked_descendants_count = 0

    def add_left(self, child):
        self.left = child

    def add_right(self, child):
        self.right = child

    @property
    def is_locked(self):
        return self.locked

    def _can_lock_or_unlock(self):
        if self.locked_descendants_count > 0:
            return False

        current = self.parent
        while current:
            if current.is_locked:
                return False
            current = current.parent
        return True

    def lock(self):
        if self._can_lock_or_unlock():
            self.locked = True

            current = self.parent
            while current:
                current.locked_descendants_count += 1
                current = current.parent
            return True
        else:
            return False

    def unlock(self):
        if self._can_lock_or_unlock():
            self.locked = False

            current = self.parent
            while current:
                current.locked_descendants_count -= 1
                current = current.parent
            return True
        else:
            return False

