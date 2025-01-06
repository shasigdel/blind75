/**
 * @param {string} s
 * @return {number}
 */

var romanToInt = function(s){
    const romanValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    let result = 0
    let i = 0
    let n = s.length

    while (i < n){
        if(i < n - 1 && romanValues[s[i]] < romanValues[s[i+1]]){
            result += romanValues[s[i+1]] - romanValues[s[i]]
            i+= 2
        }else{
            result += romanValues[s[i]]
            i+=1
        }
    }
    return result

    // for (let i = 0; i < s.length; i++){
    //     const curr = romanValues[s[i]];
    //     const next = romanValues[s[i+1]];

    //     if (curr < next){
    //         result += next - curr;
    //         i++;
    //     }else{
    //         result += curr;
    //     }
    // }
    // return result
};

const s = "MCMXCIV"
let result = romanToInt(s)
console.log(result)