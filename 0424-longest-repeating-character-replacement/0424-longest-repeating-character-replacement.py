class Solution:
    def characterReplacement(self, s, k):

        left = 0
        max_length = 0
        max_frequency = 0

        count = {}

        for right in range(len(s)):

            # Current character
            ch = s[right]

            # Frequency update
            count[ch] = count.get(ch, 0) + 1

            # Highest frequency
            max_frequency = max(max_frequency, count[ch])

            # Window invalid
            while (right - left + 1) - max_frequency > k:

                count[s[left]] -= 1
                left += 1

            # Maximum answer
            max_length = max(max_length, right - left + 1)

        return max_length