import React from "react";
import {useState, useRef, useEffect } from "react";

const NewTodo = ({todoListInfo, setTodoDone}) => {
    console.log("NewTodo todoListInfo=>", todoListInfo);
    const [newTodo, setNewTodo] = useState("");

    const handleEnter = (event) => {
       
        if (event.keyCode === 13) {
            console.log(event.key);
           
          // insert new
            let todo_id = 1;
            let idMax = 1;
            if (todoListInfo.length > 0) {
            //find max user_id
                idMax = todoListInfo.reduce(
                    (acc, value) => {
                    return (acc = acc > value.id ? acc : value.id)
                    }, 0);
                    todo_id = idMax + 1;
            }
            setTodoDone([...todoListInfo, { todo: newTodo, id: todo_id, date: "2022-02-10", isdone: false }]);
            console.log("Updated NewTodo todoListInfo=>", todoListInfo);
            //clear input
            setNewTodo("");
          
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