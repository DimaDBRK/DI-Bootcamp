fetch('/users')
    .then(res => res.json())
    .then(data => {
        console.log(data);
        render(data);
    })
    .catch((e) => {
        console.log(e);
    });

const render = (data) => {
    //html - arr of strings
    html = `<span id = "name">Hello friend: ${data.firstname} ${data.lastname}</span>`
    console.log(html);
    //add on page
    document.getElementById('name-box').innerHTML = html;
}

    document.getElementById('btn').addEventListener('click', showAlert);

function showAlert() {
    alert("Hello from JavaScript");
}