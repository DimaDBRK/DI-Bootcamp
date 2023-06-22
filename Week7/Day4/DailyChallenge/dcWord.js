const arr = ["How","Wow","Test","LongLong"];
let star = '*'
let lengthMax = 0;

function findLengthMax(array) {
    for (let word of array) {
        if (word.length > lengthMax) {
            lengthMax = word.length
        }
    }
    return lengthMax
}

function drawLine() {
    let line ='';
    for (let i = 0; i < (lengthMax + 4); i++ ) {
        line += star;
    }
    console.log(line)
}

function drawWord(array) {
   
    for (let word of array){
        let line ='* ';
        line += word
        for (let j = (2 + word.length); j < (lengthMax+3); j++) {
            line += " "}
        line += star
        console.log(line)
    }
}

// Driver
console.log('Tests')
console.log(findLengthMax(arr))

drawLine()
drawWord(arr)
drawLine()

