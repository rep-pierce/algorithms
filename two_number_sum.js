function twoNumberSum(array, targetSum) {
    // Write your code here.
    for (let i = 0; i < array.length; i++){
      let firstNum = array[i]
      for (let j = i+1; j < array.length; j++){
        if (firstNum + array[j] === targetSum){
          return [firstNum, array[j]]
        }
      }
    }return []
  }

//   function twoNumberSum(array, targetSum) {
//     const seen = new Set()
//     for (let num of array){
//       if (seen.has(targetSum - num)){
//         return [targetSum - num, num]
//       }else{
//         seen.add(num)
//       }
//     }return []
//   }

//   function twoNumberSum(array, targetSum) {
//     let l = 0
//     let r = array.length - 1
  
//     array.sort((a, b) => a - b)
  
//     while(l<r){
//       let sum = array[l] + array[r]
//       if (sum === targetSum){
//         return [array[l], array[r]]
//       }else if (sum > targetSum){
//         r--
//       }else{
//         l++
//       }
//     }return []
//   }