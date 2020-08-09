# coding:utf-8
from Queue import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        nodes = dict()
        for i in prerequisites:
            nodes.setdefault(i[0], list())
            nodes[i[0]].append(i[1])

        for i in range(numCourses):
            q = deque()
            visited = [False]*numCourses
            q.append(i)
            while q:
                for k in range(len(q)):
                    j = q.popleft()
                    if visited[j]:
                        return False
                    visited[j] = True
                    q.extend(nodes.get(j, list()))
        return True

if __name__ == '__main__':
    solution = Solution()
    numCourses = 3
    prerequisites = [[0,1],[0,2],[1,2]]
    print solution.canFinish(numCourses, prerequisites)

