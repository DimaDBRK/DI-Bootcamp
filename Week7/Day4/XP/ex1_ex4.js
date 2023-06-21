// Week7 Day4
// Dmitry Dubrov
// Ex 1 - Ex 4

// 🌟 Exercise 1 : Find The Numbers Divisible By 23
// Instructions
// Create a function call displayNumbersDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.
// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 
// 368 391 414 437 460 483
// Sum : 5313

function displayNumbersDivisible() {
    let sum = 0;
    for (let i = 0; i <= 500; i++) {
        if (i % 23 == 0) {
            console.log(i);
            sum += i;
        }
    }
    console.log(sum);
}

displayNumbersDivisible()
// Bonus: Add a parameter divisor to the function.
// displayNumbersDivisible(divisor)
// Example:
// displayNumbersDivisible(3) : Console.log all the numbers divisible by 3, 
// and their sum
// displayNumbersDivisible(45) : Console.log all the numbers divisible by 45, 
// and their sum

function displayNumbersDivisibleBonus(n) {
    let sum = 0;
    for (let i = 0; i <= 500; i++) {
        if (i % n == 0) {
            console.log(i);
            sum += i;
        }
    }
    console.log(sum);
}

displayNumbersDivisibleBonus(249)

// Exercise 2 : Shopping List
// Instructions
// 1. Add the stock and prices objects to your js file.
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

// 2. Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. 
// It means that you have 1 banana, 1 orange and 1 apple in your cart.

const shoppingList = ['banana', 'orange', 'apple']

// 3. Create a function called myBill() that takes no parameters.
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// 1) The item must be in stock. (Hint : check out if .. in)
// 2) If the item is in stock find out the price in the prices object.


function myBill() {
    let totalPrice = 0;
    for (let item of shoppingList) {
        if (item in stock) {
            if (stock[item] >= 1) {
                totalPrice += prices[item]
            }
        }
    }
    return totalPrice
}

// 4.Call the myBill() function.
console.log(myBill())

// 5. Bonus: If the item is in stock, decrease the item’s stock by 1

function myBillBonus() {
    let totalPrice = 0;
    for (let item of shoppingList) {
        if (item in stock) {
            if (stock[item] >= 1) {
                totalPrice += prices[item]
                stock[item] -= 1
            }
        }
    }
    return totalPrice
}
console.log(myBillBonus())
console.log(stock)

// Exercise 3 : What’s In My Wallet ?
// Instructions
// Note: Read the illustration (point 4), while reading the instructions

// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
// an item price
// and an array representing the amount of change in your pocket.

// In the function, determine whether or not you can afford the item.
// If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
// If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01


// 4. To illustrate:
// After you created the function, invoke it like this:
// changeEnough(4.25, [25, 20, 5, 0])
// The value 4.25 represents the item’s price
// The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
// The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

// Examples
// changeEnough(14.11, [2,100,0,0]) => returns false
// changeEnough(0.75, [0,0,20,5]) => returns true

function changeEnough(itemPrice, amountOfChange) {
    const changeValue = [0.25, 0.10, 0.05, 0.01]
    let sum = 0;
    for (let i = 0; i <  amountOfChange.length; i++) {
        if (amountOfChange[i] > 0) {
            sum += amountOfChange[i] * changeValue[i];
        }
    }

    return itemPrice <= sum;
}

console.log(changeEnough(14.11, [2,100,0,0]))
console.log(changeEnough(0.75, [0,0,20,5]))

// 🌟 Exercise 4 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:
// 1. Define a function called hotelCost().
// - It should ask the user for the number of nights they would like to stay in the hotel.
// - If the user doesn’t answer or if the answer is not a number, ask again.
// - The hotel costs $140 per night. The function should return the total price of the hotel.

function hotelCost() {
    let daysUser;
    do {
        daysUser = prompt('Input qty nights: ');
    }
    while ((isNaN(daysUser) || daysUser < 1)  && daysUser != null);
    const costNight = 140;
    return parseInt(daysUser) * costNight;
}

// console.log(hotelCost())

// 2. Define a function called planeRideCost().
// - It should ask the user for their destination.
// - If the user doesn’t answer or if the answer is not a string, ask again.
// - The function should return a different price depending on the location.
//      “London”: 183$
//      “Paris” : 220$
//       All other destination : 300$

function planeRideCost() {
    let destination;
    const locationPrice = {
        'london': 183,
        'paris': 220
    }

    do {
        destination = prompt('Input destination: ');
    }
    
    while ((!isNaN(destination) || typeof destination != 'string' || destination.trim() in ['']) && destination != null);

    if (destination != null) {
        let destinationClean =  destination.trim().toLowerCase();
        const price = (destinationClean in locationPrice) ? locationPrice[destinationClean] : 300;
        return price;
    }
    else {
        return null;
    }
}

// console.log(planeRideCost())

// 3. Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.
function rentalCarCost() {
    let daysCar;
    do {
        daysCar = prompt('Input qty days for Car: ');
    }
    while ((isNaN(daysCar) || daysCar < 1)  && daysCar != null);
    const costDay = 40;
    const res = (daysCar < 10) ?  daysCar * costDay : daysCar * costDay * (1 - 0.05);
    return res;
}

// console.log(rentalCarCost())

// 4. Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

function totalVacationCost() {
    const x =  hotelCost();
    const y =  planeRideCost();
    const z =  rentalCarCost();
    if (x != null && y != null && z != null) {
        return x + y + z;
    }
    else {
        return "Try again"
    }
    
}
// 5. Call the function totalVacationCost()
console.log('Tets:', totalVacationCost())

// 6. Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() 
// function. You need to change the 3 first functions, accordingly.

function hotelCostBonus() {
    let daysUser;
    do {
        daysUser = prompt('Input qty nights: ');
    }
    while ((isNaN(daysUser) || daysUser < 1)  && daysUser != null);
    const costNight = 140;
    const hotelPrice = parseInt(daysUser) * costNight;

    let destination;
    do {
        destination = prompt('Input destination: ');
    }
    
    while ((!isNaN(destination) || typeof destination != 'string' || destination.trim() in ['']) && destination != null);

    let daysCar;
    do {
        daysCar = prompt('Input qty days for Car: ');
    }
    while ((isNaN(daysCar) || daysCar < 1)  && daysCar != null);


    return [hotelPrice, destination, daysCar]
}

function planeRideCostBonus(destination) {
   
    const locationPrice = {
        'london': 183,
        'paris': 220
    }

    if (destination != null) {
        let destinationClean =  destination.trim().toLowerCase();
        const price = (destinationClean in locationPrice) ? locationPrice[destinationClean] : 300;
        return price;
    }
    else {
        return null;
    }
}

function rentalCarCostBonus(daysCar) {
    const costDay = 40;
    const res = (daysCar < 10) ?  daysCar * costDay : daysCar * costDay * (1 - 0.05);
    return res;
}

function totalVacationCostBonus() {
    const arr = hotelCostBonus();
    const x =  arr[0];
    const y =  planeRideCostBonus(arr[1]);
    const z =  rentalCarCostBonus(arr[2]);
    if (x != null && y != null && z != null) {
        return x + y + z;
    }
    else {
        return "Try again"
    }
    
}

console.log('Bonus:',totalVacationCostBonus());