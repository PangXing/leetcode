# coding:utf-8

class Solution(object):
    def __init__(self):
        self._res = dict()

    def try_find_all_res(self, K, W, sum):
        if sum >= K:
            self._res.setdefault(sum, 0)
            self._res[sum] += 1
            return
        for i in range(1, W+1):
            sum += i
            self.try_find_all_res(K, W, sum)
            sum -= i

    def new21Game(self, N, K, W):
        self.try_find_all_res(K, W, 0)
        all_cnt = 0
        N_cnt = 0
        for k, v in self._res.items():
            all_cnt += v
            if k <= N:
                N_cnt += v
        result = '%.5f'%(float(N_cnt)/all_cnt)
        return float(result)

if __name__ == '__main__':
    solution = Solution()
    #print solution.new21Game(10, 1, 10)
    #print solution.new21Game(6, 1, 10)
    print solution.new21Game(21, 17, 10)







