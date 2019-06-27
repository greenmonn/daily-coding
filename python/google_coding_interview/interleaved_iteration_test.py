import pytest
import sys

'''
1. Flat on initialization (current solution)
2. Read flattely on next
    # O(k) operation
    # O(k) initialization
    # Using Queue* (optimal)
'''

class iterator():
    def __init__(self, list):
        self.list = list
        self.pos = -1

    def next(self):
        self.pos += 1
        return self.list[self.pos]

    def hasNext(self):
        return self.pos + 1 < len(self.list)


class IteratorFlattener():
    def __init__(self, iterlist: list):
        self.list = []

        while len(iterlist) > 0:
            for iter in iterlist:
                if iter.hasNext():
                    self.list.append(iter.next())

            for iter in iterlist[:]:
                if not iter.hasNext():
                    iterlist.remove(iter)

        self.pos = -1

    def _get_current_item(self):
        if self.pos == -1:
            return None

        return self.list[self.pos]

    def next(self):
        self.pos += 1
        return self._get_current_item()

    def hasNext(self):
        return self.pos + 1 < len(self.list)


if __name__ == '__main__':
    arr1 = [1, 2, 3]
    arr2 = [4, 5]
    arr3 = [6, 7, 8, 9]
    
    a = iterator(arr1)
    b = iterator(arr2)
    c = iterator(arr3)

    iterlist = [a, b, c]

    IF = IteratorFlattener(iterlist)

    while(IF.hasNext()):
        sys.stdout.write(str(IF.next()))
        sys.stdout.write(' ')
