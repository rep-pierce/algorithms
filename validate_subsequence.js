function isValidSubsequence(array, sequence) {
    let i = 0
    for (let num of array ){
      if (num === sequence[i]){
        i++
      }
    }
    return i === sequence.length
  }

//   function isValidSubsequence(array, sequence) {
//     let seqInt = 0
//     for (let arrInt = 0; arrInt < array.length; arrInt++){
//       if (array[arrInt] === sequence[seqInt]){
//         seqInt++
//       }
//     }
//     return seqInt < sequence.length? false : true
//   }

//   function isValidSubsequence(array, sequence) {
//     let arrNum = 0
//     let seqNum = 0
//     while (arrNum < array.length && seqNum < sequence.length) {
//       if (array[arrNum] === sequence[seqNum]){
//         seqNum += 1
//       }
//       arrNum += 1
//     }
//     return seqNum === sequence.length
//   }