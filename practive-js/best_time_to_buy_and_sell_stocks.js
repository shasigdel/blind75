/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit = 0
    let profit = prices[0]

    for(let i =1; i < prices.length; i++){
        if(profit > prices[i]){
            profit = prices[i]
        }
        maxProfit = Math.max(maxProfit, prices[i] - profit)
    }

    return maxProfit
}

let prices = [7,1,5,3,6,4]
let result = maxProfit(prices)

console.log(result)