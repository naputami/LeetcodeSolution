class Solution {
    public String replaceDigits(String s) {
        String res = "";
        
        for(int i = 0; i < s.length(); i++){
            if(i % 2 != 0){
                char shift = (char) ((int) s.charAt(i-1) + Character.getNumericValue(s.charAt(i)));
                res += shift;
            } else {
                res += s.charAt(i);
            }
        }
        
        return res;
    }
}