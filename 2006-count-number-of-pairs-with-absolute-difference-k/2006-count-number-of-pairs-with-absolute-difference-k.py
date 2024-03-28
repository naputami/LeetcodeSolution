class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0;
        
        seen = dict()
        
        for num in nums:
            below, above = num - k, num + k
            if below in seen:
                count += seen[below]
            if above in seen:
                count += seen[above]
            seen[num] = seen.get(num, 0) + 1
        
        return count
                