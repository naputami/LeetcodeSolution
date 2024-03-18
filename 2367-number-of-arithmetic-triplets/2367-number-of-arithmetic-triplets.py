class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            j = nums[i] + diff
            k = j + diff
            
            if j in nums and k in nums:
                count += 1
        
        return count