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

console.log(tournamentWinner([["ryan", "ashley"], ["adam", "jaxon"], ["ryan", "adam"], ["ryan", "jaxon"], ["ashley", "adam"], ["ashley", "jaxon"]], [1, 0, 0, 1, 0, 1]))