// DC
document.getElementById("btn").addEventListener('click', start);
document.getElementById("switch-element").addEventListener('click', switchValue);

let result = 0;
function start(event) {
        
    if (event.button === 0 && result === 1) {
        event.preventDefault();
        clearInfo();
        console.log("start")
       // request to server
        let fromCurrencyValue = document.getElementById("from").value;
        let toCurrencyValue = document.getElementById("to").value;
        let amount = document.getElementById("amount").value;
        
        function amountCheck(amountToCheck) {
            let result = false;
            if (+amountToCheck === +amountToCheck) {
                 console.log("it is ok")
                 amountToCheck = Math.abs(+amountToCheck);
                 if (amountToCheck > 0) {
                    amount = amountToCheck;
                    result = true
                };
            }
            return result
        }
        
     
          
        
        if (amountCheck(amount)) {
            console.log(fromCurrencyValue, toCurrencyValue, amount);
            getConvertResult(fromCurrencyValue, toCurrencyValue, amount)
        } else {
            console.log("Wrong amount");
            showInfo("Wrong amount");
        }
                    
    } else if (event.button === 0 && result === 0) {
        showInfo("Check connection to API");
    }

}

function showInfo(info) {
    const infoElement = document.getElementById("info");
    infoElement.textContent = info;
    const resElement = document.getElementById("result");
    resElement.textContent = "";
}

function showResult(res) {
    
    const resElement = document.getElementById("result");
    resElement.textContent = res.toFixed(2);
}

function clearInfo() {
    const infoElement = document.getElementById("info");
    infoElement.textContent = "Welcom!";
}


async function getCurrencyCodes() {
    let allCurrencyCodes = {};
    try  {
        let link = "https://v6.exchangerate-api.com/v6/bf6fa29ad077ae16dac8bae7/codes"
        const response = await fetch(link) // promise
        console.log(response)
        if (response.ok) {
            const dataCurrency = await response.json();

           
        
            console.log(dataCurrency["supported_codes"])
            allCurrencyCodes = dataCurrency["supported_codes"] //arr of arrays
            addCurrencyToInput(allCurrencyCodes) 
            result = 1;
            
        } else {
                throw new Error ("Some issues with fetch.");
            }
        } catch (err) {
            
                console.log("IN THE CATCH: ", err.message);
                showInfo(err.message);
    
        }
   
       
    }
    
    function addCurrencyToInput(arr) {
        // take elements
        const elementFrom = document.getElementById("from");
        const FromOptionsElementsOld = [...elementFrom.children];
        FromOptionsElementsOld.forEach((element) => {element.remove()})
        
       
        const elementTo = document.getElementById("to");
        const toOptionsElementsOld = [...elementTo.children];
        toOptionsElementsOld.forEach((element) => {element.remove()})
        
       
        arr.forEach(element => {
            //add options to From
            
            const newOptionFrom = document.createElement("option");
            newOptionFrom.setAttribute("value", element[0]);
            newOptionFrom.textContent = `${element[0]} - ${element[1]}`
            elementFrom.appendChild(newOptionFrom);
            
            //add options to From
           
            const newOptionTo = document.createElement("option");
            newOptionTo.setAttribute("value", element[0]);
            newOptionTo.textContent = `${element[0]} - ${element[1]}`
            elementTo.appendChild(newOptionTo);

            console.log(element[0], `${element[0]} - ${element[1]}`)

           
            });
       
        //add to To
        
    }

async function getCurrencyCodes() {
    let allCurrencyCodes = {};
    try  {
        let link = "https://v6.exchangerate-api.com/v6/bf6fa29ad077ae16dac8bae7/codes"
        const response = await fetch(link) // promise
        console.log(response)
        if (response.ok) {
            const dataCurrency = await response.json();

           
        
            console.log(dataCurrency["supported_codes"])
            allCurrencyCodes = dataCurrency["supported_codes"] //arr of arrays
            addCurrencyToInput(allCurrencyCodes) 
            result = 1;
            
        } else {
                throw new Error ("Some issues with fetch.");
            }
        } catch (err) {
            
                console.log("IN THE CATCH: ", err.message);
                showInfo(err.message);
    
        }
   
       
    }

async function getCurrencyCodes() {
    let allCurrencyCodes = {};
    try  {
        let link = "https://v6.exchangerate-api.com/v6/bf6fa29ad077ae16dac8bae7/codes"
        const response = await fetch(link) // promise
        console.log(response)
        if (response.ok) {
            const dataCurrency = await response.json();

           
        
            console.log(dataCurrency["supported_codes"])
            allCurrencyCodes = dataCurrency["supported_codes"] //arr of arrays
            addCurrencyToInput(allCurrencyCodes) 
            result = 1;
            
        } else {
                throw new Error ("Some issues with fetch.");
            }
        } catch (err) {
            
                console.log("IN THE CATCH: ", err.message);
                showInfo(err.message);
    
        }
   
       
}
async function getConvertResult(currFrom, currTo, amount) {
    let allCurrencyCodes = {};
    try  {
        let link = `https://v6.exchangerate-api.com/v6/bf6fa29ad077ae16dac8bae7/pair/${currFrom}/${currTo}/${amount}`
        const response = await fetch(link) // promise
        console.log(response)
        if (response.ok) {
            const dataConvertationResults = await response.json();

           
        
            console.log(dataConvertationResults["conversion_result"]);

            conversionResult = dataConvertationResults["conversion_result"];
            showResult(conversionResult);
            
        } else {
                throw new Error ("Some issues with fetch.");
            }
        } catch (err) {
            
                console.log("IN THE CATCH: ", err.message);
                showInfo(err.message);
    
        }
         
}

function switchValue() {
    let fromCurrencyValue = document.getElementById("from").value;
    let toCurrencyValue = document.getElementById("to").value;
   
    document.getElementById("from").value = toCurrencyValue;
    document.getElementById("to").value = fromCurrencyValue;
}

getCurrencyCodes()

