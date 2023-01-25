const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

const myWatchedSeriesLength = myWatchedSeries.length

console.log('myWatchedSeriesLength:', myWatchedSeries.length);

const myWatchedSeriesSentence = (`${myWatchedSeries[0]}, ${myWatchedSeries[1]}, and ${myWatchedSeries[2]}`)

console.log(myWatchedSeriesSentence)

console.log(`I watched ${myWatchedSeriesLength} series : ${myWatchedSeriesSentence}`)

myWatchedSeries[2] = "friends"

console.log(myWatchedSeries)

myWatchedSeries.push("Sweet 16")

console.log(myWatchedSeries)

myWatchedSeries.unshift("Sweet November")

console.log(myWatchedSeries)

myWatchedSeries.splice(1, 1);

console.log(myWatchedSeries)

const moneyHeist = myWatchedSeries[1]

console.log(moneyHeist[2]);

console.log(myWatchedSeries);





