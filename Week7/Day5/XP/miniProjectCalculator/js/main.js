
// global vars & consts
const numbersList = [];
const operatorList = [];
let tempNumberString = '';
let dispalyText = "";
const symbolsOnDisplay = 32;
var typeOfInput = "number"; //or operator
// functions
let result = '';

function number(n) {


// if only 0, if . check if it is exist
    if ((tempNumberString != "0") || (tempNumberString == "0" && n != 0)) {
        if ((!tempNumberString.includes('.')  && tempNumberString.length != 0 && n === '.' && tempNumberString !='-') || n != '.') {
            tempNumberString += n;
            dispalyText += n;
            typeOfInput = "operator";
            console.log(tempNumberString)

            // show dispalyText'
            console.log(dispalyText);
            clearInfo("output-line-1");
            showInfo(dispalyText, "output-line-1");
           
        }
    }
}

function operator(operatorType) {
    console.log(typeOfInput);
    if (typeOfInput === "operator" && tempNumberString.length > 0) {
        operatorList.push(operatorType);
        console.log(operatorList);
        typeOfInput = "number";
        numbersList.push(tempNumberString);
        console.log(numbersList);
        tempNumberString = '';
        dispalyText += operatorType;
        clearInfo("output-line-1");
        showInfo(dispalyText, "output-line-1");

    }

    else if (operatorType == "-" && tempNumberString.length == 0) { //typeOfInput === "number" &&
        console.log(typeOfInput);
        number("-");
        typeOfInput = "number";
    }

}

  


function equal() {




// calculate = result


// check temp number - if operator - ignore, if number  add to number
    if (tempNumberString != '-' && tempNumberString != '') {
        console.log(!isNaN(tempNumberString));
        numbersList.push(tempNumberString);
        console.log(numbersList);
        tempNumberString = '';
    }

    if (numbersList.length > 1 && operatorList.length  != 0 && result == '') {
    //chek if there is now additional operator
        if (numbersList.length <= operatorList.length) {
            operatorList.pop();  
            console.log(numbersList);
            console.log(operatorList);
        }
             
        console.log("start calculate");
        const tempNumberList = [];
        const tempOperatorList = [];
        let tempRes = 0;
        // check if it is 0
      
            if (operatorList.length <= 1) {
                let i = 0;
                console.log("One operation");
                console.log(operatorList.length);
                if (operatorList[i] == '*') {
                    tempRes = Number(numbersList[i]) * Number(numbersList[i+1]);
                } else if (operatorList[i] == '/') {
                    if (numbersList[i+1] != 0) {
                        tempRes =  Number(numbersList[i]) /  Number(numbersList[i+1]);
                    }
                    else {
                        showInfo("No div by 0", "output-line-2");
                        
                    }

                } else if (operatorList[i] == '+') {
                    tempRes =  Number(numbersList[i]) +  Number(numbersList[i+1]);
                } else if (operatorList[i] == '-') {
                    tempRes =  Number(numbersList[i]) -  Number(numbersList[i+1]);
                } 
                
                tempNumberList.push(tempRes);
                console.log(tempRes);
                tempRes = '';


            } 
            // if more than 1 operator use loop
            else {
                for (let i = 0; i < (operatorList.length-1); i++) {
                    if (['*','/'].includes(operatorList[i])) {
                        console.log("current is",'*','/');
                        if (['*','/'].includes(operatorList[i + 1])) {
                            console.log("next is ",'*','/');
                            if (tempRes == '') {tempRes = Number(numbersList[i])};
                            console.log(i, "tempRes");
                            console.log(tempRes);
                            if (operatorList[i] == '*') {
                                tempRes = tempRes * Number(numbersList[i+1]);
                            } else if (operatorList[i] == '/') {
                                if (numbersList[i+1] != 0) {
                                    tempRes =  tempRes /  Number(numbersList[i+1]);
                                    }
                                else {
                                    showInfo("No div by 0", "output-line-2");
                                    break;
                                    }
                            }
                            // check if there is only last operator
                            console.log(i);
                            let lastOperatorIndex = operatorList.length -1;
                            if (i == (lastOperatorIndex-1))   {
                                console.log(operatorList[operatorList.length -1]);
                                if (operatorList[lastOperatorIndex] == '*') {
                                    tempRes = tempRes * Number(numbersList[lastOperatorIndex+1]);
                                } else if (operatorList[lastOperatorIndex] == '/') {
                                    if (numbersList[lastOperatorIndex+1] != 0) {
                                        tempRes =  tempRes /  Number(numbersList[lastOperatorIndex+1]);
                                        }
                                    else {
                                        showInfo("No div by 0", "output-line-2");
                                        break;
                                        }
                                }

                            console.log("result:", tempRes);


                            }       
                            
                        
                           
                        
                        }
                        
                    // if next + or - -> add result to temp list and add operator to temp list and temp = '';
                        else {
                            if (operatorList[i] == '*') {
                                tempRes = Number(numbersList[i]) * Number(numbersList[i+1]);
                            } else if (operatorList[i] == '/') {
                                if (numbersList[i+1] != 0) {
                                    tempRes =  Number(numbersList[i]) /  Number(numbersList[i+1]);
                                    }
                                else {
                                    showInfo("No div by 0", "output-line-2");
                                    break;
                                    }
                            }
                        }
            
                    }
                    }
                }         

            }
    }


