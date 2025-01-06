/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let j = 0
    for(let i = 0; i < t.length; i++){
        if(s[j] === t[i]){
            j++
        }
    }
    return j >= s.length ? true : false
}



let s = 'abc'
let t = 'ahbgdc'
let result = isSubsequence(s,t)

console.log(result)