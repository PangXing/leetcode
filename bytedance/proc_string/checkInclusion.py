# coding:utf-8

class Solution(object):
    def _revolve_s1(self, s1):
        self._s1_dict = dict()
        for i in s1:
            self._s1_dict.setdefault(i, 0)
            self._s1_dict[i] += 1

    def _check_ok(self, s2):
        s2_dict = dict()
        for i in s2:
            if i not in self._s1_dict:
                return False
            s2_dict.setdefault(i, 0)
            s2_dict[i] += 1

        for k, v in self._s1_dict.items():
            val = s2_dict.get(k, 0)
            if val != v:
                return False
        return True

    def checkInclusion(self, s1, s2):
        if not s1 or not s2:
            return False
        self._revolve_s1(s1)
        low = high = 0
        while high < len(s2):
            if s2[high] in s1:
                if (high - low + 1) == len(s1):
                    if self._check_ok(s2[low:high + 1]):
                        return True
                    else:
                        low += 1
            else:
                low = high + 1
            high += 1
        return False

if __name__ == '__main__':
    solution = Solution()
    print solution.checkInclusion('ab', 'eidbaooo')
    print solution.checkInclusion('ab', 'eidboaoo')
