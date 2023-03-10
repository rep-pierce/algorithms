// function squareSum(numbers){
//     let sum = 0
//     for (number of numbers){
//       sum += number**2
//     }
//     return sum
//   }

//   function squareSum(numbers){
//     let sumOfNumbers = 0
//     for (number of numbers){
//       let n = number**2
//       sumOfNumbers = sumOfNumbers + n ;
//     }
//     return sumOfNumbers;
//   }

  function squareSum(numbers){
    const sumsOfNumbers = [];
    for (number of numbers){    
      let n = number**2;
      sumsOfNumbers.push(n);
    }
    return sumsOfNumbers.reduce((partialSum, a) => partialSum + a, 0);
  }