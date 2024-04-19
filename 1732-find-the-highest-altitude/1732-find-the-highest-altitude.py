class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0]
        highest_altitude = 0
        
        for i in range(0, len(gain)):
            a = gain[i] + prefix_sum[i]
            prefix_sum.append(a)
            if highest_altitude < a:
                highest_altitude = a
        
        print(prefix_sum)
        return highest_altitude
            