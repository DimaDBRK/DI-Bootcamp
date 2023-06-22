// Daily Challenge: 99 Bottles Of Beer


// Global vars & consts
const startText = 'We start the song at 99 bottles';
const endText = 'no bottle of beer on the wall.';

// functions
function verseOfSong(onTheWallBottels, takeDown = 1) {
    const res1 = `${onTheWallBottels} ${(onTheWallBottels > 1) ? 'bottels' : 'bottel'} of beer on the wall`;
    showOnPage(res1, "p");


    const res2 = `${onTheWallBottels} ${(onTheWallBottels > 1) ? 'bottels' : 'bottel'} bottles of beer`;
    showOnPage(res2, "p");

    const res3 = `Take ${takeDown} down, pass ${(takeDown > 1) ? 'them' : 'it'} around\n`
    showOnPage(res3, "p");

    let res4 = "";
    
    if (onTheWallBottels-takeDown != 0) {
        res4 = `${onTheWallBottels-takeDown} ${((onTheWallBottels-takeDown) > 1) ? 'bottels' : 'bottel'} of beer on the wall`;
        
    } else {
        res4 = `no bottle of beer on the wall`;
        
    }

    showOnPage(res4, "p");

    showOnPage("-----------", "p");

   
}

function userNumberInput() {
    let numberFromUser;
    do {
        // Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). 
        numberFromUser = prompt('Input Number between 1 and 99: ');
        if (isNaN(numberFromUser)) { 
            alert("Sorry Not a number");
        } else if (numberFromUser < 0 || numberFromUser > 99) {
            alert("It’s not a good number");
        }
    }
    while ((isNaN(numberFromUser) || numberFromUser < 0 || numberFromUser > 99)  && numberFromUser != null);
    
    return numberFromUser;
}

function showOnPage(content, type){
    const container = document.getElementById("boxForText");
    const newElement = document.createElement(type);
    const text = document.createTextNode(content);
    newElement.appendChild(text);
    container.appendChild(newElement);

}

function showTheSong() {
    clearSection()
    let takeDown = 1;
    let startBottels = userNumberInput();
    if (startBottels) {
      
        // console.log(verseOfSong(99,takeDown));
        showOnPage(('We have ' + startBottels + '   and will take ' + takeDown), "h2");
        startBottels = Number(startBottels);
        // console.log(typeof(takeDown));
        for (let i = startBottels; i > 0; (i-=takeDown)) {
            if ((i-takeDown) < 0) {
                takeDown = i;
            }

            verseOfSong(i,takeDown);
        }
    } else {
        alert("You can try Again!")
    }
}

function clearSection() {
    const collection = document.getElementById('boxForText').querySelectorAll("*");

    for (let i = 0; i < collection.length; i++) {
        const elem = collection[i];
        elem.remove();
    }
}
//Driver

//Tests
// console.log(verseOfSong(2))
// showTheSong()
