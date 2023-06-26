// 🌟 Exercise 1: Timer
// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.

function welcom() {
    setTimeout(function() { alert("hello");} , 2000);
}

// Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.

function welcomParagraph() {
    const container = document.getElementById("container");
    const newElement = document.createElement("p");
    const text = document.createTextNode("Hello World!");
    newElement.appendChild(text);
    
    setTimeout(function() { 
        container.appendChild(newElement);
        }, 3000);
}


// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

function addParagraph() {
    const container = document.getElementById("container");
    const newElement = document.createElement("p");
    const text = document.createTextNode("Hello World!");
    newElement.appendChild(text);
    container.appendChild(newElement);
}




function autoAdd() {
    const stopButton = document.getElementById("clear");
    stopButton.addEventListener("click", function () {clearInterval(myInterval); 
    console.log("Clear button pressed");});
    let counter = 5;
    
    let myInterval = setInterval(function () {
        if (counter <= 0) {
            clearInterval(myInterval); // finish the animation after 2 seconds
            return;
        } else {

            addParagraph();
            counter -= 1;
        }
        }, 2000);
    
     
}

// Driver
welcom();
welcomParagraph();
autoAdd(); 