function strStr(haystack, needle) {
    const needleLength = needle.length
    let idxStack = 0
    let hayArr = haystack.split("")
    let needleArr = needle.split("")
    while (idxStack < haystack.length) {
        if (needleArr.join("") === hayArr.slice(idxStack, idxStack + needleLength).join("")) {
            return idxStack
        }
        else {
            idxStack += 1
        }

    }
    return -1
}


strStr("sadbutsad", "sad")
strStr("leetcode", "leeto")