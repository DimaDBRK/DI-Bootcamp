// Exercises XP
// 🌟 Exercise 1 : Colors
// Instructions
// Using this array :

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// Write a JavaScript program that displays the colors in the following order 
// : “1# choice is Blue.” “2# choice is Green.” “3# choice is Red.” ect…
colors.forEach((color, index) => {console.log(`${index+1}# choice is ${color}.`)});

// Check if at least one element of the array is equal to the value “Violet”. 
// If yes, console.log("Yeah"), else console.log("No...")
const checkResult = (colors.some(element => element ==="Violet")) ? "Yeah" : "No...";
console.log(checkResult);


// 🌟 Exercise 2 : Colors #2
// Instructions
// Using these arrays :

const colorsList = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];
// Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” 
// “2nd choice is Green.” “3rd choice is Red.” ect…
// Hint : Use the array methods taught in class and ternary operator.
colorsList.forEach((color, index) => {console.log(`${index+1}${(index < 3)? ordinal[index+1]: ordinal[0]} choice is ${color}.`)});

// Exercise 3 : Analyzing
// Instructions
// Analyze these pieces of code before executing them. What will be the outputs ?
// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);
// ---> ['bread', "carrot", "potato", 'chicken', "carrot", "potato"]

// ------2------
const country = "USA";
console.log([...country]);
// ---> [ 'U', 'S', 'A' ]

// ------Bonus------
let newArray = [...[,,]];
console.log(newArray);
// ---> [ undefined, undefined ]

// 🌟 Exercise 4 : Employees
// Instructions
// Using this array:

const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

// 1. Using the map() method, push into a new array the firstname of the user and a welcome message. 
// You should get an array that looks like this :
// const welcomeStudents = ["Hello Bradley", "Hello Chloe", "Hello Jonathan", "Hello Michael", "Hello Robert", "Hello Wes", "Hello Zach"]

const welcomeStudents = users.map((element) => `Hello ${element["firstName"]}`);
console.log(users);
console.log(welcomeStudents);

// 2. Using the filter() method, create a new array, containing only the Full Stack Residents.

const LinkFullStackResidents = users.filter((element) => element["role"] === 'Full Stack Resident');
console.log("It was:");
console.log(users);
console.log("Test 2.");
console.log(LinkFullStackResidents);

// 3. Bonus : Chain the filter method with a map method, to return an array containing only the lastName of 
// the Full Stack Residents.
const namesFullStackResidents = users.filter((element) => element["role"] === 'Full Stack Resident').map((element) => element["firstName"]);

console.log("Test 2.");
console.log(namesFullStackResidents);

// 🌟 Exercise 6 (or 5) : Star Wars
// Instructions
// Using this array 
const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

// Use the reduce() method to combine all of these into a single string.
const resStr = epic.reduce((accumulator, element) => {
    return accumulator + (element != epic[0]? element : element.charAt(0).toLocaleUpperCase()) + ( (element != epic[epic.length -1])? " ": ".");
},""); // add initial value
console.log(resStr)


// 🌟 Exercise 7 (or 6) : Employees #2
// Instructions
// Using this object:

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];

// Using the filter() method, create a new array, containing the students that passed the course.
const studentsPass = students.filter((element) => element['isPassed']);
console.log("Test 7.1");
console.log(studentsPass);

const studentsPassText = students.filter((element) => element['isPassed']).map((element) => `Good Job ${element["name"]} you passed the course in ${element["course"]}`);
console.log("Test 7.2");
console.log(users);
console.log(studentsPassText);



// Bonus : Chain the filter method with a forEach method, to congratulate the students with their name 
// and course name (ie. “Good job Jenner, you passed the course in Information Technology”, 
// “Good Job Marco you passed the course in Robotics” ect…)

const studentsPassText2 = [];
students.filter((element) => element['isPassed']).forEach((element) => studentsPassText2.push(`Good Job ${element["name"]} you passed the course in ${element["course"]}`));
console.log("Test Bonuse");
console.log(studentsPassText2);