class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        available = {}
        for ch in text:
            if ch in available:
                available[ch] += 1
            else:
                available[ch] = 1

        need = {
            'b' : 1,
            'a' : 1,
            'l' : 2,
            'o' : 2,
            'n' : 1
        }
        
        res = float('inf')
        for ch in need:
            if ch not in available:
                return 0
            times = available[ch] // need[ch]
            res = min(res, times)

        return res