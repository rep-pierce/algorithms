function openOrSenior(data){
    let lst = []
    for (let i = 0; i < data.length; i++){
      if (data[i][0] >= 55 && data[i][1] > 7){
        lst.push('Senior')
      }else {
          lst.push('Open') ;
        }
  }    return lst
  }