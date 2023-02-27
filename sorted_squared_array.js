function sortedSquaredArray(array) {
    let squaredArray = []
    for (let arrIdx = 0; arrIdx < array.length; arrIdx++){
      squaredArray.push(array[arrIdx] * array[arrIdx])
    }
    return squaredArray.sort((a, b) => a - b)
  }
  
  
//   //    BEST SOLUTION 1
//   function sortedSquaredArray(array) {
//     return array.map(val => val ** 2).sort((a,b) => a - b)
//   }


//   function sortedSquaredArray(array) {
//     let squaredArray = []
//     let leftIdx = 0
//     let rightIdx = array.length - 1
//     while (leftIdx !== rightIdx && leftIdx < rightIdx){
//       let leftNum = array[leftIdx]*array[leftIdx]
//       let rightNum = array[rightIdx]*array[rightIdx]
//       if (leftNum > rightNum){
//         squaredArray.unshift(leftNum)
//         leftIdx++
//       }else if (leftNum < rightNum){
//         squaredArray.unshift(rightNum)
//         rightIdx--
//       }else if (leftNum === rightNum){
//         squaredArray.unshift(leftNum)
//         squaredArray.unshift(rightNum)
//         leftIdx++
//         rightIdx--
//       }
//     }
//     if (leftIdx > rightIdx){
//       return squaredArray
//     }else {
//       squaredArray.unshift(array[leftIdx]*array[leftIdx])
//     }
//     return squaredArray
//   }
  

//   function sortedSquaredArray(array) {
//     const last = array.length - 1
//     let startPointer = 0
//     let endPointer = last
//     const newArr = new Array(array.length)
  
//     for (let i = last; i > -1; i--){
//       const start = array[startPointer] ** 2
//       const end = array[endPointer] ** 2
  
//       if (end > start) {
//         newArr[i] = end
//         endPointer--
//       } else {
//         newArr[i] = start
//         startPointer++
//       }
//     }
//     return newArr
//   }
  