'''
Stack implementation in python using Deque module from collections package
it is a stack representation which is using doubly linked list concept because using Array or list
is taking more time and costly.
'''
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.is_empty()
    s.pop()
    s.is_empty()
    s.push(9)
    s.push(34)
    s.push(78)
    s.push(12)
    s.peek()
    s.pop()
    s.pop()