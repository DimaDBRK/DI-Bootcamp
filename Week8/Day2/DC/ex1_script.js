// Daily Challenge: Groceries
// Hint: To do this daily challenge, take a look at today’s lesson Pass By Value & Pass By Reference

// Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method.

// Create another arrow function named cloneGroceries.
// In the function, create a variable named user that is a copy of the client variable. (Tip : make the user variable equal to the client variable)
// Change the client variable to “Betty”. Will we also see this modification in the user variable ? Why ?
// In the function, create a variable named shopping that is equal to the groceries variable.
// Change the value of the totalPrice key to 35$. Will we also see this modification in the shopping object ? Why ?
// Change the value of the payed key to false. Will we also see this modification in the shopping object ? Why ?

// Invoke the cloneGroceries function.

let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayGroceries = (object) => {
    const fruits = object.fruits;
    fruits.forEach(item => console.log(item))
        
}

displayGroceries(groceries);


const cloneGroceries = () => {
    let user  = client;
    
    console.log("user:",user);
    console.log("client:",client);
    console.log("change client to Betty");
    
    client = "Betty";
    
    console.log("client:",client);
    console.log("user:",user);
    // Why ? -> = by value, for user we make copy of initial value of client
    
    let shopping  = groceries;
    
    
    console.log("shopping - totalPrice :",shopping['totalPrice']);
    console.log("groceries - totalPrice :",groceries['totalPrice']);
    console.log("change groceries to 35$");

    groceries['totalPrice'] = "35$";

    console.log("shopping - totalPrice :",shopping['totalPrice']);
    console.log("groceries - totalPrice :",groceries['totalPrice']);
    // Why ? -> = both var linked to the same object, after we chage param in one, object was chaged.

    console.log("shopping - payed :", shopping['other']['payed']);
    console.log("groceries - payed :", groceries['other']['payed']);
    console.log("change groceries to false");
    groceries['other']['payed'] = false;
    console.log("shopping - payed :", shopping['other']['payed']);
    console.log("groceries - payed :", groceries['other']['payed']);

    // Why ? -> = both var linked to the same object

}

cloneGroceries();