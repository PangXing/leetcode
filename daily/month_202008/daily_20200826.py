# coding:utf-8

class Solution(object):

    def letterDFS(self, digits, res):
        if not digits:
            return res
        letter = int(digits[0])
        res1 = list()
        if letter >=2 and letter <= 9:
            lts = list()
            if letter <= 6:
                lts.append(chr(ord('a') + (letter - 2)*3 + 0))
                lts.append(chr(ord('a') + (letter - 2) * 3 + 1))
                lts.append(chr(ord('a') + (letter - 2) * 3 + 2))
            elif letter == 7:
                lts.append('p')
                lts.append('q')
                lts.append('r')
                lts.append('s')
            elif letter == 8:
                lts.append('t')
                lts.append('u')
                lts.append('v')
            elif letter == 9:
                lts.append('w')
                lts.append('x')
                lts.append('y')
                lts.append('z')

            if not res:
                for k in lts:
                    res1.append(k)
            else:
                for i in res:
                    for k in lts:
                        res1.append(i + k)
        else:
            res1 = res
        return self.letterDFS(digits[1:], res1)

    def letterCombinations(self, digits):
        return  self.letterDFS(digits, [])


if __name__ == '__main__':
    solution = Solution()
    digits = '23'
    print solution.letterCombinations(digits)