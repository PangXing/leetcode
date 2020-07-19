# coding:utf-8

class Solution(object):
    def twoSum(self, numbers, target):
        low = 0
        high = len(numbers) - 1
        while low < high:
            sums = numbers[low] + numbers[high]
            if sums == target:
                return [low+1, high+1]
            elif sums < target:
                low += 1
            else:
                high -= 1
        return [0, 0]

if __name__ == '__main__':
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print solution.twoSum(numbers, target)