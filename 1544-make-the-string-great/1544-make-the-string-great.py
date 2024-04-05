class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                a = stack[len(stack) - 1]
                if ord(s[i]) == (ord(a) - 32) or ord(s[i]) == (ord(a) + 32):
                    stack.pop()
                else:
                    stack.append(s[i])
        
        return "".join(stack)
        