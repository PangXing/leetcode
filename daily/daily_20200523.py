# coding:utf-8

class Solution(object):
    def is_ok(self, ok_dict):
        for v in ok_dict.values():
            if v[0] < v[1]:
                return False
        return True

    def minWindow(self, s, t):
        ok_dict = dict()
        for i in t:
            ok_dict[i] = [0, 0]
        for i in t:
            ok_dict[i][1] += 1

        low = 0
        high = 0
        size = len(s)
        min_str = ''
        while high < size:
            if s[high] in t:
                ok_dict[s[high]][0] += 1

                while self.is_ok(ok_dict):
                    if not min_str:
                        min_str = s[low:high+1]
                    elif (high - low + 1) < len(min_str):
                        min_str = s[low:high+1]

                    if s[low] in t:
                        ok_dict[s[low]][0] -= 1
                    low += 1
            high += 1
        return min_str

if __name__ == '__main__':
    solution = Solution()
    print solution.minWindow("ADOBECODEBANC", "ABC")


