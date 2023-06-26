const myform = document.forms[0];

function getValuesForm(event) {
    event.preventDefault();
    let volume;
    const inputRadius = event.target.radius.value;
    if (!isNaN(inputRadius) && inputRadius.length > 0) {
        console.log("start calculation");
        volume = 4 / 3 * 3.14 * (Number(inputRadius)**3);
        console.log(volume);
        const text = document.createTextNode(volume);
        myform.volume.value = volume;
            
    } else {
        console.log("Wrong data");
        myform.volume.value = "Wrong data";
    }
}



myform.addEventListener('submit', getValuesForm);