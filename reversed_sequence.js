const reverseSeq = n => {
    let lst = []
    while (n > 0){
      lst.push(n--)
    }
    return lst;
  };