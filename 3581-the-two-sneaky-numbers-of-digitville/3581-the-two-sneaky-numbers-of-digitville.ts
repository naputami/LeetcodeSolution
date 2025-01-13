function getSneakyNumbers(nums: number[]): number[] {
    const seenNumber = new Set();
    const res: number[] = [];

    for(const num of nums){
        if(seenNumber.has(num)){
            res.push(num);
        } else {
            seenNumber.add(num);
        }
    }

    return res;
    
};