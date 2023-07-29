import {
    getAllTodos,
    updateTodo,
    insertTodo
    
  } from "../models/dc.js";


//READ - GET get all products -> _ before it 
export const _getMessage = (req, res) => {
    const data = {msg: "Hello From Express"};
    try {
        res.json(data);
    } catch(e) {
        console.log(e);
        res.status(500).json({ msg: e.message }); // or e.message
    }
}

export const _anwserPostMessage = (req, res) => {
    try {
        const info = req.body;
        console.log(info);
        res.json(info);
    } catch(e) {
        console.log(e);
        res.status(500).json({ msg: e.message }); // or e.message
    }
}

//TODOS
// READ - GET - get all products
export const _getAllTodos = (req, res) => {
    getAllTodos()
      .then((data) => {
        res.json(data);
      })
      .catch((e) => {
        console.log(e);
        res.status(404).json({ msg: e.message });
      });
  };

  export const _updateTodo = (req, res) => {
    updateTodo(req.body, req.params.id)
      .then((data) => {
        res.json(data);
      })
      .catch((e) => {
        console.log(e);
        res.status(404).json({ msg: e.message });
      });
  };

  export const _insertTodo = (req, res) => {
    // console.log("body", req.body);
    insertTodo(req.body)
      .then((data) => {
        // res.json(data);
        _getAllTodos(req,res)
      })
      .catch((e) => {
        console.log(e);
        res.status(404).json({ msg: e.message });
      });
  };