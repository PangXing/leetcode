# coding:utf-8

'''
【990. 等式方程的可满足性】
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

示例 1：
输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。

示例 2：
输出：["b==a","a==b"]
输入：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。

示例 3：
输入：["a==b","b==c","a==c"]
输出：true

示例 4：
输入：["a==b","b!=c","c==a"]
输出：false

示例 5：
输入：["c==c","b==d","x!=z"]
输出：true

提示：
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] 和 equations[i][3] 是小写字母
equations[i][1] 要么是 '='，要么是 '!'
equations[i][2] 是 '='
'''

class Solution(object):
    '''
    Union-Find
    '''
    def is_ok(self, left, right, equal):
        self._gragh.setdefault(left, [set(left), set()])
        self._gragh.setdefault(right, [set(right), set()])
        if equal == '=':
            set_0 = self._gragh[left][0] | self._gragh[right][0]
            set_1 = self._gragh[left][1]
            for i in set_0:
                set_0 = set_0 | self._gragh[i][0]
                set_1 = set_1 | self._gragh[i][1]
            if set_0 & set_1:
                return False
            else:
                for i in set_0:
                    self._gragh[i][0] = set_0
                    self._gragh[i][1] = set_1
        else:
            self._gragh[left][1].add(right)
            self._gragh[right][1].add(left)
            if self._gragh[left][0] & self._gragh[right][0]:
                return False
        return True

    def equationsPossible(self, equations):
        self._gragh = dict()
        for i in equations:
             left = i[0]
             right = i[3]
             equal = i[1]
             if not self.is_ok(left, right, equal):
                 return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print solution.equationsPossible([['a', '=', '=', 'b'], ['b', '!', '=', 'a']])
    print solution.equationsPossible([['a', '=', '=', 'b'], ['b', '=', '=', 'a']])
    print solution.equationsPossible(["a==b","e==c","b==c","a!=e"])