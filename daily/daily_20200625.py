# coding:utf-8

class Solution(object):
    def __init__(self):
        self.dp = dict()

    def wordBreak(self, s, wordDict):
        if s in self.dp:
            return self.dp[s]

        high = 1
        while high <= len(s):
            if s[:high] in wordDict:
                if high < len(s):
                    if self.wordBreak(s[high:], wordDict):
                        self.dp[s] = True
                        return True
                else:
                    self.dp[s] = True
                    return True
            high += 1

        self.dp[s] = False
        return False


if __name__ == '__main__':
    solution = Solution()
    print solution.wordBreak("leetcode", ["leet", "code"])
    print solution.wordBreak("applepenapple", ["apple", "pen"])
    print solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])

