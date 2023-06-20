// Daily Challenge: Stars

// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *


function starOneLoop() {
    str = '*'
    for (let i = 0; i <= 5; i++ ) {
        console.log(str);
        str += ' *';
    }

}

function starNestedLoops() {
    
    for (let line = 1; line <= 6; line++ ) {
        str = ''
        for (let starQty = 1; starQty <= line; starQty++)
            str += '* '
            console.log(str);
    }

}

starOneLoop()
starNestedLoops()