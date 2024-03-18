import java.util.Arrays;
class Solution {
    private boolean checkNum(int num, int[] nums){
        boolean result = false;
        
        for(int item: nums){
            if(num == item){
                result = true;
                break;
            }
        }
        
        return result;
    }
    
    public int arithmeticTriplets(int[] nums, int diff) {
        int count = 0;
        
        for(int i = 0; i < nums.length; i++){
            int j = diff + nums[i];
            int k = j + diff;
            
            if(checkNum(j, nums) && checkNum(k, nums)){
                count++;
            }
        }
        
        return count;
    }
}