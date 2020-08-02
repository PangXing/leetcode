# coding:utf-8
from Queue import deque

class Solution(object):
    def minial(self, maze, start, target):
        '''使用BST最小步数'''
        q = deque()
        rows = len(maze)
        cols = len(maze[0])
        setep = 0
        q.append(start)
        visited = set()
        visited.add(start)
        while q:
            for i in range(len(q)):
                pos = q.popleft()
                if pos == target:
                    return setep
                if pos[1] < cols-1 and (pos[0], pos[1]+1) not in visited and maze[pos[0]][pos[1]+1] != '#':
                    q.append((pos[0], pos[1]+1))
                    visited.add((pos[0], pos[1]+1))
                if pos[1] > 0 and (pos[0], pos[1] - 1) not in visited and maze[pos[0]][pos[1] - 1] != '#':
                    q.append((pos[0], pos[1] - 1))
                    visited.add((pos[0], pos[1] - 1))
                if pos[0] < rows-1 and (pos[0] + 1, pos[1]) not in visited and maze[pos[0]+1][pos[1]] != '#':
                    q.append((pos[0]+1, pos[1]))
                    visited.add((pos[0]+1, pos[1]))
                if pos[0] > 0 and (pos[0]-1, pos[1]) not in visited and maze[pos[0]-1][pos[1]] != '#':
                    q.append((pos[0]-1, pos[1]))
                    visited.add((pos[0]-1, pos[1]))
            setep += 1
        return 0


    def minimalSteps(self, maze):
        '''
        S->O 最小步数
        O->M sum（每个M最小步数）
        M->T min (每个M最小步数)
        '''
        start = (0, 0)
        M_list = list()
        O_list = list()
        T_pos = (0, 0)
        for i in range(len(maze)):
            for k in range(len(maze[i])):
                pos = (i, k)
                if maze[i][k] == 'S':
                    start = pos
                elif maze[i][k] == 'O':
                    O_list.append(pos)
                elif maze[i][k] == 'M':
                    M_list.append(pos)
                elif maze[i][k] == 'T':
                    T_pos = pos
        if len(O_list) == 0 and len(M_list) > 0:
            return -1

        if list(M_list) == 0:
            return self.minial(maze, start, T_pos)

        #S->O 最小步数
        s_o_steps = self.minial(maze, start, O_pos)
        if s_o_steps == 0:
            return -1

        #O->M sum（每个M最小步数）
        #  M->T min (每个M最小步数)
        min_steps = float('inf')
        for i in M_list:
            o_m_steps = 0
            for m in M_list:
                if m == i:
                    continue
                o_m = self.minial(maze, O_pos, m)
                if o_m == 0:
                    return -1
                else:
                    o_m_steps += 2*o_m
            o_m = self.minial(maze, O_pos, i)
            if o_m == 0:
                return -1
            m_t = self.minial(maze, i, T_pos)
            if m_t == 0:
                return -1
            tmp = o_m_steps + o_m +m_t
            if min_steps > tmp:
                min_steps = tmp

        return s_o_steps + min_steps



if __name__ == '__main__':
    solution = Solution()
    maze = ["S#O", "M..", "M.T"]
    maze = ["S#O", "M.T", "M.."]
    maze = ["S#O", "M.#", "M.T"]
    maze = ["OOOOO","OS#OO","#O#TO","M#OOO"]
    print solution.minimalSteps(maze)

