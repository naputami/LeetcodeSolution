function twoSum(nums: number[], target: number): number[] {
    const res: number[] = [];
    const seenNumber = new Set();

    for(let i = 0; i < nums.length; i++){
        const a = target - nums[i];

        if(seenNumber.has(a)){
            res.push(nums.indexOf(a), i);
        }

        seenNumber.add(nums[i])
    }

    return res;
    
};