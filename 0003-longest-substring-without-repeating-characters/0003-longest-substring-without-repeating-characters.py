class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0 
        max_len = 0
        freq={}
        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high],0)+1
            
        
       #shrink window if distict character > k
            while freq[s[high]]>1:
                freq[s[low]] -=1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low +=1 
            max_len = max(max_len,high-low+1)
            
        return max_len