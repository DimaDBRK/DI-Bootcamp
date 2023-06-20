// Dmitry Dubrov
// Exercises XP Gold

// Exercise 1 : Divisible By Three
// Instructions
let numbers = [123, 8409, 100053, 333333333, 7]
// Loop through the array above and determine whether or not each number is divisible by three.
// Each time you loop console.log true or false.

for (let item of numbers) {
        console.log(item, item % 3 == 0);

    }

    // Exercise 2 : Attendance
    // Instructions
    let guestList = {
      randy: "Germany",
      karla: "France",
      wendy: "Japan",
      norman: "England",
      sam: "Argentina"
    }
    
    
    // Given the object above where the key is the student’s name and the value is the country they are from.
    
    // Prompt the student for their name.
    
    // If the name is in the object, console.log the name of the student and the country they come from.
    // For example: "Hi! I'm [name], and I'm from [country]."
    // Hint: You don’t need to use a for loop, just look up the statement if ... in
    
    // If the name is not in the object, console.log: "Hi! I'm a guest."


// let studentName;
// studentName = prompt("Please enter your name"); 

function checkName(studentName) {
    let studentNameClean = studentName.toLowerCase().trim();
    let res = 'Hi! I\'m a guest.';
    if (studentNameClean in guestList) {
        res = `Hi! I'm ${studentName}, and I'm from ${guestList[studentNameClean]}. `
    }
    return res
}

console.log(checkName('Albert'));
console.log(checkName('Karla'));

// Exercise 3 : Playing With Numbers
// Instructions
let age = [20,5,12,43,98,55];
// Requirements : Don’t use built-in Javascript methods to answer the following questions. You have to create the logic by yourself. Use simple for loops.


// 1. Console.log the sum of all the numbers in the age array.
// 2. Console.log the highest age in the array.

let sum = 0;
for (let item of age) {
    sum += item;
}
console.log(sum);


let maxAge = age[0];
for (let item of age) {
    if (item > maxAge) {
        maxAge = item; 
    }
}
console.log(maxAge);
