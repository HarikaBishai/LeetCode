/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let l = 0
    let maxLen = 0
    seen = new Set()
    for(let r=0;r<s.length;r++) {
        while (seen.has(s[r])) {
            seen.delete(s[l])
            l+=1
        }
        seen.add(s[r])
        maxLen = Math.max(r-l+1, maxLen)
    }
    return maxLen
};