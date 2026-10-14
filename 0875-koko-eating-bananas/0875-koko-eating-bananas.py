class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        def check(speed):
            h = 0
            for i in range(len(piles)):
                h = h + piles[i] // speed

                if (piles[i] % speed != 0):
                    h += 1
            return h

        def koko(guard):
            n = len(piles)
            low = 1
            high = max(piles)

            res = -1
            while low <= high:
                mid = (low + high)//2

                hour = check(mid)

                if hour > guard:
                    low = mid + 1

                else:
                    res = mid
                    high = mid - 1

            return res

        return koko(h)