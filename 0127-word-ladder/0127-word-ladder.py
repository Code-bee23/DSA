from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        n = len(wordList)

        seen = set(wordList)

        if endWord not in seen:
            return 0

        q = deque()

        q.append((beginWord,1))

        while q:
            s,val = q.popleft()

            if s == endWord:
                return val 

            for i in range(len(s)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = s[:i] + ch + s[i+1:]

                    if new_word in seen:
                        seen.remove(new_word)
                        q.append((new_word,val+1))

        return 0