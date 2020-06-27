# coding:utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        if not head:
            return head

        nodeset = set()
        nodeset.add(head.val)
        p = head
        while p and p.next:
            if p.next.val in nodeset:
                p.next = p.next.next
            else:
                nodeset.add(p.next.val)
                p = p.next
        return head

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(2)
    head.next.next.next.next.next = ListNode(1)
    res = solution.removeDuplicateNodes(head)
    print res
