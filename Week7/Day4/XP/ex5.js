// Week7 Day4
// Dmitry Dubrov
// Ex 5
// Exercise 5 : Users
// Instructions
// Create a new structured HTML file and a new Javascript file

// Using Javascript:
// Retrieve the div and console.log it
const myDiv = document.getElementById("container");
console.log(myDiv)

// Change the name “Pete” to “Richard”.
document.body.children[1].lastElementChild.textContent = 'Richard';

// Delete the <li> that contains the text node “Sarah”. (It’s the second <li> of the second <ul>)
let aTags = document.getElementsByTagName("li");
let searchText = "Sarah";

for (let i = 0; i < aTags.length; i++) {
    if (aTags[i].textContent == searchText) {
      aTags[i].remove();
      break;
    }
  }

// Change each first name of the two <ul>'s to your name. (Hint : use a loop)
let listTags = document.getElementsByTagName("li");
let newText = "Dima";

// for (let item of listTags) {
//     item.textContent = newText;
//     }


// Using Javascript:
// Add a class called student_list to both of the <ul>'s.
const ulTags = document.getElementsByTagName("ul");

for (let item of ulTags) {
    item.classList.add("student_list");
    }

// Add the classes university and attendance to the first <ul>.
const targetUl = document.body.children[1];
targetUl.classList.add("university", "attendance");


// Using Javascript:
// Add a “light blue” background color and some padding to the <div>.
myDiv.style.backgroundColor = "lightblue";
myDiv.style.padding = "150px 50px 50px 30px";

// Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>
for (let item of listTags) {
    if (item.textContent == 'Dan') {
        item.textContent += ' --- to Hide'
        item.style.display = "none";
        break;
      }
   
    }

// Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
for (let item of listTags) {
    if (item.textContent == 'Richard') {
        item.textContent += ' --- to add Border'
        item.style.border = "1px solid red";
        break;
      }
   
    }
// Change the font size of the whole body.
document.body.style.fontSize = "x-large";
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
if (myDiv.style.backgroundColor === 'lightblue') {
    const x = [];
    for (let item of document.body.children[1].getElementsByTagName("li")) {
       console.log(item.textContent);
       x.push(item.textContent)
    }

    textAlert = `Hello ${x[0]} and ${x[1]}!`
    alert(textAlert);
} 