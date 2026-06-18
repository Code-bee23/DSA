class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0 :
            return 0

        binary = format(n,'032b')

        reversed_binary = binary[::-1]

        return int(reversed_binary,2)
