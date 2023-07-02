// DC


function showRequest() {
 
    const text = getInformationFromForm();
    document.getElementById("result").innerHTML = text;

}

function getInformationFromForm() {
    const res = []
    
    var reciveParams = new URLSearchParams(window.location.search);
    reciveParams.get("name")
    
    return `${reciveParams.get("name")} ${reciveParams.get("lastname")}` 
}

showRequest() 


