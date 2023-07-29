import React from "react";
import {useState, useRef, useEffect } from "react";
import NewTodoDB from "./NewTodoDB";



const BASE_URL = process.env.REACT_APP_BASE_URL;

const NewTodo = ({setTodos}) => {
    
    const [newTodo, setNewTodo] = useState("");

    const handleEnter = (event) => {
        // send post req function
        const updateTodo = async (newdata) => {
                              
                try {
                    const res = await fetch(`${BASE_URL}/api/todos`,{
                        method: 'POST',
                        headers: {
                          'Content-type': 'application/json'
                        },
                        body: JSON.stringify({todo: newdata})
                    });
                    const data = await res.json();
                    //
                    console.log(data);
                    //update info on react page
                    // update data
                    setTodos(data);
                    console.log("Updated NewTodo todoListInfo=>", data);
                    //clear input
                    setNewTodo("");
                } catch (e) {
                    console.log(e);
                }
            }
       
        if (event.keyCode === 13) {
            console.log(event.key);
            // send NewTodo to server
            updateTodo(newTodo);

           
        }

    }

    return (
        <div>
            <h4>New Todo:</h4>
            <input value = {newTodo} onChange={e => setNewTodo(e.target.value)} onKeyDown={handleEnter}/>
        </div>
    )
}

export default NewTodo;