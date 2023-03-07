function persistence(num) {
    let counter = 0 ;
    let nm = num.toString() ;
    let len = nm.length ;
    while (len > 1){
      let total = parseInt(nm[0]) ;
      let i = len - 1 ;
      while (i > 0) {
        total = total * parseInt(nm[i]) ;
        --i ;
      }
      nm = total.toString() ;
      len = nm.length ;
      counter++ ;
    } 
    return counter ;
  }