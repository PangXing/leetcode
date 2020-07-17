# coding:utf-8

class Solution(object):
    def isPaliandrome(self, s):
        if len(s) < 2:
            return True

        low = 0
        high = len(s) -1
        while low < high:
            while not s[low].isalnum() and low < high:
                low += 1
            while not s[high].isalnum() and low < high:
                high -= 1

            if low < high:
                if s[low].lower() != s[high].lower():
                    return False
            low += 1
            high -= 1
        return True

if __name__ == '__main__':
    solution = Solution()
    #print solution.isPaliandrome("A man, a plan, a canal: Panama")
    #print solution.isPaliandrome("race a car")
    print solution.isPaliandrome(".,")


