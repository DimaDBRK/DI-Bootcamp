import { db } from "../config/db.js";

export const getAllTodos = () => {
    return db("todos").select("id", "todo", "date","isdone").orderBy("id");
  };
  

  export const updateTodo = ({isdone}, id) => {
    return db('todos')
    .update({isdone})
    .where({id})
    .returning(['id','isdone'])
  }

  export const insertTodo = ({todo}) => {
    // console.log('name',name, 'price', price);
    return db('todos')
    .insert ({todo})
    .returning(['id','todo'])
  }