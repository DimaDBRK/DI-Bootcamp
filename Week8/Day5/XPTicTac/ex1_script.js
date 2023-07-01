const xList = [];
const oList = [];
let move = 0;
let symbol = "X";
let moveType = "user";
let superPowerStatus = false;
// data
const winCombos = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [6, 4, 2]
]




//listeners
function addEventsToDiv() {
    Array.from(document.getElementsByClassName("cell")).forEach((element) => element.addEventListener("click", addElement));
    document.getElementById("clear").addEventListener("click", clear);
    document.getElementById("iplay").addEventListener("click", firstMove);
    document.getElementById("level").addEventListener("click", superPower);
}



//functions
function drawSymbols() {
    xList.forEach((element) => document.getElementById(element).textContent = "X");
    oList.forEach((element) => document.getElementById(element).textContent = "O");
}

function drawOneSymbol(id) {
    document.getElementById(id).textContent = symbol;
    
}



function addMoveInfoAndDraw(id) {
    if (!(xList + oList).includes(Number(id)) && move <= 9) {
        console.log("it is ok")
        emptyIndexies()
        if (symbol === "X") {
            xList.push(Number(id));
            drawOneSymbol(id);
            ifWin();
            symbol = "O"
            console.log("xs:", xList)
            
        } else {
            oList.push(Number(id));
            drawOneSymbol(id);
            ifWin();
            symbol = "X";
            console.log("Os:", oList)
            
        }
        
        // drawSymbols();
       
        console.log(moveType);
       
        return true
    }

    return false
}

function addElement() {
    console.log("click on div");
    console.log(this.id)
    if (addMoveInfoAndDraw(this.id)) {
        move += 1;
        moveType = "computer";
        setTimeout(computerMove,400); //computer move
        };
    
}

  

function clear() {
    xList.splice(0,xList.length)
    oList.length = 0;
    Array.from(document.getElementsByClassName("cell")).forEach((element) => {element.textContent = "";
        element.style.backgroundColor = "rgb(182, 145, 237)";});
    // moveType === "computer"? "user":"computer";
    moveType = "user";
    move = 0;
    symbol = "X";
    document.getElementById("xpaly").textContent = moveType;
    document.getElementById("whowin").textContent = "";

    superPowerStatus = false;
    document.getElementById("level").style.backgroundColor = "gray";
}

function computerMove() {
    console.log(moveType);
    if (moveType === "computer" && move < 9) {
        let i;

        //new move
        if (!superPowerStatus) {
        do {i = getRandomIntInclusive(0,8)}
        while((xList + oList).includes(Number(i)));
        } else  {
            console.log("Super");
            i = 3;

        }
        
        console.log("comp move", i);
        addMoveInfoAndDraw(i);
        move += 1;
        moveType = "user";
    }


    function getRandomIntInclusive(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
    }

}

// functions if arr includes
const isSubset = (array1, array2) =>
  array2.every((element) => array1.includes(element));

// check if win
function ifWin() {
    winCombos.forEach ((item) => {
        if (isSubset(xList, item)) { 
            console.log("Win X player")
            document.getElementById("whowin").textContent = `X  WIN - ${moveType}`;
            move = 10; // to stop game
            showWinDivs(item);
        }
        else if (isSubset(oList, item)) {
            document.getElementById("whowin").textContent = `O  WIN - ${moveType}`;
            move = 10; // to stop game
            showWinDivs(item);
        }
    } )

    if (move===8) {
        document.getElementById("whowin").textContent = `tie game`;
    }
}

function showWinDivs(arr) {
    arr.forEach((id) => {
        document.getElementById(id).style.backgroundColor = "yellow";
        // console.log(document.getElementById(id).style.listStyle);
        // backgroundColor = "red";
    });
}

function firstMove() {
    clear();
    moveType =  moveType === "computer"? "user":"computer";
    // clear();
    document.getElementById("xpaly").textContent = moveType;
    computerMove();

    
}

function superPower() {
 if (!superPowerStatus && move === 0) {
    superPowerStatus = true;
    document.getElementById("level").style.backgroundColor = "green";
 } else if (superPowerStatus && move === 0) {
    superPowerStatus = false;
    document.getElementById("level").style.backgroundColor = "gray";

 } else {
    alert("Clear game to change");
 }
}

function emptySquares() {
    return origBoard.filter(s => typeof s == 'number');
}


function emptyIndexies(){
    let res = [0,1,2,3,4,5,6,7,8].filter(x => !(xList + oList).includes(x));
    console.log(res);
    return  res;
  }


function minimax(newBoard, player) {
    var availSpots = emptyIndexies();

    
    var moves = [];
      // loop through available spots
    for (var i = 0; i < availSpots.length; i++) {
        //create an object for each and store the index of that spot 
        var moveIn = {};
        moveIn.index = newBoard[availSpots[i]];
        newBoard[availSpots[i]] = player;

        if (player == aiPlayer) {
            var result = minimax(newBoard, huPlayer);
            moveIn.score = result.score;
        } else {
            var result = minimax(newBoard, aiPlayer);
            moveIn.score = result.score;
        }

        newBoard[availSpots[i]] = moveIn.index;

        moves.push(moveIn);
    }

    var bestMove;
    if (player === aiPlayer) {
        var bestScore = -10000;
        for (var i = 0; i < moves.length; i++) {
            if (moves[i].score > bestScore) {
                bestScore = moves[i].score;
                bestMove = i;
            }
        }
    } else {
        var bestScore = 10000;
        for (var i = 0; i < moves.length; i++) {
            if (moves[i].score < bestScore) {
                bestScore = moves[i].score;
                bestMove = i;
            }
        }
    }

    return moves[bestMove];
}


//Tests


//Driver
addEventsToDiv();
 