# coding:utf-8

'''
【785. 判断二分图】
给定一个无向图graph，当这个图为二分图时返回true。
如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。
graph将会以邻接表方式给出，graph[i]表示图中与节点i相连的所有节点。每个节点都是一个在0到graph.length-1之间的整数。这图中没有自环和平行边： graph[i] 中不存在i，并且graph[i]中没有重复的值。

示例 1:
输入: [[1,3], [0,2], [1,3], [0,2]]
输出: true
解释:
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。

示例 2:
输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
输出: false
解释:
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。

注意:
graph 的长度范围为 [1, 100]。
graph[i] 中的元素的范围为 [0, graph.length - 1]。
graph[i] 不会包含 i 或者有重复的值。
图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。
'''

class UnionFind(object):
    def __init__(self, n):
        self._parents = list()
        self._size = list()
        self._cnt = n
        for i in range(n):
            self._parents.append(i)
            self._size.append(1)

    def _find(self, p):
        while self._parents[p] != p:
            self._parents[p] = self._parents[self._parents[p]]
            p = self._parents[p]
        return p

    def union(self, p, q):
        root_p = self._find(p)
        root_q = self._find(q)

        if root_p != root_q:
            if self._size[root_p] < self._size[root_q]:
                self._parents[root_p] = root_q
                self._size[root_q] += self._size[root_p]
            else:
                self._parents[root_q] = root_p
                self._size[root_p] += self._size[root_q]
            self._cnt -= 1

    def connected(self, p, q):
        root_p = self._find(p)
        root_q = self._find(q)
        return root_p == root_q

    def get_cnt(self):
        return self._cnt

class Solution(object):
    def isBipartite(self, graph):
        '''
        图中每个顶点的所有邻接点都应该属于同一集合，且不与顶点处于同一集合
        '''
        if not graph:
            return False
        uf = UnionFind(len(graph))
        for i in graph:
            if len(i) > 1:
                for k in range(1, len(i)):
                    uf.union(i[k], i[k-1])
        for i in range(len(graph)):
            for k in graph[i]:
                if uf.connected(i, k):
                    return False
        return True

if __name__ == '__main__':
    solution = Solution()
    graph = [[1,3], [0,2], [1,3], [0,2]]
    graph =  [[1,2,3], [0,2], [0,1,3], [0,2]]
    print solution.isBipartite(graph)