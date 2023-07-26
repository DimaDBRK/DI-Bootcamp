import React from "react";
import {useState, useRef, useEffect } from "react";

const BASE_URL = process.env.REACT_APP_BASE_URL;
console.log(BASE_URL);

const ServerRequests = () => {
    const link = `${BASE_URL}/api/word`;
    const inputRef = useRef();

    
    const [answer, setAnswer] = useState();

    const sendPostRequest = (event) => {
        event.preventDefault();
        console.log("Button pressed");

        const info = async () => {
        
            try {
                
                const dataToServer = {
                    msg: inputRef.current.value
                  }

                const res = await fetch(link, {
                method: 'POST',
                
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(dataToServer)
                });
                if (res.ok) {
                    const data = await res.json();
                    console.log(data.msg);
                    setAnswer(`I received your POST request. This is what you sent me: ${data.msg}`);
                   
                } else {
                    throw new Error("Problem on server side");
                }
                
            } catch (e) {
                console.log(e);
                setAnswer("Error");
            }
        }

        info();
    }

    return (
        <>
        <form onSubmit={sendPostRequest}>
            <input ref={inputRef}/>
            <input type="submit" value="Send POST data"/>
        </form>
        <p>{answer}</p>
        
        </>
      
    )
  }

  export default ServerRequests;