function countPositivesSumNegatives(input) {
    let pos = 0
    let neg = 0
    if (input == '' || input == null){return []}
    input.forEach(number => {
      if (number > 0){
        pos++
      }else if(number < 0){
        neg = neg + number
      }
    })
    return [pos, neg]
  }