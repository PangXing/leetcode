# coding:utf-8

import random

class Solution(object):
    def __init__(self, N, blacklist):
        self._N = N
        self._blacklist = blacklist

    def pick(self):
        random_num = random.randint(0, self._N-1)
        while random_num in self._blacklist:
            if random_num == 0:
                random_num = self._N - 1
            else:
                random_num -= 1
        return random_num

if __name__ == '__main__':
    solution = Solution(2, [])
    print solution.pick()
    print solution.pick()