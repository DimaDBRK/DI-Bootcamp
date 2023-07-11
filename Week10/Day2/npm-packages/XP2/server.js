//XP_2
// Exercise 1 : Express & JSON
const express = require('express');

const app = express();

app.use(express.urlencoded({ extended: true }))
// parse application/json
app.use(express.json())

//static
app.use('/',express.static(__dirname + '/public'));

const user = {firstname: 'John',lastname: 'Doe'}

app.listen(3000, () => {
    console.log(`My server is listening on port 3000`);
});


//add GET
app.get('/users', (req,res) => {
    
    if (Object.keys(user).length === 0) return res.status(404).json({msg: "Data not found"}); // return will stope code
    console.log("server send:", user);
    res.json(user); //  We can use res.json if know type of data
})


// Exercise 2 : Express & Parameters
// Instructions
// In the server.js file, create your server using express.
// Create a route /, and use a GET request method.
// The path of the route should contain the route parameter id.
// The handler function of the route should respond with the value of the route parameter. Check out req.params.
// Run on port http://localhost:3000/ and add an id, for example http://localhost:3000/1234
// The response should be the JSON Object. Console.log this object and display it on the DOM.

// get  id
app.get('/:id', (req,res) => {
    //params - after / in request => {"id": ...}
    const data = req.params;
    const id = req.params.id;
    
    console.log(data); // { id: '1' }
    res.json(data) // {"id":"1"}
    
})

// Exercise 3: Express & Static Files
// Instructions
// Create a public folder, that contains an HTML file. This HTML file can contain some CSS and some JavaScript (for example a head tag with some classes for styling, and in the body a button with an onClick attribute calling a Javascript function with an alert).
// In a server.js file create your server using express.
// Your server on http://localhost:3000/ should serve the HTML file. Check out the lesson named Express Routes & Queries in the Course Notes, more specifically the part “How To Serve Static Files In Express”