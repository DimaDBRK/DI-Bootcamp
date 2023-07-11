// Exercise 1 : Reading From A File In Node.JS
// Instructions
// Create a text file and write something inside (example: ‘Some Text To See’)
// Create an fs.js file, and inside use the Node JS File System to read the text file and console.log the output in the terminal

const fs = require('fs')

fs.readFile('text.txt', 'utf-8', (err, data) => {
    console.log("data from file:", data);
    if (err) return console.log(err);
});

// Exercise 2 : Writing Files With Node JS
// Instructions
// Create an fs.js file, and use the Node js File System to create a new text file and write to it.

// console.log("new file");
// fs.writeFile('text2.txt', "- test data", 'utf-8', (err) => {
//     if (err) return console.log(err);
// });

// 2. Use the Node js File System to append some other text to the text file. (Example:”Buy orange juice”)

// fs.appendFile('text2.txt', "Buy orange juice", 'utf-8', (err) => {
//     if (err) return console.log(err);
// }) // file, data cod, funct fo err

//  res in file - > - test dataBuy orange juice

// 3. Use the Node js File System to delete the file.

// delete a file

// fs.unlink("text2.txt", (err) => {
//   if (err) return console.log(err);
// });