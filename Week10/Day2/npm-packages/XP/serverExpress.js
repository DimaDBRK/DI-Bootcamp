//XP_1
// Exercise 3 : Express
const express = require('express');

const app = express();

app.listen(3000, () => {
    console.log(`My server is listening on port 3000`);
});

//add GET
app.get('/', (req,res) => {
    const html = `<div>
    <h1>Express</h2>
    <h2>Good</h4>
    <p>Lib</p>
    </div>`
    
    res.send(html); 
})