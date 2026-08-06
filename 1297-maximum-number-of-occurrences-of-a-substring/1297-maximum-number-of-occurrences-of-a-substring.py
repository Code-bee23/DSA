from collections import defaultdict

class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):

        freq = defaultdict(int)

        answer = 0

        for i in range(len(s) - minSize + 1):

            # Current substring
            sub = s[i:i + minSize]

            # Check unique characters
            if len(set(sub)) <= maxLetters:

                freq[sub] += 1

                answer = max(answer, freq[sub])

        return answer