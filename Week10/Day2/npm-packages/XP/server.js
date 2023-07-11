//XP_1
// Exercise 2 : HTTP & JSON
const http = require("http");

const server = http.createServer((request, response) => {
    console.log('Get the request from client');
    const user = {
        firstname: 'John',
        lastname: 'Doe'
    }
    console.log(JSON.stringify(user)); //=> convert to string
    response.end(JSON.stringify(user));
});

server.listen(8080, () => {
    console.log("run on 8080")
});