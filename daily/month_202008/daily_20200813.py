# coding:utf-8

class Solution(object):
    def _mult(self, str1, num2, pos):
        res = '0' * pos
        num = 0
        for i in str1[::-1]:
            tmp = int(i)*num2 + num
            str_tmp = str(tmp%10)
            num = tmp/10
            res = str_tmp + res
        if num > 0:
            res = str(num) + res
        if len(res) > 1:
            for pos in range(len(res)):
                if res[pos] != '0':
                    break
            res = res[pos:]
        return res

    def _add(self, str1, str2):
        res = ''
        pos = 0
        str1 = str1[::-1]
        str2 = str2[::-1]
        n1 = len(str1)
        n2 = len(str2)
        num = 0
        while pos < n1 and pos< n2:
            tmp = int(str1[pos]) + int(str2[pos])+ num
            pos += 1
            str_tmp = str(tmp % 10)
            num = tmp / 10
            res = str_tmp + res

        while pos < n1:
            tmp = int(str1[pos]) + num
            pos += 1
            str_tmp = str(tmp % 10)
            num = tmp / 10
            res = str_tmp + res
        while pos < n2:
            tmp = int(str2[pos]) + num
            pos += 1
            str_tmp = str(tmp % 10)
            num = tmp / 10
            res = str_tmp + res
        if num > 0:
            res = str(num) + res
        return res


    def multiply(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)

        res = '0'
        if n1 > 0 and n2 >0:
            for i in range(n2-1, -1, -1):
                tmp = self._mult(num1, int(num2[i]), n2-1-i)
                res = self._add(res, tmp)
        if not res:
            res = '0'
        return res

if __name__ == '__main__':
    solution = Solution()
    num1 = "123456789"
    num2 = "987654321"
    num1 = "140"
    num2 = "721"
    num1 = "9133"
    num2 = "0"
    print solution.multiply(num1, num2)
