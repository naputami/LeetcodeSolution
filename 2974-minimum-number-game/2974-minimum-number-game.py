class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        
        for i in range(len(nums_sorted)):
            if i % 2 != 0:
                temp = nums_sorted[i-1]
                nums_sorted[i-1] = nums_sorted[i]
                nums_sorted[i] = temp
        
        return nums_sorted
        