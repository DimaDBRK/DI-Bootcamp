    // 2nd Daily Challenge
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
      let text = "   Hello friends!"
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
    event.preventDefault();
    console.log("Start")
  
    toJs(morse)
          .then((result) => {
          console.log(result);
          console.log("converted JSON to JSObject morse code!");
          return toMorse(result);
          })
          .then((result2) => {
          console.log(result2);
          console.log("converted JSON to JSObject morse code!");
          //function to show result
          })
          .catch((error) => {
          console.log("ERROR :", error);
          // function to show error
          })
  }

start()