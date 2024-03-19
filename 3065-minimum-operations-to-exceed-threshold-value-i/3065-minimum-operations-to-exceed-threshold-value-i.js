/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    count = 0;
    
    for(num of nums){
        if(num < k){
            count++;
        }
    }
    
    return count;
};