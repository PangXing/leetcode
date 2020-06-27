# coding:utf-8

'''
1. 二叉堆逻辑上是一个完全二叉树，但使用顺序表存储，
    - 左孩子 parent*2 + 1
    - 右孩子 parent*2 + 2
    - 父亲 (i -1)/2
2. 时间复杂度：
   - 上浮 O(logN) 【树的高度相关】
   - 下沉 O(logN)
   - 构建 O(N)
3. 空间复杂度 ： O(1)
'''

class MinHeap(object):
    def __init__(self, l1):
        self._item = l1
        self.buildHeap()


    def buildHeap(self):
        '''
        从最底层第一个非叶子节点开始，对所有非叶子节点进行下沉，类似于挨个插入
        '''
        i = (len(self._item) -2)/ 2
        while i >= 0:
            self.adjustDown(i)
            i -= 1

    def adjustDown(self, i):
        '''
        下沉操作
        '''
        if i >= len(self._item):
            return
        val = self._item[i]
        left = i*2 + 1
        right = i*2 + 2
        while left < len(self._item) or right< len(self._item):
            if right < len(self._item):
                min_pos = right if self._item[right] < self._item[left] else left
            else:
                min_pos = left
            if self._item[min_pos] < val:
                self._item[i] = self._item[min_pos]
                i = min_pos
                left = i*2 + 1
                right = i * 2 + 2
            else:
                break
        self._item[i] = val


    def abjustUp(self, i):
        '''
        上浮操作
        '''
        val = self._item[i]
        parrent = (i -1)/2
        while parrent >= 0 and self._item[parrent] > val:
            self._item[i] = self._item[parrent]
            i = parrent
            parrent = (i-1)/2
        self._item[i] = val

if __name__ == '__main__':
    l1 = [7,1,3,10,5,2,8,9,6]
    min_heap = MinHeap(l1)
    print min_heap._item

    '''
    实际上，Python没有独立的堆类型，而只有一个包含一些堆操作函数的模块。这个模块名为heapq
     - heapify(heap) 让列表具备堆特征 (建立小根堆)
     - heappush(heap, x)  将x压入堆中
     - heappop(heap)  从堆中弹出最小的元素
    
    '''
    import heapq
    l1 = [7, 1, 3, 10, 5, 2, 8, 9, 6]
    heapq.heapify(l1)
    print l1
    heapq.heappop(l1)
    print l1









