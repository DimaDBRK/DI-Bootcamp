// Daily Challenge: Planets



// Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?

// Create an array which value is the planets of the solar system.

const planets = [
                {'name': 'Mercury', 'moons': 0},
                {'name': 'Venus', 'moons': 0},
                {'name': 'Earth', 'moons': 1},
                {'name': 'Mars', 'moons': 2},
                {'name': 'Jupiter', 'moons': 95},
                {'name': 'Saturn', 'moons': 146},
                {'name': 'Uranus', 'moons': 27},
                {'name': 'Neptune', 'moons': 14},
]

const colors = ["lightgreen","yellow","green","red","blue","pink","white","lightblue"]

const container = document.body.firstElementChild;
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
for (let i = 0; i < planets.length; i++) {
    const newBox = document.createElement("div");
    const newDiv = document.createElement("div");
    newDiv.setAttribute("class",`planet`);
    newDiv.style.backgroundColor = colors[i];
    const text = document.createTextNode(planets[i]['name']);
    newDiv.appendChild(text);
    
    
   
    newBox.appendChild(newDiv);
    // Bonus: Do the same process to create the moons.
    for (let j = 0; j < planets[i]['moons']; j++) {
        const newMoonDiv = document.createElement("div");
        newMoonDiv.setAttribute("class",`moon`);
        newMoonDiv.style.cssText  = "display: inline-block";
        newBox.appendChild(newMoonDiv);
    }
    // newDiv.style.display  = "inline-block";
    container.appendChild(newBox);
}
// Each planet should have a different background color. (Hint: you could add a new class to each planet -
//  each class containing a different background-color).

// Finally append each div to the <section> in the HTML (presented below).

