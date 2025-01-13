function minimumOperations(nums: number[]): number {
    let res = 0;

    for(const num of nums){
        if(num % 3 !== 0){
            res++;
        }
    }

    return res;
};