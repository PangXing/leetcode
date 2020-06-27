# coding:utf-8
'''
【23. 合并K个排序链表】
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''

from Queue import PriorityQueue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def mergeKLists(self, lists):
        '''
        使用优先队列合并
        '''
        head = pt = ListNode(0)
        q = PriorityQueue()
        for i in lists:
            if i:
                q.put((i.val, i))
        while q.qsize() > 1:
            val, node = q.get()
            pt.next = node
            pt = node
            if node.next:
                q.put((node.next.val, node.next))
        if q.qsize() == 1:
            val, node = q.get()
            pt.next = node
        return head.next


if __name__ == '__main__':
    solution = Solution()
    lists = list()
    p = ListNode(1)
    p.next = ListNode(4)
    p.next.next = ListNode(5)
    lists.append(p)
    p = ListNode(1)
    p.next = ListNode(3)
    p.next.next = ListNode(4)
    lists.append(p)
    p = ListNode(2)
    p.next = ListNode(6)
    lists.append(p)
    res = solution.mergeKLists(lists)
    print res








