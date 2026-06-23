class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n

        pre_prod = 1
        for i in range(0,n):
            ans[i] = pre_prod
            pre_prod = pre_prod * nums[i]

        post_prod = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * post_prod
            post_prod = post_prod * nums[i]

        return ans