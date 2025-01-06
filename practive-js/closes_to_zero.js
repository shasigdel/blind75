var findClosestNumber = function(nums){
    let closest = Infinity;
    for(const num of nums){
        if (Math.abs(num)< Math.abs(closest)){
            closest = num
        }else if(Math.abs(num) === Math.abs(closest)){
            closest = Math.max(num, closest)
        }
    }
    return closest;
};


let nums = [-4,-2,1,4,8]
let nums2 = [-2,-1,1]
let result = findClosestNumber(nums2)
console.log(result)