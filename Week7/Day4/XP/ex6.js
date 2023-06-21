// Exercise 6 : Change The Navbar
// Instructions
// Create a new structured HTML file and a new Javascript file
// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, 
// using the setAttribute method.
const myDiv = document.body.firstElementChild;
myDiv.setAttribute("id","socialNetworkNavigation");
// check by style to new ID

// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
const listElement = document.createElement('li');
    //  but we need to make a for link.
    const aElement = document.createElement('a');
    aElement.setAttribute("href","#");
// Create a new text node with “Logout” as its specified text.
const content = document.createTextNode('Logout');

// Append the text node to the newly created list node (<li>).
//  at first add to a - link text.
aElement.appendChild(content);
listElement.appendChild(aElement);

// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.
const navigationElement = myDiv.firstElementChild;
navigationElement.appendChild(listElement)

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their 
// parent element (<ul>). 
const fitstListElem = myDiv.firstElementChild.firstElementChild;
const lastListElem = myDiv.firstElementChild.lastElementChild;

// Display the text of each link. (Hint: use the textContent property).
console.log(fitstListElem.textContent);
console.log(lastListElem.textContent);