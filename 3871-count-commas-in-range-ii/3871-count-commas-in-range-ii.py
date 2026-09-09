class Solution:
    def countCommas(self, n: int) -> int:

        start = 1000
        commas = 1
        result = 0

        while start <= n:

            end = start * 1000 - 1

            if n < end:
                end = n

            count = end - start + 1

            result += count * commas

            start *= 1000
            commas += 1

        return result