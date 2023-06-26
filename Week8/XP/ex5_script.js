
// Exercise 5 : Event Listeners
// Instructions
// Add many events listeners to one element on your webpage. 
// Use the click, mouseover, mouseout and dblclick events.
// Each listener should do a different thing, for instance - change position x, 
// change position y, change color, change the font size… and more.





const elemenForAnimation = document.querySelectorAll("p")[0];
const elemenForAnimationTwo = document.querySelectorAll("p")[1];
const box1 = document.getElementById("box1");
console.log(elemenForAnimation);

elemenForAnimation.addEventListener("mouseover", highlight);
elemenForAnimationTwo.addEventListener("mouseover", highlightRed);
elemenForAnimation.addEventListener("dblclick", returnItemsToDefault);
elemenForAnimationTwo.addEventListener("dblclick", returnItemsToDefault);
box1.addEventListener("click", moveRight);


function highlight() {
    console.log("mouse on");
    this.style.border  = "2px solid green";
}

function highlightRed() {
    console.log("mouse on");
    this.style.border  = "2px solid red";
}


function returnItemsToDefault() {
    this.style.removeProperty('border');
}

function moveRight() {
    console.log("move ->");
    let rect = this.getBoundingClientRect();
    let x= rect.x;
    let y= rect.y;
    // get the postion related to the webpage
    // x = x + ;
    // y = y + window.scrollY;
    console.log(x);
    this.style.position = "absolute";
    this.style.left = `${x+30}px`;
    
    console.log(y);
    
}
