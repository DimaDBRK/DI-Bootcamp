// 🌟 Exercise 2 : Move The Box
// Copy the code above, to a structured HTML file.
// In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions



function draw(x) {
    const box = document.getElementById("animate");
    box.style.left = x + 'px';
  }
function myMove() {
    const stopParametr = 350;
    let counter = 1;

    let myInterval = setInterval(function () {
        if (counter >= stopParametr) {
            draw(0);
            clearInterval(myInterval); // finish the animation after 2 seconds
            return;
        } else {
            draw(counter);

            // addParagraph();
            counter += 1;
        }
        }, 5);
    
     
}

// Driver
