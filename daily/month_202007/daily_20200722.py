# coding:utf-8

class Solution(object):
    def minArray(self, numbers):
        low = 0
        high = len(numbers) -1
        while low < high:
            mid = low + (high-low)/2
            if numbers[mid] < numbers[high]:
                high= mid
            elif numbers[mid] >numbers[high]:
                low = mid + 1
            else:
                high -= 1
        return numbers[low]

if __name__ == '__main__':
    solution = Solution()
    numbers = [3,4,5,1,2]
    numbers = [2,2,2,2,2,1]
    #numbers = [1, 3, 5]
    #numbers = [3, 1, 2]
    numbers = [3, 1, 1, 1, 1]
    print solution.minArray(numbers)
