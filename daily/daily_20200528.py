# coding:utf-8

class Solution(object):
    def decodeString(self, s):
        def _is_num(i):
            if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return True
            return False

        num_stack = list()
        alpha_stack = list()
        out_put = ''
        num_str = ''
        alpha_str = ''
        for i in s:
            if _is_num(i):
                num_str += i
            elif i == '[':
                num_stack.append(int(num_str))
                num_str = ''
                if len(num_stack) == 0:
                    out_put += alpha_str
                    alpha_str = ''
                alpha_stack.append(alpha_str)
                alpha_str = ''
            elif i == ']':
                num = num_stack.pop()
                alpha_str = num*alpha_str
                tmp = alpha_stack.pop()
                alpha_str = tmp + alpha_str
            else:
                alpha_str += i
        out_put += alpha_str
        return out_put

if __name__ == '__main__':
    solution = Solution()
    print solution.decodeString('3[a]2[bc]')
    print solution.decodeString('ab3[a2[bc]]')


