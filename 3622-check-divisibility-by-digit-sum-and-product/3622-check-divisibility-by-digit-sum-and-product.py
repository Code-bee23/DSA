class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ori_n = n
        digit_sum = 0
        digit_product = 1

        while n > 0:
            digit = n % 10

            digit_sum += digit
            digit_product *= digit
            
            n = n//10      #remove the last digit

            total = digit_sum + digit_product

        if ori_n % total == 0:
            return True
        else:
            return False

        