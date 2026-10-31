class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high)//2
            daysNeeded = 1
            curr_weight = 0

            for weight in weights:

                if curr_weight + weight > mid:
                    daysNeeded += 1
                    curr_weight = weight

                else:
                    curr_weight = curr_weight + weight

                
            if daysNeeded <= days:
                high = mid

            else:
                low = mid + 1

        return low