// DC

document.getElementById("btn").addEventListener('click', start);
document.getElementById("clear").addEventListener('click', clear);

function start(event) {
    console.log("start")
    event.preventDefault();
    // get word from input
    getInput()
}

function getInput() {
    let word = document.forms[0].elements[0].value;
    word = word.toLowerCase().replace(' ','').trim();
    console.log(word)
    makeGifRequest(word);
    return word
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


async function makeGifRequest(word) {
    //consts and vars
    const textElement = document.getElementById("word");
    

    try  {
        let link = `https://api.giphy.com/v1/gifs/random?tag=${word}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`
        const response = await fetch(link) // promise
        if (response.ok) {
            const dataGif = await response.json();

            // function
            if (dataGif["data"].length === 0) {
                console.log("Cannot Find a Gif");
                throw new Error ("Cannot Find a Gif");
            } else {
        
            console.log(dataGif)
            const link = dataGif["data"]["images"]["fixed_width"]["url"]
            displayWord(word) 
            displayInfo(link, word, dataGif["data"]["id"] );
            }
        } else {
                throw new Error ("Some issues with fetch.");
            }
        } catch (err) {
            if (err.message === "Cannot find a Gif") {
                console.log("Change word")
            } else { 
                console.log("IN THE CATCH: ", err.message);
                displayError(err.message);
            }
        }


    function displayError(err) {
        textElement.textContent = err;
    }
    

    function displayInfo(link, word ,id) {
        const divClone = template.content.cloneNode(true);
        divClone.firstElementChild.setAttribute("id", id);
        divClone.firstElementChild.children[0].textContent = word;
        divClone.firstElementChild.children[1].setAttribute("src", link);
        divClone.firstElementChild.children[1].setAttribute("alt", word);
        divClone.firstElementChild.children[2].addEventListener('click', deleteImageDiv);
        document.getElementById("container").appendChild(divClone);
    
      
       
    }
    
    function displayWord(word) {
        console.log(word);
       
        textElement.textContent = word;
    }

}

// test clone
