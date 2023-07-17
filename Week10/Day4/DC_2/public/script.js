const formRegister = document.querySelector("#registerForm");
formRegister.addEventListener("submit", registerUser);

async function registerUser (event) {
    event.preventDefault()
    const data = new FormData(formRegister);
    const objData = Object.fromEntries(data);
    console.log(objData);


    const responsePost = await fetch('/registeruser',{
        method : "POST",
        headers : {
            "Content-Type" : "application/json"
        },
        body : JSON.stringify(objData)
    })
    console.log(responsePost);
    if (responsePost.ok) {
        const result = await responsePost.json();
        const div = document.getElementById("resultUser");
        div.textContent = result;
    }
}