//

const PixelsHight = 32;
const PixelsLength = 60;
const colors = ["red","orange","yellow","green","blue","lightblue","brown","black","white"]
let color = colors[0];
let check = false;
let takeColor = false;

function stopDraw() {
    console.log(document.getElementsByTagName("*"));
    Array.from(document.getElementsByTagName("*")).forEach((element) => element.addEventListener("click", checkOff));
}

function checkOff() {
    console.log("OK");
    check = false;
}
function makeField(length, hight) {
    const container = document.getElementsByClassName("grid-container-field")[0];    
    console.log(container);
    for (i = 1; i <= (hight * length); i++) {
        const newPixel = document.createElement("div");
        // const headerText = document.createTextNode(`${i}`);
        // newPixel.appendChild(headerText);
        newPixel.classList.add("grid-item-pixels")
        // newPixel.addEventListener("click", changeBackground);
        newPixel.addEventListener("mousedown", changeBackgroundOn);
        newPixel.addEventListener("mouseup", changeBackgroundOff);
        newPixel.addEventListener("mouseover", changeBackgroundSmart);
        newPixel.addEventListener("dblclick", getColor);
        container.appendChild(newPixel);
    }
}

function makeColors() {
    const container = document.getElementsByClassName("grid-container-menu")[0];    
    console.log(container);
    colors.forEach((item) => {
        const newColorElement = document.createElement("div");
        const headerText = document.createTextNode(`${item}`);
        newColorElement.appendChild(headerText);
        newColorElement.classList.add("grid-item-color")
        newColorElement.style.background = item;
        newColorElement.setAttribute("id", item);
        if (item === color) {
            newColorElement.style.border = "1px solid black";
        }
        newColorElement.addEventListener("click", changeColor);
        container.appendChild(newColorElement);

    })
       
}



//clear
const buttonClear = document.getElementById("clear");
buttonClear.addEventListener("click", clear);

function changeColor() {
    document.getElementById(color).style.border = `1px solid gray`;
    color = this.id;
    
    document.getElementById(color).style.border = "1px solid black";
}

function getColor(event) {
   
        console.log("Get color DBLCLICK")
//     document.getElementById(color).style.border = `1px solid gray`;
//     // color = this.backgroundColor;
    
//     document.getElementById(color).style.border = "1px solid black";
    }


function clear() {
    const pixels = document.getElementsByClassName("grid-item-pixels");
    console.log(pixels);
    Array.from(pixels).forEach((element) => element.style.background = "white");
}
    

// get all pixels by style.
// const pixels = document.getElementsByClassName("grid-item-pixels");
// console.log(pixels);
// Array.from(pixels).forEach((element) => element.addEventListener("click", changeBackground));


// make function wich change background
function changeBackgroundOn(event) {
    if (event.button === 0) {
    check = true;
    console.log("On - change background");
    this.style.background = color;
    } else if (event.button === 2) {
        console.log("Get color")
    }
    
}

function changeBackgroundOff(event) {
    if (event.button === 0) {
        check = false;
        console.log("Off - change background");
        this.style.background = color;
    }
}

function changeBackgroundSmart(event) {
    console.log(event.button)
    if (event.button === 0) {
        if (check) {console.log("check press ok - change background");
        this.style.background = color;}
    }
}

//driver
makeColors();
makeField(PixelsLength, PixelsHight);
stopDraw();