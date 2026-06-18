class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num],i]

            seen[num] = i

obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))