function clearAll() {
    console.log("Clear");
    if (dispalyText.length != 0) {
        console.log("Str not empty OK, Clear");
        console.log(dispalyText);
        const lastSymbol = dispalyText.charAt(dispalyText.length - 1);
        console.log(dispalyText);
        console.log("Last symbol", lastSymbol, ['+','-','*','/'].includes(lastSymbol), dispalyText.length);
        
        if (['+','-','*','/'].includes(lastSymbol) && dispalyText.length != 1 && tempNumberString.length != 1) { // check for case -1 at start of string
            console.log("Last symbol -  Operator");
            // delete last element from operators array
            operatorList.pop()
            typeOfInput = "number";
           
        } 
        else {
            console.log("Last symbol -  Number or - in Temp Number");
            // check if tempNumber is not empty -> yes, clear last symbol in empty number, else correct last didgit in array
            if (tempNumberString.length > 0) {
                tempNumberString = tempNumberString.slice(0, -1);
                console.log("Last symbol delet", tempNumberString);

            }

            else {

                // take last element from number array and delet one symbol, if it is only 1 - delete last element
                console.log("Last symbol -  Number");
                let lastElementInNumberArray = numbersList[numbersList.length - 1]
                console.log("Last Number", lastElementInNumberArray);
                if (lastElementInNumberArray.length != 1) {
                    const NewNumber = lastElementInNumberArray.slice(0, -1);
                    numbersList[numbersList.length - 1] = NewNumber;
                }
                else {
                    numbersList.pop();
                }
            }
        
        }

         // delete last symbol from dispalyText
        dispalyText = dispalyText.slice(0, -1);
        clearInfo("output-line-1");
        showInfo(dispalyText, "output-line-1");
        clearInfo("output-line-2");
        result = '';
        
        

        console.log(numbersList);
        console.log(operatorList);
    }
}

function reset() {
    numbersList.length = 0;
    operatorList.length = 0;
    tempNumberString = '';
    dispalyText = "";
    result = '';

    clearInfo("output-line-1");
    clearInfo("output-line-2");
}

function showInfo(content, line) {
    const textToShow = checkInfoLen(content);
    const container = document.getElementById(line);
    const text = document.createTextNode(textToShow);
    container.appendChild(text);
}

function clearInfo(id) {
    const elementToCleanText = document.getElementById(id);
    elementToCleanText.innerHTML = '';
   

}

function checkInfoLen(text) {
    
    const res = text.length < symbolsOnDisplay ? text : text.substring(text.length - symbolsOnDisplay);
    return res
}

// Old




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