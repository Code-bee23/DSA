class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        res = [0]*n

        left = 0
        right = n-1
        index = n-1

        while left<=right:
            left_sq = nums[left]*nums[left]
            
            right_sq = nums[right]*nums[right]

            if left_sq>right_sq:
                res[index] = left_sq
                left += 1

            else:
                res[index] = right_sq
                right -= 1
            
            index -= 1
        return res