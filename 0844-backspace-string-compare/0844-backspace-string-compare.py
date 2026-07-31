class Solution:

    def build(self, string):

        stack = []

        for ch in string:

            # Normal character
            if ch != "#":
                stack.append(ch)

            # Backspace
            elif stack:
                stack.pop()

        return "".join(stack)

    def backspaceCompare(self, s, t):

        return self.build(s) == self.build(t)