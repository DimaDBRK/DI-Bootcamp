import express from 'express';
import { _getMessage,
        _anwserPostMessage,
        _getAllTodos,
        _updateTodo,
        _insertTodo
        } from '../controllers/dc.js';

// it is trafic controller
const prouter = express.Router();

prouter.get('/hello', _getMessage);
prouter.post('/word', _anwserPostMessage);
prouter.get('/todos', _getAllTodos);
prouter.put("/todos/:id", _updateTodo);
prouter.post("/todos", _insertTodo);

export default prouter;