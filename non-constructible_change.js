function nonConstructibleChange(coins) {
    if (coins.length === 0){
      return 1
    }
    const sortedCoins = coins.sort(function(a, b) {
      return a - b;
    })
    let change = 0
    for (let i = 0; i < sortedCoins.length; i++){
      if (change < sortedCoins[i] - 1){
        return change + 1
      }else {
        change += sortedCoins[i]
      }
    }
    return change + 1
}
coins = [5, 7, 1, 1, 2, 3, 22]

console.log(nonConstructibleChange(coins))