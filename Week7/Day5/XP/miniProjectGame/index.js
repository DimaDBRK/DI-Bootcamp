// XP
// Exercise 1 : Play A Guessing Game

// 3. Create a function called playTheGame() that takes no parameter.
// In the function, start by asking the user if they would like to play the game 
// (Hint: use the built-in confirm() function).

// If the answer is false, alert “No problem, Goodbye”.



// You then have to check the validity of the user’s number :
// If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
// If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.

let countOfUserLoose;
function playTheGame() {
    countOfUserLoose = 3;
    const startGame = confirm("Would like to play the game?\nPress a button!\nEither OK or Cancel.");
    // If his answer is true, follow these steps:
    if (startGame) {
        // Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). 
        let gameStatus = true;
        while (gameStatus) {
            const userNumber = userNumberInput();
            if (userNumber) {
            //user number is str to alloow use null
            
            // Else (ie. he entered a number between 0 and 10), create a variable named computerNumber 
            const computerNumber = createComputerNumber();
            gameStatus  = compareNumbers(Number(userNumber), computerNumber)
            console.log(gameStatus)
            console.log(countOfUserLoose)
            }
            else {
                alert('Try Again!');
                gameStatus = false;
            }
        }
    }
    // If the answer is false, alert “No problem, Goodbye”.
    else {
        alert('No problem, Goodbye!')
    }
}

// function Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt()
// You then have to check the validity of the user’s number :
// If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
// If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.

// Bonus
// In the First Part, instead of stopping the process if the user didn’t enter a valid number. Continue asking for a number until the user enters a valid number.

function userNumberInput() {
    let numberFromUser;
    do {
        // Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). 
        numberFromUser = prompt('Input Number between 0 and 10: ');
        if (isNaN(numberFromUser)) { 
            alert("Sorry Not a number");
        } else if (numberFromUser < 0 || numberFromUser > 10) {
            alert("It’s not a good number");
        }
    }
    while ((isNaN(numberFromUser) || numberFromUser < 0 || numberFromUser > 10)  && numberFromUser != null);
    
    return numberFromUser;
}

// create a variable named computerNumber 
// value is a random number between 0 and 10 (Hint: Use the built-in Math.random() function).
// Make sure that the number is rounded.
function createComputerNumber (min = 0, max= 10) {

    min = Math.ceil(min);
    max = Math.floor(max);

    return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
}

// compareNumbers - The point of this function is to check if the userNumber is the same as the computerNumber:
// If userNumber is equal to computerNumber, alert “WINNER” and stop the game.
// If userNumber is bigger than computerNumber, alert “Your number is bigger then the computer’s, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).
// If userNumber is lower than computerNumber, alert “Your number is smaller then the computer’s, guess again” (Hint: use the built-in prompt() function to ask the user for a new number).
// If the user guessed more than 3 times, alert “out of chances” and exit the function.

function compareNumbers(userNumber,computerNumber) {
    if (userNumber === computerNumber) {
        alert(`WINNER. Number ${userNumber}`);
        countOfUserLoose += 1
        } else if (userNumber > computerNumber) {
        alert(`Your number ${userNumber} is bigger then the computer’s ${computerNumber}, guess again`);
        countOfUserLoose -= 1
    } else if (userNumber < computerNumber) {
        alert(`Your number ${userNumber}is smaller then the computer’s ${computerNumber}, guess again`);
        countOfUserLoose -= 1
    }

    if (countOfUserLoose <= 0) {
        alert("Out of chances");
        return false;
    } else {
        return true;
    }

}

// Driver
// playTheGame()

//Tests


// const list = [];
// for (let i = 0; i < 40; i++) {
//     list.push(createComputerNumber());
// }
// console.log(list);

// if (null) {
//     console.log('Ok')
// }