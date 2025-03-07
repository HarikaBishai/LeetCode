/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    
    if (nums1.length > nums2.length){
        [nums1, nums2] = [nums2, nums1]
    }

    const n1 = nums1.length
    const n2 = nums2.length

    total = n1+n2
    half = Math.floor(total/2)

    l = 0
    r = n1-1
    while(true) {
        n1Mid = Math.floor((l+r)/2)
        n2Mid = half - n1Mid - 2
        aLeft = n1Mid < 0 ? -Infinity : nums1[n1Mid]
        aRight = n1Mid + 1 >= n1 ? Infinity: nums1[n1Mid + 1]
        bLeft = n2Mid < 0 ? -Infinity : nums2[n2Mid]
        bRight = n2Mid + 1 >= n2 ? Infinity: nums2[n2Mid + 1]

        if(aLeft <= bRight && bLeft <= aRight) {
            if(total%2 === 0) {
                return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight))/2
            } else{
                return Math.min(aRight, bRight)
            }
        } else if (aLeft > bRight) {
            r = n1Mid-1
        } else {
            l = n1Mid+1
        }
    }


};