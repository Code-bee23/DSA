class Solution:
    def defangIPaddr(self, address: str) -> str:
        #return address.replace(".","[.]") -----> Method 1

        #method - 2:
        result = ""

        for ch in address:
            if ch == ".":
                result += "[.]"


            else:
                result += ch

        return result