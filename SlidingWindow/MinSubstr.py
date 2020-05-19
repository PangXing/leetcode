# coding:utf-8

class Solution(object):
    def minSubStr(self, S, T):
        def is_sub_str(T_dict):
            for v in T_dict.values():
                if v == 0:
                    return False
            return True


        res = list()
        left = 0
        right = 0
        window_dict = {} #窗口中各个字母出现的次数
        for i in T:
            window_dict[i] = 0
        while right < len(S):
            #扩大窗口做什么
            if S[right] in T:
                window_dict[S[right]] += 1
            right += 1

            #缩小窗口做什么
            while is_sub_str(window_dict):
                res.append(S[left:right + 1])
                if S[left] in T:
                    window_dict[S[left]] -= 1
                left += 1

        min_str= ''
        if res:
            min_str = res[0]
            for i in res:
                if len(i) < len(min_str):
                    min_str = i
        return min_str

if __name__ == '__main__':
    solution = Solution()
    print solution.minSubStr('ADOBECODEBANYC', 'ABC')










