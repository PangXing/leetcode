# coding:utf-8

'''
BFS 本质就是让你在一副图中找到从起点start 到终点 target的最短距离
'''

from Queue import deque

def BFS(start, target):
    q = deque()
    visited = set()

    q.append(start)
    visited.add(start)
    step = 0

    while q:
        n = len(q)
        for i in range(n):
            cur = q.popleft()
            if cur == target:
                return step
            for k in cur.children:
                q.append(k)
                visited.add(k)
        step += 1






