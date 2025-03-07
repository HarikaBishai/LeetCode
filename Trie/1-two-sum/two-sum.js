/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let seen = {}
    let out = [-1,-1]
    for(let i=0;i<nums.length;i++) {
        num = nums[i]
        if(target-num in seen) {
            out = [i, seen[target-num ]]
            break;
        }
        seen[num] = i
    }
   

    return out
};