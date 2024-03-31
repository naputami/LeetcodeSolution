class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        result = ""
        
        for i in range(len(s)):
            if s[i] == "1":
                count+=1
        
        for i in range(len(s)):
            if i == len(s)-1:
                result += "1"
            else:
                if count-1 > 0:
                    result += "1"
                    count-=1
                else:
                    result += "0"
        
        return result
            
            
        