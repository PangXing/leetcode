# coding:utf-8
'''
【面试题 16.18. 模式匹配】
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

示例 1：
输入： pattern = "abba", value = "dogcatcatdog"
输出： true

示例 2：
输入： pattern = "abba", value = "dogcatcatfish"
输出： false

示例 3：
输入： pattern = "aaaa", value = "dogcatcatdog"
输出： false

示例 4：
输入： pattern = "abba", value = "dogdogdogdog"
输出： true
解释： "a"="dogdog",b=""，反之也符合规则

提示：
0 <= len(pattern) <= 1000
0 <= len(value) <= 1000
你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。
'''

class Solution(object):
    '''
    按照下面的二元表达式 不断遍历 a长度的枚举
    cnt_a * la + (lp - cnt_a) * lb = lv
     - cnt_a 为 pattern中 a的个数
     - la 为 A 的字符串长度 范围为 [0，lv/cnt_a]
    '''

    def match(self, pattern, value, la, lb):
        len_v = len(value)
        set_a = set()
        set_b = set()
        pos = 0
        for i in pattern:
            if i == 'a':
                if la != 0:
                    start = pos
                    end = pos + la
                    if end > len_v:
                        return False
                    set_a.add(value[start:end])
                    if len(set_a) > 1:
                        return False
                    pos = end
            else:
                if lb != 0:
                    start = pos
                    end = pos + lb
                    if end > len_v:
                        return False
                    set_b.add(value[start:end])
                    if len(set_b) > 1:
                        return False
                    pos = end
        return True

    def patternMatching(self, pattern, value):
        if pattern == '':
            return True if value == '' else False
        len_v = len(value)
        len_a = len(['a' for x in pattern if x == 'a'])
        len_b = len(pattern) - len_a
        if len_v == 0:
            return False if len_a > 0 and len_b > 0 else True
        if len_a == 0:
            if (len_v % len_b) == 0:
                return self.match(pattern, value, 0, len_v/len_b)
            else:
                return False
        if len_b == 0:
            if (len_v % len_a) == 0:
                return self.match(pattern, value, len_v/len_a, 0)
            else:
                return False

        max_len_a = len_v/len_a
        for i in range(max_len_a+1):
            if (len_v - i * len_a) % len_b == 0:
                lb = (len_v - i * len_a) / len_b
                if self.match(pattern, value, i, lb):
                    return True

        return False

if __name__ == '__main__':
    solution = Solution()
    pattern = "abba"
    value = "dogcatcatdog"
    value = "dogcatcatfish"

    pattern = "bbbbbbbbbbbbbbabbbbb"
    value = "ppppppppppppppjsftcleifftfthiehjiheyqkhjfkyfckbtwbelfcgihlrfkrwireflijkjyppppg"
    print solution.patternMatching(pattern, value)