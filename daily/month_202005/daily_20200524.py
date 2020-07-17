# coding:utf-8

class Solution(object):
    def findMedianSortedArray(self, nums1, nums2):
        if not nums1:
            mid = len(nums2)/2
            if len(nums2)%2 == 1:
                return nums2[mid]
            else:
                return float(nums2[mid] + nums2[mid-1])/2
        if not nums2:
            mid = len(nums1) / 2
            if len(nums1) % 2 == 1:
                return nums1[mid]
            else:
                return float(nums1[mid] + nums1[mid - 1]) / 2


        if len(nums1) > len(nums2):
            short_list = nums2
            long_list = nums1
        else:
            short_list = nums1
            long_list = nums2

        low = 0
        high = len(short_list) - 1
        mid = (len(short_list) + len(long_list))/2
        i = low + (high - low + 1) / 2
        while low < high:
            i = low + (high - low + 1) / 2
            k = mid - i
            if short_list[i] <= long_list[k]:
                low = i + 1
            else:
                high = i - 1

        if i == 0:
            short_min = float("-inf")
            short_max = short_list[i]
        elif i == len(short_list):
            short_min = short_list[i-1]
            short_max = float("inf")
        else:
            short_min = short_list[i - 1]
            short_max = short_list[i]

        k = mid - i
        if k == 0:
            long_min = float("-inf")
            long_max = long_list[k]
        elif k == len(long_list):
            long_min = long_list[k - 1]
            long_max = float("inf")
        else:
            long_min = long_list[k - 1]
            long_max = long_list[k]

        mid_list = sorted([short_min, short_max, long_min, long_max])
        mid_num = mid_list[2] if (len(nums1) + len(nums2)) % 2 == 1 else float(mid_list[1] + mid_list[2])/2
        return mid_num

if __name__ == '__main__':
    solution = Solution()
    #print solution.findMedianSortedArray([1, 2], [3, 4])
    # print solution.findMedianSortedArray([1, 3], [2])
    # print solution.findMedianSortedArray([0, 0], [0, 0])
    # print solution.findMedianSortedArray([], [0, 0])
    # print solution.findMedianSortedArray([1], [1])
    # print solution.findMedianSortedArray([-1, 3], [1, 2])
    # print solution.findMedianSortedArray([10000], [10001])
    print solution.findMedianSortedArray([1], [2,3,4])




