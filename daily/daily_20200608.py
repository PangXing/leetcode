# coding:utf-8

class Solution(object):
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