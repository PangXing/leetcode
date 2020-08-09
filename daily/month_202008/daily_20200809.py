# coding:utf-8

'''
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。



示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

'''

class Solution(object):
    '''
    回溯 + 剪枝
    '''
    def __init__(self):
        self.address = dict()

    def ipAddresses(self, s, n):
        if (s, n) in self.address:
            return self.address[(s, n)]
        size = len(s)
        res = list()
        if not s or n == 0 or size > n*3 or size < n:
            pass
        elif size == n*3:
            tmp = list()
            for i in range(n):
                ip = s[(i*3):(i*3+3)]
                if ip[0] == '0' or int(ip) > 255:
                    break
                tmp.append(ip)
            if len(tmp) == n:
                res.append('.'.join(tmp))
        elif n == 1:
            if size > 1 and s[0] == '0':
                pass
            elif int(s) < 256:
                res.append(s)
        else:
            tmp = s[0]
            tmp_list = self.ipAddresses(s[1:], n-1)
            for i in tmp_list:
                res.append(tmp + '.' + i)
            if size > 1 and s[0] != '0':
                tmp = s[0:2]
                tmp_list = self.ipAddresses(s[2:], n - 1)
                for i in tmp_list:
                    res.append(tmp+'.'+i)
            if size > 2 and s[0] != '0' and int(s[0:3]) < 256:
                tmp = s[0:3]
                tmp_list = self.ipAddresses(s[3:], n - 1)
                for i in tmp_list:
                    res.append(tmp+'.'+i)
        self.address[(s,n)] = res
        return res


    def restoreIpAddresses(self, s):
        res = self.ipAddresses(s, 4)
        return res

if __name__ == '__main__':
    solution = Solution()
    s = "25525511135"
    s = "0000"
    s = "010010"
    print solution.restoreIpAddresses(s)