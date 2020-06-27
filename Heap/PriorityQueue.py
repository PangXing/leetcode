# coding:utf-8

from heap import MinHeap

class MinPriorityQueue(MinHeap):
    def __init__(self, l1):
        super(MinPriorityQueue, self).__init__(l1)

    def enQueue(self, k):
        self._item.append(k)
        self.abjustUp(len(self._item)-1)

    def deQueue(self):
        if not self._item:
            return None
        head = self._item[0]
        tail = self._item.pop()
        self._item[0] = tail
        self.adjustDown(0)
        return head

if __name__ == '__main__':
    l1 = [7, 1, 3, 10, 5, 2, 8, 9, 6]
    mypq = MinPriorityQueue(l1)
    mypq.enQueue(4)
    print mypq._item
    print mypq.deQueue()

    from Queue import PriorityQueue
    l2 = [7, 1, 3, 10, 5, 2, 8, 9, 6]
    q = PriorityQueue()
    for i in l2:
        q.put(i)
    q.put(4)
    print q.queue
    print q.get()

