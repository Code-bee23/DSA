class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count_zeros = 0
        max_len = 0

        for right in range(len(nums)):

            if nums[right]==0:
                count_zeros += 1

            while count_zeros>k:
                
                if nums[left]==0:
                    count_zeros-=1

                left+=1
            max_len = max(max_len, right-left+1)

        return max_len