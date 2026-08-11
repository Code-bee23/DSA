class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp = (s+s)[1:-1]
        if s in temp:
            return True

        else:
            return False