function searchInsert(nums, target) {
    let idx = 0
    while (target > nums[idx]) {
        idx += 1
    }
    return idx
}

console.log(searchInsert([1,2,3,4], 5))
console.log(searchInsert([1,2,4,5,6], 5))
console.log(searchInsert([5,6,8,9], 5))