import React from "react";
import {useState, useRef, useEffect } from "react";
import NewTodoDB from "./NewTodoDB";
import { useParams } from "react-router-dom";


const BASE_URL = process.env.REACT_APP_BASE_URL;
    
const CardsDB = (props) => {
   
    const linkAll = `${BASE_URL}/api/todos`;

    const [todoListInfo, setTodos] = useState([]);

    useEffect(()=>{
        all()
    },[])

    const all = async () => {
        try {
            const res = await fetch(linkAll);
            const data = await res.json();
            setTodos(data);
        } catch (e) {
            console.log(e);
        }
    }

    // console.log("Cards todoListInfo=>", todoListInfo);
    
    const handleCardClick = (event) => {
        const id = +event.currentTarget.getAttribute('todo-id');
        if (event.button === 0 & event.detail>=2) {
            console.log("we will srt to done");
            
            const updateTodo = async (dataUpd) => {
                
               
                try {
                    const res = await fetch(`${BASE_URL}/api/todos/${id}`,{
                        method: 'PUT',
                        headers: {
                          'Content-type': 'application/json'
                        },
                        body: JSON.stringify(dataUpd)
                    });
                    const data = await res.json();
                    //
                    console.log(data);
                    //update info on react page
                    all();
                } catch (e) {
                    console.log(e);
                }
            }

            const todoForUpdate = todoListInfo.find(obj => obj.id === id);
            console.log("todoForUpdate=>", todoForUpdate);
            updateTodo({isdone: !todoForUpdate.isdone});
       
         
        }
    }


    return(
        <div>
            <h1>TODO List from DataBase:</h1>
            <h6>Double click to remove</h6>
            {   
                todoListInfo.map((item)=>{
                    
                    if (!item.isdone) {
                        return(
                            <div todo-id={item.id} key={item.id} onClick={handleCardClick} className="Card">
                                <p>{item.todo}</p>
                                <p>date: {item.date}</p>
                            </div>
                        )
                    
                    };
                    
                })
               
            }
            {
                todoListInfo.findIndex(item=>!item.isdone) >=0? <p></p>:<p>No TODO in list</p>
            }
            <NewTodoDB setTodos = {setTodos}/>
        </div>
       
    )
}

export default CardsDB;