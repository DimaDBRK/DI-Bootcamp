import React from "react";
import {useState, useRef, useEffect } from "react";

const BASE_URL = process.env.REACT_APP_BASE_URL;
console.log(BASE_URL);

const HeaderRequest = () => {
    
    const link = `${BASE_URL}/api/hello`;

    
    const [headerFromServer, setHeader] = useState();
    
    useEffect(()=>{
        getHeader()
    })
    
    const getHeader = async () => {
        
            try {
             

                const res = await fetch(link);
                if (res.ok) {
                    const data = await res.json();
                    console.log(data.msg);
                    setHeader(data.msg);
                   
                } else {
                    throw new Error("Problem on server side");
                }
                
            } catch (e) {
                console.log(e);
                setHeader("Error from DB");
            }
        }


    return (
        <>
            <p>Here will be Header from DB:</p>
            <h3>{headerFromServer}</h3>
        
        </>
      
    )
  }

  export default HeaderRequest;