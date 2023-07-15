// add listeners
const addListeners = () => {
    console.log("Added Listeners");
    const allInputs = document.querySelectorAll('input');
    allInputs.forEach((element) => {
        element.addEventListener("input", checkInputs);
    })

}

//Make sure to disable any submit button if an input is empty.
const checkInputs = (event) => {
    //check values of all inputs
    let checkValue = true;
    //get all input elemnts of fther this.elemnt

    const formInputs = event.target.parentElement.querySelectorAll('input');
    const formButton = event.target.parentElement.querySelectorAll('button')[0];
    
    //check in lop value => if one length < 1 => check false.
    formInputs.forEach((element) => {if (element.value.length < 1) checkValue = false});
    // if true -> switch button inside parents element
    if (checkValue) {
        console.log("switch on button");
        formButton.disabled = false;
    } else { formButton.disabled = true; };
}


// render data at info box - 2 registration 
const render2 = (arr) => {
    const html = arr.map(item => {
        return `<div>
        <p>OK! Hello ${item.first_name} ${item.last_name} Your username: ${item.username} and id: ${item.user_id} </p>
        </div>`
    });
    console.log(html);

    document.getElementById("info-box2").innerHTML = html.join("");
}

// render data at info box - 2 registration 
const render1 = (text) => {
    const html = `<div>
        <p>${text}</p>  
        </div>`
    document.getElementById("info-box1").innerHTML = html;
}



const renderError = (text) => {
    const html = `<div>
        <p>${text}</p>
        </div>`
  
    document.getElementById("info-box2").innerHTML = html;
}


const register = async () => {
    console.log("Register starts");
    //collect info from inputs
    const firstName = document.getElementById('firstname-register-input').value;
    const lastName = document.getElementById('lastname-register-input').value;
    const email = document.getElementById('email-register-input').value;
    const userName = document.getElementById('username-register-input').value;
    const password = document.getElementById('password-register-input').value;
    try {
        const res = await fetch('api/users',{
            method:'POST',
            headers: {
                "content-type":"application/json"
            },
            body: JSON.stringify({
                first_name: firstName,
                last_name: lastName,
                email: email,
                username: userName,
                password: password
            })
            });

            if (res.status === 200) {
                const data = await res.json();
                console.log(res);
                render2(data);
            } else {
                const data = await res.json();
                data.msg
                console.log("other status of resp:", data.msg);
                renderError(`Error ${res.status}: ${data.msg}`);
            }
    } catch (err) {
        console.log("ERROR FROM SERVER:", err)
    }

}

//
const login = async () => {
    console.log("Login starts");
       //collect info from inputs

       const userName = document.getElementById('username-login-input').value;
       const password = document.getElementById('password-login-input').value;
       try {
           const res = await fetch('api/login',{
               method:'POST',
               headers: {
                   "content-type":"application/json"
               },
               body: JSON.stringify({
                    username: userName,
                    password: password
               })
               });
   
               if (res.status === 200) {
                   const data = await res.json();
                //    console.log(res);
                   console.log(data);
                   render1(data.result);
               } else {
                   const data = await res.json();
                   data.msg
                   console.log("other status of resp:", data.msg);
                   render1(`Error ${res.status}: ${data.msg}`);
                //    renderError(`Error ${res.status}: ${data.msg}`);
               }
       } catch (err) {
           console.log("ERROR FROM SERVER:", err)
       }
   
}







// Driver
addListeners();