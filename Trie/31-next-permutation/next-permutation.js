/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    n = nums.length
    if (n===0 || n === 1) {
        return nums
    }

       
    let index = -1
    for(let i=n-2; i>=0; i-- ) {
        if(nums[i] < nums[i+1]) {
            index = i
            break
        }
    }

    if(index===-1) {
        return nums.sort((a,b)=> {return a-b})
    }

    for (let i=n-1; i>index; i--) {
        if(nums[i]> nums[index]) {
            temp = nums[i]
            nums[i] = nums[index]
            nums[index] = temp
            break;
        }
    }


    nums.push(...nums.splice(index+1).sort((a, b) => a - b))
    return nums
};