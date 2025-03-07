/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    
    let l = 0
    let r = height.length-1
    let res = 0
    while (l<r) {
        if (height[l]<=height[r]) {
            res = Math.max(res, (r-l) * (height[l]))
            l+=1
        } else {
            res = Math.max(res, (r-l) * (height[r]))
            r-=1
        }
    }

    return res
};