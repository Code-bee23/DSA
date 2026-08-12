class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        vowel = "aeiouAEIOU"
        words = sentence.split()
        result = []
        for i,word in enumerate(words):
            if word[0] not in vowel:
                word = word[1:] + word[0]

            word = word +"ma"+"a"*(i+1)

            result.append(word)
        return " ".join(result)