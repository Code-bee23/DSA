class Solution:
    def totalNumbers(self, digits):
        
        # Count how many times each digit appears
        count = [0] * 10
        
        for digit in digits:
            count[digit] += 1
        
        result = 0
        
        # Choose first digit
        for first in range(1, 10):
            
            if count[first] == 0:
                continue
            
            # Use the first digit
            count[first] -= 1
            
            # Choose second digit
            for second in range(10):
                
                if count[second] == 0:
                    continue
                
                # Use the second digit
                count[second] -= 1
                
                # Choose last digit
                for last in range(0, 10, 2):
                    
                    if count[last] > 0:
                        result += 1
                
                # Put second digit back
                count[second] += 1
            
            # Put first digit back
            count[first] += 1
        
        return result