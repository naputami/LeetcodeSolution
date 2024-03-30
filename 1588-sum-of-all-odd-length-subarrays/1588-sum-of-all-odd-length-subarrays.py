class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum = [0] * (len(arr) + 1)
        
        for i in range(len(arr)):
            prefix_sum[i + 1] =  prefix_sum[i] + arr[i]
            
        result = 0
        
        for i in range(1, len(arr) +1, 2):
            for j in range(len(arr) - i + 1):
                result += prefix_sum[j+i] - prefix_sum[j]
        
        return result