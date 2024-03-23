class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sumNum = 0
        sumDigit = 0
        for i in range(len(nums)):
            sumNum += nums[i]
            a = list(str(nums[i]))
            if len(a) > 1:
                b = sum([int(item) for item in a])
                sumDigit += b
            else:
                sumDigit += nums[i]
        
        return abs(sumNum - sumDigit)
                  

          
            
        