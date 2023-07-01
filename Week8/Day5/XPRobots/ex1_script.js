//XP project Robots
//Additional functions:
// - smart search - search inputted letters in any order in name.
// - change robot picture buy double left button click
// - copy robot image from one Robo-card to another. Press and hold "Shift" button till end of copy process, 
//right click on robot picture to be copied, chose new card to Paste image, click on it. Image should changed.
// - it check robot's name, in case it is too long, slice to 17 symbols

//Const, vars, data
const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'https://robohash.org/1?200x200'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'https://robohash.org/2?200x200'
    },
    {
      id: 3,
      name: 'Clementine Bauch',
      username: 'Samantha',
      email: 'Nathan@yesenia.net',
      image: 'https://robohash.org/3?200x200'
    },
    {
      id: 4,
      name: 'Patricia Lebsack',
      username: 'Karianne',
      email: 'Julianne.OConner@kory.org',
      image: 'https://robohash.org/4?200x200'
    },
    {
      id: 5,
      name: 'Chelsey Dietrich',
      username: 'Kamren',
      email: 'Lucio_Hettinger@annie.ca',
      image: 'https://robohash.org/5?200x200'
    },
    {
      id: 6,
      name: 'Mrs. Dennis Schulist',
      username: 'Leopoldo_Corkery',
      email: 'Karley_Dach@jasper.info',
      image: 'https://robohash.org/6?200x200'
    },
    {
      id: 7,
      name: 'Kurtis Weissnat',
      username: 'Elwyn.Skiles',
      email: 'Telly.Hoeger@billy.biz',
      image: 'https://robohash.org/7?200x200'
    },
    {
      id: 8,
      name: 'Nicholas Runolfsdottir V',
      username: 'Maxime_Nienow',
      email: 'Sherwood@rosamond.me',
      image: 'https://robohash.org/8?200x200'
    },
    {
      id: 9,
      name: 'Glenna Reichert',
      username: 'Delphine',
      email: 'Chaim_McDermott@dana.io',
      image:'https://robohash.org/9?200x200'
    },
    {
      id: 10,
      name: 'Clementina DuBuque',
      username: 'Moriah.Stanton',
      email: 'Rey.Padberg@karina.biz',
      image:'https://robohash.org/10?200x200'
    }
    ];

let tempLink;
let copyStatus = false;
let check = false;

// events
document.getElementsByTagName("input")[0].addEventListener('input', search);
document.onkeydown = copyOn;
document.onkeyup = copyOff;
//functions
function makeCards(arr) {
    const container = document.getElementById("container");    
    console.log(container);

    
    arr.forEach((item) => {
        // console.log(item[id])
        const newCard = document.createElement("div");
        newCard.classList.add("card");
        newCard.setAttribute("id", item["id"]);
        //avatar with img
        const newAvatar = document.createElement("div");
        newAvatar.classList.add("avatar");

        const newImg = document.createElement("img");
        newImg.setAttribute("src", item["image"]);
        newImg.addEventListener("dblclick", changeImage, false);
        // on prees
        newImg.addEventListener("click", copyImage, false);
        // on long press
        // newImg.addEventListener("mouseup", pasteImage, false);
        

        newAvatar.appendChild(newImg);
            //add avatar with img to Card
        newCard.appendChild(newAvatar);

        // name
        const robotName = document.createTextNode(`${item["name"].length <= 17? item["name"]: item["name"].substring(0, 17) }`);
        const newPName = document.createElement("p");
        newPName.classList.add("name");
        newPName.appendChild(robotName);
        newCard.appendChild(newPName);

        // email
        const email = document.createTextNode(`${item["email"]}`);
        const newEmail = document.createElement("p");
        newEmail.classList.add("email");
        newEmail.appendChild(email);
        newCard.appendChild(newEmail);

        
        // add card to container
        container.appendChild(newCard);

    })
       
}
//change Image

function changeImage(event) {
    if (event.button === 0) {
        
        console.log("change image");
        const i  = getRandomIntInclusive(10, 20);
        this.setAttribute("src", `https://robohash.org/${i}?200x200`);
        // newLinkGenerator;
    }

   


    function getRandomIntInclusive(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1) + min); // The maximum is inclusive and the minimum is inclusive
    }

    
}

// copy on
function copyOn(event) {
    console.log('on', event.keyCode);
    if (event.keyCode===16) {copyStatus = true;}
}

function copyOff(event) {
    console.log('0ff', event.keyCode);
    check = false;
    if (event.keyCode===16) {copyStatus = false;}

}

// copy link
function copyImage(event) {
    
    if (event.button === 0 && copyStatus) {
        if (check) {
            check = false;
            console.log("psate image");
            console.log('temp link: ', tempLink);
            this.setAttribute("src", tempLink);
            
            console.log(tempLink);

        } else {
            check = true;
            console.log("copy image");
            tempLink = this.src;
            // this.id = 
            console.log(tempLink);
        }
        // console.log("copy image");
        
        // tempLink = this.src;
        // console.log(tempLink);
        
    }
}
        // on long press
function pasteImage(event) {
       
    if (event.button === 0 && copyStatus) {
   
        console.log("psate image");
        console.log('temp link: ', tempLink);
        this.setAttribute("src", tempLink);
        console.log(tempLink);
    }
}

//psate link



// search
function search(event) {
   
    let checkMe = true;
    const search = this.value.toLowerCase();
   
    function checkSearchIsInElement(element) {
        checkMe = true;
        console.log(element["name"].toLowerCase());
        console.log([...search]);
        [...search].forEach((letter) => {       
           
            checkMe = element["name"].toLowerCase().includes(letter) ? checkMe : false
            console.log("letter: ",letter, "elememnt- ", element["name"].toLowerCase(), "res", checkMe);
        });
        
        return checkMe;
        }

    const searchResult = robots.filter((element) => checkSearchIsInElement(element));
         
    if (searchResult.length > 0) {
        // clear
        clear();
        // add robots
        makeCards(searchResult);

    } else {
        clear();
        //show no info
        const container = document.getElementById("container");
        const newCard = document.createElement("div");
        newCard.classList.add("card");
        
        // name
        const robotName = document.createTextNode("No Robot with this name.");
        const newPName = document.createElement("p");
        newPName.classList.add("name");
        newPName.appendChild(robotName);
        newCard.appendChild(newPName);

        // add card to container
        container.appendChild(newCard);


        }

    // });
   
}

//clear
function clear() {
    const cards = document.getElementsByClassName("card");
    Array.from(cards).forEach((element) => element.remove());
}
   



//Driver
makeCards(robots);

//Tests

// const lettersList = [..."abc"]


// letters.forEach((letter) => {
//     checkMe = word.includes(letter) ? checkMe: false;
//     console.log( letter, word.includes(letter))
// });

// console.log(checkMe);const word = "albertc";
// let checkMe = true;
