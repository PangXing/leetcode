# coding:utf-8

class Node(object):
    def __init__(self, val=0, neignbors=[]):
        self.val = val
        self.neighbors = neignbors

class Solution(object):
    def __init__(self):
        self.visited = dict()

    def cloneGraph(self, node):
        if not node:
            return None
        if node.val in self.visited:
            return self.visited[node.val]
        root = Node(node.val)
        self.visited[root.val] = root
        neighbors = []
        for i in node.neighbors:
            tmp = self.cloneGraph(i)
            neighbors.append(tmp)
        root.neighbors = neighbors
        return root

if __name__ == '__main__':
    solution = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    root = solution.cloneGraph(node2)
    print root


