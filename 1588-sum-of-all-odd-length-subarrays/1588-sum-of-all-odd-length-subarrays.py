class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        
        for i in range(len(arr)):
            j = i
            while j < len(arr):
                result += sum(arr[i:j+1])
                j += 2
            
        return result
        
        