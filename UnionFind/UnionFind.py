# coding:utf-8

class UF(object):
    def __init__(self, n):
        # 存储原始数据父节点的索引 森林
        self._parent = list()
        # 每棵树的规模
        self._sizes = list()
        # 森林的数量
        self._cnt = n
        # 初始都是独立森林 指向自己
        for i in range(n):
            self._parent.append(i)
            self._sizes.append(1)

    def _find(self, p):
        '''
        查证 p 的root 节点
        '''
        while self._parent[p] != p:
            # 路径压缩
            self._parent[p] = self._parent[self._parent[p]]
            p = self._parent[p]
        return p

    def union(self, p, q):
        '''
        连接 p 与 q 节点
        '''
        root_p = self._find(p)
        root_q = self._find(q)
        if root_p != root_q:
            #小树 连到 大叔下 ，平衡
            if self._sizes[root_q] < self._sizes[root_p]:
                self._parent[root_q] = root_p
                self._sizes[root_p] += self._sizes[root_q]
            else:
                self._parent[root_p] = root_q
                self._sizes[root_q] += self._sizes[root_p]
            self._cnt -= 1

    def connected(self, p, q):
        '''
        判断p 与 q 节点的连通性
        '''
        root_p = self._find(p)
        root_q = self._find(q)
        return root_p == root_q

    def get_count(self):
        return self._cnt
