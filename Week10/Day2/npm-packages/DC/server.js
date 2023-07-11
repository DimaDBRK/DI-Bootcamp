//Daily Challenge: Express
// Instructions
// Use Express to create a few routes:
// The route /aboutMe/:hobby sends the name of one hobby (ie. the value of the route parameter). If the parameter is not a string (ie. numbers or else), set the status to 404.
// The route /pic : displays an HTML file with a picture of your choice.
// The route /form: displays an HTML file.
// Requirements:
// The HTML file must be in the public folder.
// The HTML file must contain a form to contact you.
// The form must contain the inputs email and message. (add some HTML form validations)
// Output:
// You should get the data and display it on the browser at the route /formData.
// For example, “john@gmail.com sent you a message “Love your new website”.
// const express = require('express');
const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }))
// parse application/json
app.use(express.json())

//static
app.use('/',express.static(__dirname + '/public'));


app.listen(3000, () => {
    console.log(`My server is listening on port 3000`);
});



// The route /aboutMe/:hobby sends the name of one hobby 
app.get('/aboutMe/:hobby', (req,res) => {
    //params - after / in request => {"id": ...}
    const data = req.params;
    const hobby_name = data.hobby;
    console.log("res:", hobby_name, "type", typeof(hobby_name)); // { id: '1' }
    // If the parameter is not a string (ie. numbers or else), set the status to 404.
    if (/[^a-zA-Z]/.test(hobby_name)) return res.status(404).json({msg: "Wrong type of hobby"}); // return will stope code
    
    res.json(hobby_name) // {"id":"1"}
    
})

//send static file pic.html
app.get('/pic', (req,res) => {
    res.sendFile(__dirname + '/public/picture.html'); //to send filer
})

//form
app.get('/form', (req,res) => {
    res.sendFile(__dirname + '/public/form.html'); //to send file
    
})


//post
app.post('/formData', (req,res) => {
    console.log(req.body);
    // need library or package to extract data from body - body-parser. In 18 version it is in express
    console.log(req.body.message);
    console.log(req.body.email);
    res.end(`You recive message "${req.body.message}" from : ${req.body.email}`); // send - will string by auto. We can use res.json if know type of data
    
})