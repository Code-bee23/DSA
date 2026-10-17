class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        low  = 1
        high = max(bloomDay)
        if m * k > len(bloomDay):
            return -1

        while low < high:
            mid = (low+high)//2
            flow = 0
            bouq = 0
            for a in bloomDay:
                if a > mid:
                    flow = 0

                else:
                    flow += 1
                
                if flow >= k:
                    flow = 0
                    bouq += 1

                    if bouq == m:
                        break
            
            if bouq >= m:
                high = mid

            else:
                low = mid + 1
        
        return low