// Instructions
const numbers = [5,0,9,1,7,4,2,6,3,8];

// Using the .toString() method convert the array to a string.
// Using the .join()method convert the array to a string. Try passing different values into the join.
// Eg .join(“+”), .join(” “), .join(“”)
// Bonus : To do this Bonus look up how to work with nested for loops
// Sort the numbers array in descending order, do so using for loops (Not using built-in sort methods).
// The output should be: [9,8,7,6,5,4,3,2,1,0]
// Hint: The algorithm is called “Bubble Sort”
// Use a temporary variable to swap values in the array.
// Use 2 “nested” for loops (Nested means one inside the other).
// Add comments and console.log the result for each step, this will help you understand.
// Requirement: Don’t copy paste solutions from Google


console.log(numbers, typeof(numbers));

console.log("toString");
let strTest = numbers.toString();
console.log(strTest, typeof(strTest));

console.log("join()");
let strTest2 = numbers.join();
console.log(strTest2, typeof(strTest2));

console.log("join('')");
let strTest3 = numbers.join(''); 
console.log(strTest3, typeof(strTest3));

console.log("join('+')");
let strTest4 = numbers.join('+'); 
console.log(strTest4, typeof(strTest4));

console.log("join(' ')");
let strTest5 = numbers.join(' '); 
console.log(strTest5, typeof(strTest5));

console.log("Bubble Sort");
// const numbers = [5,0,9,1,7,4,2,6,3,8];
// The output should be: [9,8,7,6,5,4,3,2,1,0]
console.log(numbers.length);
let tempDidgit;
let maxDidgit;
let position;

for (let i = 0; i < numbers.length; i++ ) {
    tempDidgit = numbers[i];
    maxDidgit = numbers[i];
    position = i;
    console.log(i, tempDidgit, maxDidgit, position);

    for (let j = i; j < numbers.length; j++) {
        if (numbers[j] > maxDidgit) {
            maxDidgit = numbers[j];
            position = j;
        }
    }

    if (position != i) {
        numbers[i] = maxDidgit;
        numbers[position] = tempDidgit;
    }

}

console.log(numbers);



