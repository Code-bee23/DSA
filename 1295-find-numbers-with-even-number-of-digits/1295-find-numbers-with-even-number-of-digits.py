class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        ans = 0
        
        for num in nums:
            digit_count = 0    
            while num > 0:
                num = num//10

                digit_count += 1

            if digit_count%2 == 0:
                ans += 1

        return ans

