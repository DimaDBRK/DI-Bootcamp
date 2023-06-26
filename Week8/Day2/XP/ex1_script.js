// XP
// 🌟 Exercise 1 : Scope
// Instructions

// Analyse the code below, and predict what will be the value of a in all the following functions.
// Write your prediction as comments in a js file. Explain your predictions.
// #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// -> a = 3, OK
// #1.1 - run in the console:
// funcOne()
// #1.2 What will happen if the variable is declared 
// with const instead of let ? 
// -> Will be error

//#2
// let a = 0;
function funcTwo() {
    a = 5;
}
// -> a = 5
function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1 - run in the console:
// funcThree() // -> a=0
// funcTwo() // -> a= 5
// funcThree() // -> a= 5
// #2.2 What will happen if the variable is declared 
// with const instead of let ?
// -> Error on funcTwo, only 0 will be alerted


//#3
function funcFour() {
    window.a = "hello";
    console.log(window.a);
    console.log(a);
}

// In the global context, using var vs assigning to window are indeed quite similar. 
// However, yes there are a number of differences. 
// Here are a few I can think of:
// - var declarations are hoisted, which means that you can use a variable declared with var before you've declared it. On the other hand, trying to use something assigned to window before that assignment has occurred will produce a ReferenceError:
// - Variables declared with var cannot be removed from the global object, but simple assignments to window can be removed:

//-> a =  "hello" should still exists here, in case if there are not global var a uin code
function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console:
// funcFour()
// funcFive()

//#4
// const a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }
//-> a =  "test" in alert

// #4.1 - run in the console:
// funcSix()
// #4.2 What will happen if the variable is declared 
// with const instead of let ?
//-> it is OK,  a= test in alert

//#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console 
// -> in =5, out = 1
// #5.2 What will happen if the variable is declared 
// with const instead of let ?

// -> the same, function don't chnge global var (or const)


// 🌟 Exercise 2 : Ternary Operator
// Instructions
// Using the code below:

// function winBattle(){
//     return true;
// }

// Transform the winBattle() function to an arrow function.
// Create a variable called experiencePoints.
// Assign to this variable, a ternary operator. If winBattle() is true, 
// the experiencePoints variable should be equal to 10, 
// else the variable should be equal to 1.
// Console.log the experiencePoints variable.

const winBattle = () => true;
let experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints);
console.log(winBattle());

// 🌟 Exercise 3 : Is It A String ?
// Instructions
// Write a JavaScript arrow function that checks whether the value of the argument passed, 
//  is a string or not. The function should return true or false
// Check out the example below to see the expected output
// Example:
// console.log(isString('hello')); 
// //true
// console.log(isString([1, 2, 4, 0]));
// //false
console.log('is String');
const isString = (input) => typeof(input) == 'string' ? true : false;
console.log(isString('hello')); 
console.log(isString([1, 2, 4, 0])); 

// 🌟 Exercise 4 : Find The Sum
// Instructions
// Create a one line function (ie. an arrow function) that receives two 
// numbers as parameters and returns the sum.

const add = (a,b) => a + b;
console.log(add(2,3));

// 🌟 Exercise 5 : Kg And Grams
// Instructions
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)

// First, use function declaration and invoke it.
function switchKg(kg) {
    return kg * 1000;
}
console.log(switchKg(1));
// Then, use function expression and invoke it.
const switchKgExpression = function(kg) { 
    return kg * 1000;
}
console.log(switchKgExpression(1)); 

// Write in a one line comment, the difference between function declaration and function expression.
// The main difference between a function expression and a function declaration is the function name, which can be omitted in function expressions to create anonymous functions. A function expression can be used as an IIFE (Immediately Invoked Function Expression) which runs as soon as it is defined.

// Finally, use a one line arrow function and invoke it.
const switchKgarrow = kg => kg*1000;
console.log(switchKgarrow(1));

// 🌟 Exercise 6 : Fortune Teller
// Instructions
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, 
// geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic 
// location>, and married to <partner's name> with <number of children> kids."
((numberOfChildren,partnersName, geographicLocation, jobTitle) => {
        const divElement = document.getElementById("conatainer");
        divElement.textContent = `You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnersName}  with ${numberOfChildren} kids.`;
    })(2,"Olga","California", "SW Developer")


// 🌟 Exercise 7 : Welcome
// Instructions
// John has just signed in to your website and you want to welcome him.

// Create a Navbar in your HTML file.
// In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
// The function should add a div in the nabvar, displaying the name of the user and his profile picture.

const LogUserName = "John";
let loginStatus = true;
const picturesURL = {
    "John":"test.jpg",
    "Albert":"https://imageio.forbes.com/specials-images/imageserve/5faad4255239c9448d6c7bcd/Best-Animal-Photos-Contest--Close-Up-Of-baby-monkey/960x0.jpg"
};

((userName) => {
    const nameElement = document.getElementById("username");
    nameElement.textContent = `Hello ${userName}`;
    const imgElement = document.getElementById("box");
    const newImg = document.createElement("img");
    // add link
    newImg.setAttribute("src", picturesURL[userName])
    imgElement.prepend(newImg);
    console.log(picturesURL[userName])

})("Albert")


// 🌟 Exercise 8 : Juice Bar
// Instructions
// You will use nested functions, to open a new juice bar.

// Part I:
// The outer function named makeJuice receives 1 argument: the size of the beverage the client 
// wants - small, medium or large.

// The inner function named addIngredients receives 3 ingredients, and displays on the DOM a 
// sentence like The client wants a <size drink> juice, containing <first ingredient>, <second 
// ingredient>, <third ingredient>".

// Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the 
// global scope.

// Part II:
// In the makeJuice function, create an empty array named ingredients.

// The addIngredients function should now receive 3 ingredients, and push them into the ingredients
//  array.

// Create a new inner function named displayJuice that displays on the DOM a sentence like The
//  client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third 
// ingredient>".

// The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE.
//  Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.

function makeJuice(size) {
    const ingredients = [];


    function addIngredients(firstIngredient, secondIngredient, thirdIngredient) {
        ingredients.push(firstIngredient, secondIngredient, thirdIngredient);
        console.log(ingredients)

    }

    function displayJuice() {
        let text = `Client wants a ${size} juice, containing: `;
        
        for (let item of ingredients) {
            text += (item == ingredients[ingredients.length - 1])? item + '.' : item + ', ';
            
            }
        const nameElement = document.getElementById("orderList");
        nameElement.textContent = text;
    }
//test
   
    addIngredients("apple", "banana", "orange")
    addIngredients("kiwi", "lemon", "meant")
    displayJuice();

}

//test
makeJuice("big");
