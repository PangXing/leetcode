# coding:utf-8

class Solution(object):
    def findMinMoves(self, machines):
        mac_len = len(machines)
        if sum(machines) % mac_len != 0:
            return -1
        agv = sum(machines)/mac_len
        moves = 0
        dp = list()
        for i in range(0, mac_len):
            if i == 0:
                after_agv = agv * len(machines[i + 1:])
                after_sum = sum(machines[i + 1:])
                pre_agv = 0
                pre_sum = 0
                dp.append([pre_agv, pre_sum, after_agv, after_sum])
            elif i == (mac_len-1):
                after_agv = 0
                after_sum = 0
                pre_agv = agv * len(machines[:i])
                pre_sum = sum(machines[:i])
                dp.append([pre_agv, pre_sum, after_agv, after_sum])
            else:
                after_agv = agv * len(machines[i + 1:])
                after_sum = sum(machines[i + 1:])
                pre_agv = agv * len(machines[:i])
                pre_sum = sum(machines[:i])
                dp.append([pre_agv, pre_sum, after_agv, after_sum])

        while(max(machines) != agv):
            for i in range(0, mac_len):
                if machines[i] > 0:
                    if dp[i][2] > dp[i][3]:
                        machines[i] -= 1
                        machines[i+1] += 1
                        dp[i][3] += 1
                    elif dp[i][0] > dp[i][1]:
                        machines[i] -= 1
                        machines[i - 1] += 1
                        dp[i][1] += 1

            moves += 1
        return moves


class Solution1(object):
    def findMinMoves(self, machines):
        n = len(machines)
        dress_total = sum(machines)
        if dress_total % n != 0:
            return -1

        dress_per_machine = dress_total // n
        for i in range(n):
            # Change the number of dresses in the machines to
            # the number of dresses to be removed from this machine
            # (could be negative)
            machines[i] -= dress_per_machine

        # curr_sum is a number of dresses to move at this point,
        # max_sum is a max number of dresses to move at this point or before,
        # m is number of dresses to move out from the current machine.
        curr_sum = max_sum = res = 0
        for m in machines:
            curr_sum += m
            max_sum = max(max_sum, abs(curr_sum))
            res = max(res, max_sum, m)
        return res


if __name__ == '__main__':
    solution = Solution()
    print solution.findMinMoves([1, 0, 5])
    print solution.findMinMoves([70245, 77822, 7921, 1696, 32988, 37651, 1, 83166, 87173, 49392, 98685, 48950, 50583, 96901, 74270, 3311, 51937,
     95628, 96270, 41493, 39529, 25251, 64928, 51521, 5389, 49035, 64882, 32584, 39051, 44316, 31435, 36445, 15868,
     76835, 80931, 92547, 54907, 71705, 33945, 90291, 86275, 84865, 54020, 31975, 82838, 64029, 28304, 17281, 90970,
     39213, 95015, 64762, 55453, 63014, 3404, 77131, 1466, 6411, 5576, 63345, 52692, 28875, 8027, 94433, 90719, 69686,
     22804, 53896, 91518, 30173, 56572, 15069, 97510, 75077, 71980, 26566, 75522, 74888, 27039, 56868, 47952, 29768,
     8801, 35932, 20136, 10320, 55399, 51138, 8189, 63722, 52729, 6980, 39036, 45622, 83530, 79184, 84754, 95854, 88840,
     91875])


