import heapq
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = defaultdict(int)
        for num in nums:
            f[num] += 1

        pq = []
        for element, freq in f.items():

            curr = (freq, element)

            if len(pq) < k:
                heapq.heappush(pq, curr)

            elif curr[0] > pq[0][0]:
                heapq.heappop(pq)
                heapq.heappush(pq, curr)

        res = []

        while pq:
            res.append(heapq.heappop(pq)[1])

        return res