// Week7 Day2
// Dmitry Dubrov
// Exercises XP

// 🌟 Exercise 1 : List Of People
// Instructions
const people = ["Greg", "Mary", "Devon", "James"];


// Part I - Review About Arrays
// 1. Write code to remove “Greg” from the people array.
console.log(people);
people.shift();

console.log(people);


// 2. Write code to replace “James” to “Jason”.
//Option 1
people.pop();
people.push('Jason');
console.log(people);
// Option 2
people[2] = 'Jason';

// 3. Write code to add your name to the end of the people array.

people.push('Dima');
console.log(people);

// 4. Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

console.log(people.indexOf('Mary'));


// 5. Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

let peopleCopy = people.slice(1,3)
console.log(peopleCopy);

// 6. Write code that gives the index of “Foo”. Why does it return -1 ? 
console.log(people.indexOf('Foo'));
// -1 means that Foo not in array

// 7. Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?
let last;
last = people[(people.length-1)];
console.log(last);

// Part II - Loops
// 1. Using a loop, iterate through the people array and console.log each person.

for (let item of people) {
    console.log(item);
}

// 2. Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
// Hint: take a look at the break statement in the lesson.

for (let item of people) {
     console.log(item);
    if (item == 'Devon')  {
        break;
    }
}


// 🌟 Exercise 2 : Your Favorite Colors
// Instructions
// 1. Create an array called colors where the value is a list of your five favorite colors.
// 2. Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .


colors = ['Black','Blue', 'White', 'Green', 'Yellow'];
for (let i in colors) {
    console.log(`My # ${(parseInt(i)+1)} choice is ${colors[i]}`);
}

// 3. Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

colors = ['Black','Blue', 'White', 'Green', 'Yellow'];
for (let i in colors) {
    let suff;
    switch (parseInt(i)+1) {
        case 1:
            suff = 'st'
            break;
        case 2:
            suff = 'nd'
            break;
        case 3:
            suff = 'rd'
            break;
        default:
            suff = 'th'
            break;
    }

    console.log(`My ${(parseInt(i)+1)}${suff} choice is ${colors[i]}`);
}

// 🌟 Exercise 3 : Repeat The Question
// Instructions
// 1. Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

let number;
do
{
    number = prompt("Please enter your number"); 
    console.log(typeof(number));
    console.log(isNaN(number));

}
while (parseInt(number) < 10 || isNaN(number));


// 🌟 Exercise 4 : Building Management
// Instructions:
// Review About Objects
// 1. Copy and paste the above object to your Javascript file.

// 2. Console.log the number of floors in the building.

// 3. Console.log how many apartments are on the floors 1 and 3.

// 4. Console.log the name of the second tenant and the number of rooms he has in his apartment.

// 5. Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building['numberOfFloors']);

console.log(building['numberOfAptByFloor']['firstFloor'], building['numberOfAptByFloor']['thirdFloor'] );

// 4. Console.log the name of the second tenant and the number of rooms he has in his apartment.
let nameOfTenant = building['nameOfTenants'][1];
console.log(nameOfTenant, building['numberOfRoomsAndRent'][nameOfTenant.toLowerCase()][0]);

// 5. Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
console.log('Sarah’s  rent: ', building['numberOfRoomsAndRent']['sarah'][1], ', ', 'David’s  rent: ', building['numberOfRoomsAndRent']['david'][1]);
console.log('Sarah’s and David’s rents: ', building['numberOfRoomsAndRent']['sarah'][1] + building['numberOfRoomsAndRent']['david'][1]);
console.log('Sarah’s and David’s rents is bigger than Dan’s rent : ', (building['numberOfRoomsAndRent']['sarah'][1] + building['numberOfRoomsAndRent']['david'][1]) > building['numberOfRoomsAndRent']['dan'][1]);
if ((building['numberOfRoomsAndRent']['sarah'][1] + building['numberOfRoomsAndRent']['david'][1]) > building['numberOfRoomsAndRent']['dan'][1]){
    building['numberOfRoomsAndRent']['dan'][1] = 1200
}
console.log('Dan’s rent : ', building['numberOfRoomsAndRent']['dan'][1]);

// 🌟 Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

const family = {
    dad: 'Albert',
    mom: 'Izabel',
    son: 'Shon',
}

for (let key in family) {
    console.log(key);
}

for (let key in family) {
    console.log(family[key]);
}

// Exercise 6 : Rudolf
// Instructions
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
let res = '';
for (let key in details) {
    res = res + key + ' ' + details[key] + ' '
}

console.log(res);

// Exercise 7 : Secret Group
// Instructions
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”
let societyName = '';
for (let item of names) {
    societyName += item[0]
}
console.log(societyName.split('').sort().join(''));

// Option 2
const names2 = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names2.sort();
console.log(names2);
let societyName2 = '';
for (let item of names2) {
    societyName2 += item[0]
}
console.log(societyName2);