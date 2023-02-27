function tournamentWinner(competitions, results) {
    let points = {}
    for (let i = 0; i < competitions.length; i++){
        points[competitions[i][results[i] === 1? 0 : 1]]
        if (points[competitions[i][results[i] === 1? 0 : 1]] === undefined){
            points[competitions[i][results[i] === 1? 0 : 1]] = 3
        }else {
            points[competitions[i][results[i] === 1? 0 : 1]] += 3
        }
    }
    return Object.keys(points).reduce((a, b) => points[a] > points[b] ? a : b);
}

function tournamentWinnerOther(competitions, results) {
    const leader = {score: -Infinity, name: ''}
    const scoreboard = {}
  
    for (let i = 0; i < competitions.length; i++){
      const winnerIdx = results[i] === 0 ? 1 : 0
      const winner = competitions[i][winnerIdx]
  
      if (winner in scoreboard) scoreboard[winner] += 3
      else scoreboard[winner] = 3
  
      if (leader.score < scoreboard[winner]) {
        leader.name = winner
        leader.score = scoreboard[winner]
      }
    }
    return leader.name
  }
  
  // Do not edit the line below.
  exports.tournamentWinner = tournamentWinner;

console.log(tournamentWinner([["ryan", "ashley"], ["adam", "jaxon"], ["ryan", "adam"], ["ryan", "jaxon"], ["ashley", "adam"], ["ashley", "jaxon"]], [1, 0, 0, 1, 0, 1]))