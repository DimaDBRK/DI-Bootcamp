// Daily Challenge: Play With Words
// Instructions
// 1rst Daily Challenge
// Create two functions. Each function should return a promise.
// The first function called makeAllCaps(), takes an array of words as an argument
// If all the words in the array are strings, resolve the promise. The value of the resolved promise is the array of words uppercased.
// else, reject the promise with a reason.
// The second function called sortWords(), takes an array of words uppercased as an argument
// If the array length is bigger than 4, resolve the promise. The value of the resolved promise is the array of words sorted in alphabetical order.
// else, reject the promise with a reason.
// Test:

function makeAllCaps(arr) {
    const checkAllIsString = new Promise ((resolve, reject) => {
        const isString = element => typeof(element) === "string";
        if (arr.every(isString)) {
                
                resolve(arr.map((element) => element.toUpperCase()));
                                
        } else {
                reject("Not all the words in the array are strings.");
            }
        })
        return checkAllIsString
}


// console.log(makeAllCaps(["ds","dsaFS", 1]));

function sortWords(arr) {
    const checkAllIsString = new Promise ((resolve, reject) => {
        if (arr.length > 4) {
            arr.sort()
            resolve(arr);                  
        } else {
            reject("Length is less 4.");
        }
    }
    )
    return checkAllIsString
}

// sortWords(["ds","dsaFS"])
//     .then((result2) => {
//         console.log(result2)})
//     .catch((error2) => {
//         console.log("ERROR:", error2);
//     })


makeAllCaps(["ds","dsaFS", "dsad", "dASFD", "DASFD"])
    .then((result) => {
        console.log(result); 
        return sortWords(result);
    })
    .then((result2) => {
        console.log(result2)})
    .catch((error2) => {
        console.log("ERROR:", error2);
    })


    // 2nd Daily Challenge
let text = "";
const morse = `{
      "0": "-----",
      "1": ".----",
      "2": "..---",
      "3": "...--",
      "4": "....-",
      "5": ".....",
      "6": "-....",
      "7": "--...",
      "8": "---..",
      "9": "----.",
      "a": ".-",
      "b": "-...",
      "c": "-.-.",
      "d": "-..",
      "e": ".",
      "f": "..-.",
      "g": "--.",
      "h": "....",
      "i": "..",
      "j": ".---",
      "k": "-.-",
      "l": ".-..",
      "m": "--",
      "n": "-.",
      "o": "---",
      "p": ".--.",
      "q": "--.-",
      "r": ".-.",
      "s": "...",
      "t": "-",
      "u": "..-",
      "v": "...-",
      "w": ".--",
      "x": "-..-",
      "y": "-.--",
      "z": "--..",
      ".": ".-.-.-",
      ",": "--..--",
      "?": "..--..",
      "!": "-.-.--",
      "-": "-....-",
      "/": "-..-.",
      "@": ".--.-.",
      "(": "-.--.",
      ")": "-.--.-",
      " ": " "
    }`
    // added symbol " "
    
function toJs(jsonString) {
    const convertToJSObject = new Promise ((resolve, reject) => {
        newObject = JSON.parse(jsonString);
        let check = Object.keys(newObject).length > 0;
        
        if (check) {
            resolve(newObject);                  
        } else {
            reject("Length of string is 0.");
        }
    }
    )
    return convertToJSObject
}

const test1 = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-"}`;

const test2 = `{}`;
const test3 = `{"1"}`;

// toJs(test2)
//     .then((result) => {
//         console.log(typeof(result)); 
//     })
//     .catch((error2) => {
//         console.log("ERROR HERE:", error2);
//     })

function  toMorse(morseJS) {
    //convert JSON morse to Object JS
    const morseObject = morseJS; // additional const for manual tests
    //get input word -> change to function
    text = document.forms[0].elements[0].value;
    // delet extra spces -  pattern to search = /.../ denotes a regular expression, \s+ one or more whitespace, g - all occurrences of the pattern should be replaced, not just the first one.
    text = text.replace(/\s+/g,' ').trim();
    //convert to array of words ???

    //function to check if letter exist in keys -> true or false
    function checkLetter(letter) {
        return Object.keys(morseObject).includes(letter);
    }

    function checkWrongSymbols(arr) {
        let str = "";
        arr.forEach((letter) => {
            if (!checkLetter(letter)) {str += letter + " "}
        });
        return str
    }

    //convert word to a list of symbols
    let lettersArr = [...text.toLowerCase()]
    //check if all letters in arr is OK for morse code
    let check = lettersArr.every(checkLetter)
    //start 
    const convertToMorse = new Promise((resolve, reject) => {
        if (check) {
            const morseArr = lettersArr.map((element) => morseObject[element]);
            resolve(morseArr);                  
        } else {
            //add check for length
            reject(`The character${checkWrongSymbols(lettersArr).length>1? "s": ""} " ${checkWrongSymbols(lettersArr)}" doesn't exist in the morse.`);
        }
    })
    return convertToMorse
}

// toMorse()
// .then((result2) => {
//     console.log(result2)})
// .catch((error2) => {
//     console.log("ERROR:", error2);
// })

document.getElementById("convert").addEventListener('click', start);


function start(event) {
    console.log("Start")
    event.preventDefault();
    // const myForm =  document.forms[0].elements[0]
    
    function clear() {
        console.log("clear")
            const pToRemove = document.getElementsByClassName("code-style");
            Array.from(pToRemove).forEach((element) => element.remove());
            showText("")
    }

    function showText(text) {
        const pToShowText = document.getElementById("texttocode");
        pToShowText.textContent = text;
    }

    function showCode(arr) {
        const container = document.getElementById("container");
        console.log(container)
        arr.forEach((item, index) =>  {
            const newCodeElement = document.createElement("p");
            newCodeElement.textContent = `${index + 1}) ${item}`;
            newCodeElement.setAttribute("id", index);
            newCodeElement.setAttribute("class", "code-style");
            container.appendChild(newCodeElement);
          
        })
    }

    clear()

    toJs(morse)
        .then((result) => {
        console.log(result);
        console.log("converted JSON to JSObject morse code!");
        return toMorse(result);
        })
        .then((result2) => {
        console.log(result2);
        console.log("converted JSON to JSObject morse code!");
        showCode(result2);
        showText(text);
        })
        .catch((error) => {
        console.log("ERROR :", error);
        // function to show error
        showText(error);
        })
}