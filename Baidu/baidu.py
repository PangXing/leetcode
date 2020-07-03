# coding:utf-8

def findmax(l1):
    if not l1:
        return None
    if len(l1) < 2:
        return l1[0]
    if len(l1) < 3:
        return max(l1[0], l1[1])

    low = 0
    high = len(l1)-1

    while low <= high:
        mid = low + (high-low)/2

        if mid == 0 or mid == len(l1)-1:
            return l1[mid]

        if l1[mid] > l1[mid -1] and l1[mid] > l1[mid+1]:
            return l1[mid]

        if l1[mid] > l1[low]:
            low = mid + 1
        elif l1[mid] > l1[high]:
            high = mid -1

    return l1[high]

if __name__ == '__main__':
    l1 = [3, 5, 8, 7, 6, 2]
    l1 = [10, 7, 6, 2]
    l1 = [1, 2, 4]
    l1 = [4, 2, 1]
    l1 = []
    l1 = [1, 2]
    l1 = [3]
    print findmax(l1)