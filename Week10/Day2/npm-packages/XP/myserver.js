//XP_1
// Exercise 1 : HTTP
const http = require("http");

const server = http.createServer((request, response) => {
    console.log('Get the request from client');
    const html = `<div>
            <h1>First</h2>
            <h2>Second</h4>
            <p>Third</p>
            </div>`
   
    response.end(html)
});

server.listen(3001, () => {
    console.log("run on 3001")
});