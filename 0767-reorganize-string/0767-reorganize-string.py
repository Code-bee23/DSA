import heapq
from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        f = defaultdict(int)
        for ch in s:
            f[ch] += 1

        pq = []
        for ch, freq in f.items():
            heapq.heappush(pq, (-freq, ch))

        res = ""
        prev = None
        while pq:
            freq, ch = heapq.heappop(pq)

            if ch == prev:

                if not pq:
                    return ""

                freq2, ch2 = heapq.heappop(pq)
                res += ch2
                prev = ch2

                freq2 += 1

                if freq2 < 0:
                    heapq.heappush(pq, (freq2, ch2))

                heapq.heappush(pq, (freq, ch))

            else:
                res += ch
                prev = ch
                freq += 1
                if freq < 0:
                    heapq.heappush(pq, (freq, ch))
        return res