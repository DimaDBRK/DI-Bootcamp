// Daily Challenge - Right & Left
// Instructions
// Download this Github repository.
// Create an fs.js file and use the Node js File System to read the RightLeft file. In the file, you will see a list of symbols : > and <. Each one of this symbol has a meaning:
// > means that you move 1 step to the right
// < means that you move 1 step to the left
// Example:
// When you start reading the file, you start at the position 0
// If the file begins like this ">>>" after 3 steps you would be in position 3
// If the file begins like this ">>><<" after 5 steps you would be in position 1

const { error } = require('console');
let fs = require('fs');

function start() {
    fs.readFile('RightLeft.txt', 'utf-8', function (err, data) {
        if (err) {
            console.error(err)
            return
        }
        const arrOfMoves = showData(data);
        // Use the corresponding operations to calculate the final position at the end of the file - The answer should be: 74 steps to the right.
        // Use the corresponding operations to calculate the number of steps needed to hit position the -1 for the first time - The answer should be: 1795 steps.
        findFinPosition(arrOfMoves, 0);
        findFinPosition(arrOfMoves, -1);
    });
}

function showData(data) {
    const arr = data.split('');
    console.log(arr);
    console.log("we recive moves, length:", arr.length)
    
    return arr
}
 
function leftOrRight(step) {
    let res = `Sorry, we don't know where you are`;
    if (step > 0) { 
        res = ' steps to the right ';
    } else if (step < 0) {
        res = ' steps to the left ';
    } else if (step === 0) {
        res = ' in the middle ';
    }
    return res
}

function findFinPosition(arrMoves, startPosition) {
    let position = startPosition;
    let step = 1;
    let check = true;
    arrMoves.forEach((move, index) => {
        if (["<",">"].includes(move)) {
            position += (move === "<") ? -1: 1;
            step += 1;
        } 
        if (position === -1 && startPosition === -1 && check) {
            console.log("We reach position - 1 in steps:", step)
            check = false;
        }
    });
   if (check) {console.log("final position: ", position, leftOrRight(position));}
}

start();