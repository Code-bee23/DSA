class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p)>len(s):
            return []

        result = []

        #frequency of p
        need = {}

        for ch in p:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        #frequency of current window
        window = {}
        left = 0

        for right in range(len(s)):
            ch = s[right]

            if ch in window:
                window[ch] += 1

            else:
                window[ch] = 1
            
            if (right-left+1) > len(p):
                leftChar = s[left]

                window[leftChar] -= 1

                if window[leftChar] == 0:
                    del window[leftChar]

                left += 1
            
            if window == need:
                result.append(left)

        return result
