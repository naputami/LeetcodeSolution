import java.util.ArrayList;
class Solution {
    public int[] decompressRLElist(int[] nums) {
        ArrayList<Integer> a = new ArrayList<Integer>();
        
        for(int i = 0; i < nums.length; i+=2){
            int freq = nums[i];
            int val = nums[i+1];
            
            int b = 0;
            
            while(b < freq){
                a.add(val);
                b++;
            }
        }
        
        int[] result = new int[a.size()];
        
        for(int i = 0; i < result.length; i++){
            result[i] = a.get(i);
        }
        
        return result;
    }
}