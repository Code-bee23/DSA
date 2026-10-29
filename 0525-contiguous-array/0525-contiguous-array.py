class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0:-1}

        prefixSum = 0
        maxLength = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefixSum = prefixSum - 1

            else:
                prefixSum = prefixSum + 1

            if prefixSum in seen:
                length = i - seen[prefixSum]
                maxLength = max(maxLength,length)

            else:
                seen[prefixSum] = i

        return maxLength