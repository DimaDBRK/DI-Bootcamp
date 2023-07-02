// DC

document.getElementsByTagName("button")[0].addEventListener('click', showRequest);


function showRequest(event) {
   event.preventDefault();
   const text = JSON.stringify(getInformationFromForm(), null, 2);
   
   document.getElementById("result").innerHTML = text;

}

function getInformationFromForm() {
    const res = []
    // /ex1.html?name=John&lastname=Doe -> [name=John,lastname=Doe] -> [[name,John],[lastname,Doe]] -> object
    location.search.slice(1).split("&").forEach((element) => res.push(element.split("=")));
    return Object.fromEntries(res);
}