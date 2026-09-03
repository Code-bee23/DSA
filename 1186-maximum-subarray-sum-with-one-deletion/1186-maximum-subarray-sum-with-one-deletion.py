class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_power = arr[0]
        power = float('-inf')
        res = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]

            # Maximum sum ending here without deletion
            no_power_new = max(x, no_power + x)

            # Maximum sum ending here with one deletion
            power_new = max(power + x,no_power)

            no_power = no_power_new
            power = power_new

            res = max(res, no_power, power)

        return res