import java.util.Arrays;
class Solution {
    public int[] decompressRLElist(int[] nums) {
        int resultSize = 0;
        
        for(int i = 0; i < nums.length; i+=2){
            resultSize += nums[i];
        }
        
        int[] result = new int[resultSize];
        
        int start = 0;
        
        for(int i = 0; i < nums.length; i+=2){
            Arrays.fill(result, start, start + nums[i], nums[i+1]);
            start+=nums[i];
        }
        
        return result;
        
        
    }
}