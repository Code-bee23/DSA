class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        res = 0

        while temp > 0:
            d = temp % 10
            res = res * 10 + d
            temp = temp // 10

        return res == x
