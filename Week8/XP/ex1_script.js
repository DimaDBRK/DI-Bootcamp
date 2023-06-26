// 🌟 Exercise 1 : Change The Article
// Instructions

// Using a DOM property, retrieve the h1 and console.log it.

const elementH1 = document.querySelector("h1");
console.log(elementH1);
console.log(elementH1.textContent);

// Using DOM methods, remove the last paragraph in the <article> tag.
const container = document.querySelector("article");
const toRemove = container.lastElementChild.remove();

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
const elementH2 = document.querySelector("h2");

elementH2.addEventListener("click", changeBackground);

function changeBackground() {
    console.log("change background");
    elementH2.classList.toggle("toRed");
}

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
const elementH3 = document.querySelector("h3");

elementH3.addEventListener("click", hideMe);

function hideMe() {
    console.log("Hide H3");
    elementH3.style.cssText  = "display: none";
}
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
const toAddButton = document.body;
    
const newElement = document.createElement("button");
const text = document.createTextNode("Change to Bold");
newElement.appendChild(text);
newElement.setAttribute("value","Bold");
newElement.setAttribute("id",`btn_bold`);
newElement.addEventListener("click", changeTextStyle);
toAddButton.appendChild(newElement);

function changeTextStyle() {
    const allPsElements = document.querySelectorAll("p");
    for (element of allPsElements) {
        element.style.cssText  = "font-weight: bold";
    }
}
// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

elementH1.addEventListener("mouseover", changeFontSizeRandom);

function changeFontSizeRandom() {
    console.log("Hover H1 - OK");
    function getRandomIntInclusive(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
    }
    const NewTextSize = getRandomIntInclusive(1,100);
    console.log(`font-size: ${NewTextSize}`);
    // elementH1.style.cssText = `font-size: ${NewTextSize}px`; -> // Option 2
    elementH1.style.setProperty('--h1-tx-size', `${NewTextSize}px`);

}


// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
const elemenForAnimation = document.querySelectorAll("p")[1];

elemenForAnimation.addEventListener("mouseover", addAnimation);

function addAnimation() {
    console.log("Mouse over for Animation - OK");
    elemenForAnimation.classList.toggle("animation");

}


