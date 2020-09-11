# coding:utf-8

class Solution(object):
    def isValid(self, s):
        stack = list()
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == ')' and stack.pop() != '(':
                    return False
            elif i == '}' and stack.pop() != '{':
                    return False
            elif i == ']' and stack.pop() != '[':
                    return False
        return len(stack) == 0

if __name__ == '__main__':
    solution = Solution()
    s = "()[]{}"
    s = "(]"
    print solution.isValid(s)

