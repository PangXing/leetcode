# coding:utf-8

class Solution(object):
    def __init__(self):
        self.flags = dict()

    def iscallback(self, s):
        if s in self.flags:
            return self.flags[s]
        flag = True
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                flag = False
                break
            l += 1
            r -= 1
        self.flags[s] = flag
        return flag

    def cntSubstr(self, s):
        size = len(s)
        if size <= 1:
            return 0
        if size == 2:
            cnt = 0
            if s[0] == s[1]:
                cnt += 1
            return cnt
        if size == 3:
            cnt = 0
            if s[0] == s[-1]:
                cnt += 1
            if s[0] == s[1]:
                cnt +=1
            if s[1] == s[2]:
                cnt += 1
            return cnt
        res = 0
        if s[0] == s[-1] and self.iscallback(s[1:size-1]):
            res += 1
            res += self.cntSubstr(s[1:size-1])
        res += self.cntSubstr(s[1:])
        res += self.cntSubstr(s[:size-1])
        return res

    def countSubstrings(self, s):
        cnt = len(s)
        if cnt <= 1:
            return cnt
        cnt += self.cntSubstr(s)
        return cnt

if __name__ == '__main__':
    solution = Solution()
    s = "aaaaa"
    print solution.countSubstrings(s)

