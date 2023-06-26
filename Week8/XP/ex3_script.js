
// 🌟 Exercise 3 : Transform The Sentence
// Instructions
// In the JS file:
// Declare a global variable named allBoldItems.
let allBoldItems;
// Create a function called getBoldItems() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
function getBoldItems() {
    allBoldItems = document.getElementsByTagName("strong");
    console.log(allBoldItems);
}
// Create a function called highlight() that changes the color of all the bold text to blue.
function highlight() {
    for (let element of allBoldItems) {
        element.style.color  = "blue";
    }
}
// Create a function called returnItemsToDefault() that changes the color of all the bold text back to black.
function returnItemsToDefault() {
    for (let element of allBoldItems) {
        element.style.removeProperty('color');
    }
}
// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph),
//  and the function returnItemsToDefault() on mouseout (ie. when the mouse pointer is moved out of 
// the paragraph). Look at this example
getBoldItems();
const elemenForAnimation = document.querySelectorAll("p")[0];

elemenForAnimation.addEventListener("mouseover", highlight);
elemenForAnimation.addEventListener("mouseout", returnItemsToDefault);


// highlight();
// returnItemsToDefault();