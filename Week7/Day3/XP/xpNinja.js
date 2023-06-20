// Exercise 1 : Checking The BMI
// Instructions
// Hint:
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

// Create two objects, each object should hold a person’s details. Here are the details:
// FullName
// Mass
// Height

// Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person

// Outside of the objects, create a JS function that compares the BMI of both objects.

// Display the name of the person who has the largest BMI.

let personOne = {
    fullName: "Albert", 
    mass: 100,
    height: 189,  
    personBMI: function () {
        let bmi = Number((this.mass / (this.height/100) ** 2).toFixed(2));
        return bmi;
    }
}


let personTwo = {
    fullName: "Dan", 
    mass: 150,
    height: 169,  
    personBMI: function () {
        let bmi = Number((this.mass / (this.height/100) ** 2).toFixed(2));
        return bmi;
    }
}
console.log(personOne.personBMI())
console.log(personTwo.personBMI())

function checkBmi(Object1, Object2) {
    let res = Object1.fullName;
    
    if (Object2.personBMI() > Object1.personBMI()) {
        res = Object2.fullName;
    }
    return res
}

console.log(checkBmi(personOne, personTwo));


// Exercise 2 : Grade Average
// Instructions
// Hint:
// - This Exercise is trickier then the others. You have to think about its structure before you start coding.
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

// In this exercise we will be creating a function which takes an array of grades as an argument and will console.log the average.

// Create a function called findAvg(gradesList) that takes an argument called gradesList.

// Your function must calculate and console.log the average.

// If the average is above 65 let the user know they passed

// If the average is below 65 let the user know they failed and must repeat the course.
// Bonus Try and split parts 1,2 and 3,4 of this exercise to two separate functions.
// Hint One function must call the other.

gradesList1 = [56, 67, 67, 89, 90]
gradesList2 = [56, 57, 47, 39, 20]

function findAvg(gradesList) {
    let res = 0;
    for (let item of gradesList) {
        res += item;
    }
    return(Math.round(res/gradesList.length));
}


function checkResult(grade) {
    let result = `Your grade is ${grade} it is below 65, so you must repeat the course.`;
    if (grade >= 65) {
        result = `Your grade is ${grade} it is more 65, so you Pass!!!`;
    }
    console.log(result);
}
console.log(findAvg(gradesList1));
console.log(findAvg(gradesList2));

checkResult(findAvg(gradesList1));
checkResult(findAvg(gradesList2));