# coding:utf-8

class MinStack(object):
    def __init__(self):
        self._items = list()
        self._min_items = list()

    def push(self, x):
        self._items.append(x)
        if not self._min_items:
            self._min_items.append(x)
        else:
            min_item = self._min_items[-1]
            if x < min_item:
                self._min_items.append(x)
            else:
                self._min_items.append(min_item)

    def pop(self):
        if self._items:
            self._items.pop()
            self._min_items.pop()

    def top(self):
        if self._items:
            return self._items[-1]
        else:
            return

    def getMin(self):
        if self._min_items:
            return self._min_items[-1]
        else:
            return

if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print min_stack.getMin()
    min_stack.pop()
    print min_stack.top()
    print min_stack.getMin()