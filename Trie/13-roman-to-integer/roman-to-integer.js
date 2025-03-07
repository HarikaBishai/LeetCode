/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    out = 0

    for(let i = 0; i< s.length; i++) {
        curr = mapping[s[i]]
        next = mapping[s[i+1]]

        if(next > curr){
            out+= next-curr
            i+=1
        } else{
            out+= curr
        }
    }
    return out
};