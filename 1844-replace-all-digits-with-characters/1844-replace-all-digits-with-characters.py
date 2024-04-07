class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        
        for i in range(len(s)):
            if i % 2 != 0:
                b = chr(ord(s[i-1])+ int(s[i]))
                res += b
            else:
                res += s[i]
        
        return res