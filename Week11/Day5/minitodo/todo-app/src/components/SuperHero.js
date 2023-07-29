import React from "react";
import {useState, useRef, useEffect } from "react";
import NewTodo from "./NewTodo";

const todoList = [
    {
        todo: "Card1",
        id: 1,
        date: "2022-02-10",
        isdone: false
    },
    {
        todo: "Card2",
        id: 2,
        date: "2022-02-10",
        isdone: false
    },
    {
        todo: "Card2",
        id: 3,
        date: "2022-02-10",
        isdone: false
    }
]

const Cards = (props) => {
   

    const [todoListInfo, setTodoDone] = useState(todoList);
    console.log("Cards todoListInfo=>", todoListInfo);
    
    const handleCardClick = (event) => {
        const id = +event.currentTarget.getAttribute('todo-id');
        if (event.button === 0 & event.detail>=2) {
            console.log("we will srt to done");
            setTodoDone(todoListInfo.map((item)=> 
                    item.id === id ? {...item, isdone: !item.isdone} : {...item}
                    )
            );
            console.log(todoListInfo.findIndex(item=>!item.isdone));

        }
    }

    // useEffect(()=>{
        
    // },[todoListInfo])

    return(
        <div>
            <h1>TODO List:</h1>
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
            <NewTodo todoListInfo = {todoListInfo} setTodoDone = {setTodoDone}/>
        </div>
       
    )
}

export default Cards;