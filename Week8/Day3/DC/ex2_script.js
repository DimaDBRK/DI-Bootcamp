// DC
// Daily Challenge: Car Inventory

// Instructions
// Part I

// Create a function getCarHonda(carInventory) that takes a single parameter. carInventory‘s value is an array which is an inventory of cars (see the array of objects below)
// The function should
// loop through the array of object and return the first car with the name “Honda”.
// then, return a string in the format This is a {car_make} {car_model} from {car_year}.
// Hint : Find an array method that returns the value of the first element in an array that pass a test.
// Use the cars inventory below:
const inventory = [
  { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
  { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
  { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
  { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
  { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

// Option 1
function getCarHonda(arr) {
  const car =  arr.find((element) => element["car_make"] == "Honda");
  return `This is a ${car["car_make"]} ${car["car_model"]} from ${car["car_year"]}`
}

console.log(getCarHonda(inventory));


// Part II

// Create a function sortCarInventoryByYear(carInventory) that takes a single parameter. carInventory‘s value is an array which is an inventory of cars (see the array of objects below)
// the function should return an inventory that is sorted by car_year, ascending.
// Hint : Check out this tutorial on the sort method
// Use the cars inventory below:



// The output should be

// [
//   { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
//   { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
//   { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
//   { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
//   { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
// ];

// Option 1. sort
function sortCarInventoryByYear(carInventory) {
  carInventory.sort(function (x, y) {
    return x.car_year - y.car_year;
    });

  }
console.log("Option 1 - Sort");
console.log("Initial before sort");
console.log(inventory);
console.log("Sorted");
sortCarInventoryByYear(inventory);
console.log("Test after sort");
console.log(inventory);

// Option 2. ToSorted new function which works Only in Browser, it doesn't change initial object
const inventory2 = [
  { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
  { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
  { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
  { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
  { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

function sortCarInventoryByYearNewObject(carInventory) {
  return carInventory.toSorted(function (x, y) {
    return x.car_year - y.car_year;
    });

  }

  console.log("Option 2 - Sort");
  console.log("Initial before sort");
  console.log(inventory2);
  console.log("Sorted");
  // console.log(sortCarInventoryByYearNewObject(inventory2)); 
  console.log("Test after sort");
  console.log(inventory2);

  // Option 3.My Sort in console and make new array

  const inventory3 = [
    { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
    { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
    { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
    { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
    { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
  ];
  
function sortCarInventoryByYearNewObject(carInventory) {
    const  arr = [...carInventory];
    arr.forEach((element, index) => {
      for (let j = 0; j < arr.length - index - 1; j++) {
        if (arr[j]["car_year"] > arr[j + 1]["car_year"]){
          const min = arr[j + 1];
          arr[j + 1] = arr[j];
          arr[j] = min;
        }
      }
    });

    return arr
  }
      


console.log("It was");
console.log(inventory3);
console.log("My sort");
console.log(sortCarInventoryByYearNewObject(inventory3));
console.log("Initial");
console.log(inventory3);