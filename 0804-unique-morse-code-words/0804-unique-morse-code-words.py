class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            code = " "
            for ch in word:
                index = ord(ch)-ord('a')
                code += morse_code[index]

            result.add(code)
        return len(result)