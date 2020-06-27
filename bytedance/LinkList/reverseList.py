# coding:utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList1(self, head):
        if not head:
            return None
        pt = head
        pre = head.next
        pt.next = None
        while pre:
            tmp = pre.next
            pre.next = pt
            pt = pre
            pre = tmp
        return pt

    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p



if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = solution.reverseList(head)
    print res