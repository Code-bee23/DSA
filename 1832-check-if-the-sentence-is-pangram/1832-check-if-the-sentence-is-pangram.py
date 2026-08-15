class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique = set(sentence)

        if len(unique) == 26:
            return True
        else:
            return False

        #Method -2

        #return(len(set(sentence))==26)