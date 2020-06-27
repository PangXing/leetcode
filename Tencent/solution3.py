# coding:utf-8

'''
count
input str
output int
'tencent,' 'atencent'
'ttencent'
'''

class Solution(object):
    def findstr(self, s):
        low = 0
        high = 0
        cnt = 0
        while high < len(s):
            if s[high] in 'tencent':
                if high - low == 7:
                    if s[low:high+1] == 'tencent':
                        flag = True
                        if low > 0 and s[low-1].isalph():
                            flag = False
                        if high < len(s)-1 and s[high+1].isalph():
                            flag = False
                        if flag:
                            cnt += 1
                    else:
                        low += 1
            else:
                low = high + 1
            high += 1
        return cnt
