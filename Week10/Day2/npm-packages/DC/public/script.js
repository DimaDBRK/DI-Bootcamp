// fetch('/users')
//     .then(res => res.json())
//     .then(data => {
//         console.log(data);
//         render(data);
//     })
//     .catch((e) => {
//         console.log(e);
//     });

// const render = (data) => {
//     //html - arr of strings
//     html = `<span id = "name">Hello friend: ${data.firstname} ${data.lastname}</span>`
//     console.log(html);
//     //add on page
//     document.getElementById('name-box').innerHTML = html;
// }

document.getElementById('btn').addEventListener('click', start);

const urlToSend = '/formData';  


function start(event) {
   
    //check data
    function checkValue() {
        let res = true;
        let message = "";
        let email = "";

        const allInputs = document.querySelectorAll('input');
        let errorElement = [];
        console.log(allInputs);
        
        // for email
        const validateEmail = (email) => {
            const re = /\S+@\S+\.\S+/;
            return re.test(email);
        };

            

        for (let inp of allInputs) {
           
            if (inp.value.length === 0) {
                errorElement.push(`- ${inp.id} is empty`);
                res =  false;
            } else if (inp.id === "email" && !validateEmail(inp.value)) {
                errorElement.push(` - add correct email`);
                res =  false;
            } else {
                if (inp.id === "email") {email = inp.value}
                if (inp.id === "message") {message = inp.value}
            }
        }
        const data = {email: email, message: message}
        return [res, errorElement, data]
    }
    
    const check = checkValue();
    console.log("check", check);
    // let checkValue = true;
    if (event.button === 0 && check[0]) {
        event.preventDefault();
        console.log("Start");
        render(["Sending data to server..."]);
        const data = check[2];
        console.log("data", data);
        //function to send data
        sendDataToApi(urlToSend, data);

    } else if (event.button === 0 && !check[0]) {
        event.preventDefault();
        console.log(check[1]);
        //show error list
        render(check[1]);
    }
}   

const render = (arr) => {
    const html = arr.map(item => {
        return `<p>${item}</p>`
    });
    console.log(html);
    //add on page
    document.getElementById('info').innerHTML = html.join("")
};

//send data with fetch

async function sendDataToApi(url, data) {
  try  {
    console.log("data to send:", JSON.stringify(data));
    const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
    });

    console.log("response from server:", response);
    if (response.ok) {
      console.log('Data sended OK!');
      const responseData = await response.text();
      const info = responseData;
      console.log("Info from response: ", responseData);
      render(["Data sended OK!", responseData]);
    } else {
      throw new Error ('Failed to send: ', );
    }
  } catch (err) {
    console.log("IN THE CATCH: ", err.message);
    render([`IN THE CATCH: ", ${err.message}`]);
  }
}
