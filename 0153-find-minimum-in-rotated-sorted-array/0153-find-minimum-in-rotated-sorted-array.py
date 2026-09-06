class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0 
        high = n-1
        res = 0 

        while (low <= high):
            guess = (low+high)//2

            if nums[guess] > nums[n-1]:
                low = guess + 1

            else:
                res = guess
                high = guess - 1

        return nums[res]