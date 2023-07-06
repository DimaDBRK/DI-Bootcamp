// miniproject

//const and vars
document.getElementById("btn").addEventListener('click', start);
// store prev ID
let prevID = 0;

function start(event) {
    //check if left button
    if (event.button === 0) {
        console.log("start")
       // request to server
      
       makeSWRequest();
    }
}

function deleteImageDiv(event) {
    this.parentElement.remove()
}


function clear(event) {
    //clear text
    document.getElementById("word").textContent = ""
    //clear input
    document.forms[0].elements[0].value = ""
    const container = document.getElementById("container")
    while (container.firstChild) {
        container.removeChild(container.lastChild);
      }
   

}


async function makeSWRequest() {
    //consts and vars
    const textElement = document.getElementById("word");
    
    //make request ti SW API
    try  {
        // show download
        document.getElementById("download-logo").classList.remove('hideme');
        document.getElementById("download-text").classList.remove('hideme');
        document.getElementById("info-box").classList.add('shadow');
        // hide others:
        document.getElementById("name").classList.add('hideme');
        const pElements = [...document.getElementsByClassName(`text`)];
        pElements.forEach((element) => {element.classList.add('hideme')})


        //get random ID from function and check if it is not like previouse one

        let id = 0;
        // console.log(getRandomIntInclusive(1, 83));
        function getNewlink() {
            do { 
                id = getRandomIntInclusive(1, 83); //17
                console.log(id)
            }
            while (id == prevID);
            prevID = id;
            // console.log(id)
            let link = `https://www.swapi.tech/api/people/${id}`
    
            return link
        }
        
        const response = await fetch(getNewlink()) // promise
        
        if (response.ok) {
            const dataSW = await response.json();
            // const dataSW = await response.json();


            // function to check if response includes info
            if (dataSW["result"].length === 0) {
                console.log("No info");
                throw new Error ("No info");
            } else {
                console.log("Ok, get homeworld");
                // function to get howeworld.
                let homeworldLink = dataSW["result"]["properties"]["homeworld"];
                console.log(homeworldLink);
                let result ="unknown";
                if (homeworldLink.includes("https://www.swapi.tech/api/planets/")) {
                    //fetch info
                    try  {
                        const response2 = await fetch(homeworldLink) // promise
                        if (response.ok) {
                            const dataWRD = await response2.json();
                            console.log(dataWRD);
                            result = dataWRD["result"]["properties"]["name"]
                        }
                        else {
                            throw new Error ("Some issues with fetch for homeworld.");
                        }
                    } catch (error) {
                        console.log("IN THE CATCH: ", error.message);
                    }
                } 


                
                const person = {
                name: dataSW["result"]["properties"]["name"],
                gender: dataSW["result"]["properties"]["gender"],
                birth_year: dataSW["result"]["properties"]["birth_year"],
                height: dataSW["result"]["properties"]["height"],
                homeworld: result
                }

            console.log(person)

            
            displayPerson(person) 
          
            }
        } else {
            
            const dataSW = await response.json();

            if (dataSW["message"] === "not found") {
                console.log("Error -  Person not found ")
                throw new Error ("Person not found!");
            } else {
                throw new Error ("Some issues with fetch.");
            }
            
            }
        } catch (err) {
            if (err.message === "Person not found!") {
                console.log("Person not found!")
                displayError("Person not found!") 
            } else if (err.message.includes("not valid JSON")) {
                console.log("Some issues with link or fetch.");

            } else { 
                console.log("IN THE CATCH: ", err.message);
                displayError(err.message)
                // displayError(err.message);
            }
        }

    
    function getRandomIntInclusive(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
    }

    function displayError(err) {
        console.log(document.getElementById("download-logo"));
        document.getElementById("download-logo").classList.add('hideme');
        document.getElementById("download-text").classList.add('hideme');
        document.getElementById("name").classList.remove('hideme');
        document.getElementById("info-box").classList.remove('shadow');
        document.getElementById("name").textContent = err
        
    }
    

    function displayPerson(person) {
        // hide download
        console.log(document.getElementById("download-logo"));
        document.getElementById("download-logo").classList.add('hideme');
        document.getElementById("download-text").classList.add('hideme');
        document.getElementById("name").classList.remove('hideme');
        document.getElementById("info-box").classList.remove('shadow');
        
        //get info from object in loop and show
        Object.entries(person).forEach(([key, value]) => {
            
            document.getElementById(`${key}-text`).textContent = value;
            document.getElementById(key).classList.remove('hideme');
            });
        // divClone.firstElementChild.children[0].textContent = person[0];
        
    
      
       
    }
    
    function displayWord(word) {
        console.log(word);
        textElement.textContent = word;
    }

}

// test clone
