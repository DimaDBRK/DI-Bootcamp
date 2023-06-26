// Daily Challenge: Tell The Story
// Instructions
// In todays exercise we will be creating a Mad Libs game.
// If you’ve never played this game, a mad lib is a game where you fill in a bunch of 
// blank inputs with different word types (ie : noun, adjective, verb), and then a story is 
// generated based on the words you chose, and sometimes the story is surprisingly funny.

// In this exercise you work with the HTML code presented below.

// Follow these steps :

// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the 
// event.preventDefault()
// Make sure the values are not empty
const myform = document.forms[0];
myform.addEventListener('submit', getValuesForm);

let elementObject;

//Mix button
const buttonMix = document.getElementById("shuffle");
buttonMix.addEventListener("click", showMixStory);

function getValuesForm(event) {
    // - use event.preventDefault(), why ?
        event.preventDefault(); //stop the form refresh 
        console.log("Submit");
    // - get the values of the input tags,
        const inputValues = {'noun': event.target.noun.value, 
                            'adjective':  event.target.adjective.value,
                            'person':  event.target.person.value,
                            'verb':  event.target.verb.value,
                            'place':  event.target.place.value,
                            };
        // const inputLname = event.target.lname.value;
        console.log(inputValues);
        
    // - make sure that they are not empty,
        let checkRes = true;
        let tempKey;
        for (const [key, value] of Object.entries(inputValues)) {
            
            tempKey = key;
            checkRes = (value != '');
            if (!checkRes) {
                alert(`Please, fill form: ${tempKey}`);
                break;
            }
            console.log(key, value, checkRes);
        }

        if (checkRes) {
            console.log("Value OK");
            elementObject = inputValues
            showStory(elementObject);
        }

  
    
    
    }
constcarr = [];
let counter = 4;
let arr = [];

function  showStory(object) {
    arr = []; 
    //clear function
    clear();
    const {noun,adjective,person,verb,place} = object;
    let story = noun + ' ' + adjective + ' ' + person + ' ' + verb + ' ' + place + '.';
    // const container = document.getElementById("story");
    const newElement = document.getElementById("story");
    const text = document.createTextNode(story);
    newElement.appendChild(text);
    console.log("before arr");
    counter = 0;
    console.log(counter);
    // arr = [noun,adjective,person,verb,place]; //-> ERROR
    
    for (const [key, value] of Object.entries(object)) {
        arr.push(value);
    }
    console.log(arr);
   
    console.log(counter);
    // container.appendChild(newElement);
}

function mixWords() {
    const mixList = [];
    const iList =[];
    while (mixList.length < arr.length) {
        let i = getRandomInt(0,arr.length);
        
        console.log(i, arr[i], !iList.includes(i));
        console.log(mixList);

        if (!iList.includes(i)) {
            mixList.push(arr[i]);
            iList.push(i);
        }
        
    }
    console.log(mixList);
    let res = '';
    for (let items of mixList) {
        if (items != mixList[mixList.length - 1]) {
            res += items + " ";}
        else {
            res += items + ".";
        }
        

    }
    return res
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min); // The maximum is exclusive and the minimum is inclusive
  }

function  showMixStory() {
    console.log(counter);
    if (counter < 3) {
        counter += 1;
        //add new h3 with id1
        //add new span with id
        const container = document.getElementsByTagName("p")[0];
        const newHeader = document.createElement("h3");
        const headerText = document.createTextNode(`Mixed story # ${counter} :`);
        newHeader.appendChild(headerText);
        container.appendChild(newHeader);
        
        const stortText = mixWords();

        
        const newSpan = document.createElement("span");
        const newText = document.createTextNode(stortText);
        newSpan.appendChild(newText);
        container.appendChild(newSpan);
    }
    else {
        alert("No attempt. Clear");
        //function clear text and form
    }
  }

function clear() {
    const h3Elements = document.getElementsByTagName("h3");
    for (let item of h3Elements) {
        item.remove();
    }
}
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story
//  currently displayed (but keep the values entered by the user). 
// ssThe user could click the button at least three times and get a new story. 
// Display the stories randomly.

