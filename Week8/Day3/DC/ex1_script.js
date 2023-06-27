// DC
// Daily Challenge : Go Wildcats
// Instructions
// Using this array:

const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
   ];
// 1. Create an array using forEach that contains all the usernames from the gameInfo array, add 
// an exclamation point (ie. “!”) to the end of every username.
// The new array should look like this :
// const usernames = ["john!", "becky!", "susy!", "tyson!"]

// Option 1
const usernames1 = [];
gameInfo.forEach((element) =>  usernames1.push(element["username"] + "!"));
console.log(usernames1);

// Option 2
const usernames2 = gameInfo.map((element) => element["username"] + "!");
console.log(usernames2);

// 2. Create an array using forEach that contains the usernames of all players with a score bigger than 5.
// The new array should look like this :

// const winners = ["becky", "susy"]

// Option 1
const winners = [];
gameInfo.forEach((element) => {
    if (element["score"]  > 5) winners.push(element["username"]);
    
});
console.log(winners);

// Option 2
const winners2 = gameInfo.filter((element) => element["score"]  > 5).map((element) => element["username"]);
console.log(winners2);

// 3. Find and display the total score of the users. (Hint: The total score is 71)

const sum = gameInfo.reduce((accumulator, element) => {
    return accumulator + element["score"];
}, 0);
console.log(sum)