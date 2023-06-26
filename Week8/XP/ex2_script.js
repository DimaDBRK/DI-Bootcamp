
// 🌟 Exercise 2 : Work With Forms
// Instructions

// Retrieve the form and console.log it.
const myform = document.forms[0];
console.log(myform);
// Retrieve the inputs by their id and console.log them.
const firstNmae = myform.fname;
const lastNmae = myform.fname;
console.log(firstNmae);
console.log(lastNmae);

// Retrieve the inputs by their name attribute and console.log them.
const firstNmaebyName = myform.fname;
const lastNmaebyName = myform.fname;
console.log(firstNmaebyName);
console.log(lastNmaebyName);

// When the user submits the form (ie. submit event listener)

myform.addEventListener('submit', getValuesForm);

function getValuesForm(event) {
// - use event.preventDefault(), why ?
    event.preventDefault(); //stop the form refresh 
    console.log("Submit");
// - get the values of the input tags,
    const inputValues = [event.target.fname.value, event.target.lname.value];
    // const inputLname = event.target.lname.value;
    console.log(inputValues[0]);
    console.log(inputValues[1]);   
    console.log(event.target.lname); 
// - make sure that they are not empty,
    let checkRes = true;
    for (let item of inputValues) {
        checkRes = (item.length > 0);
    }

    if (checkRes) {
// - create an li per input value,
        for (let item of inputValues) {        
        // - then append them to a the <ul class="usersAnswer"></ul>, below the form.
            console.log("Ok")
            const container = document.getElementsByClassName("usersAnswer")[0];
            const newElement = document.createElement("li");
            const text = document.createTextNode(item);
            newElement.appendChild(text);
            container.appendChild(newElement);
        }

    }


}
// -The output should be :
// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>