class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        #remove leading spaces
        while i<n and s[i] == ' ':
            i += 1
        
        #check the sign
        sign = 1
        if i<n and s[i] == "-":
            sign = -1
            i+=1

        elif i<n and s[i]=="+":
            i += 1

        #convert into digits
        number = 0

        while i<n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            number = number *10 +digit
            i += 1

        number = number * sign 

        #handle 32 bit
        if number < -2147483648:
            return -2147483648

        if number > 2147483647:
            return 2147483647

        return number