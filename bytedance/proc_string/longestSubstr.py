# coding:utf-8

class Solution(object):
    def lengthOfLongestSubsting(self, s):
        def _is_reduce(window):
            m_set = set()
            for i in window:
                if i in m_set:
                    return True
                else:
                    m_set.add(i)
            return False

        if not s:
            return 0
        low = 0
        high = 1
        size = len(s)
        longest_len = 0
        while high <= size:
            while _is_reduce(s[low:high]):
                low += 1
            longest_len = max(high-low, longest_len)
            high += 1
        return longest_len

if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLongestSubsting('abcabcbb')
    print solution.lengthOfLongestSubsting('pwwkew')





